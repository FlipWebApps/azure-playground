import argparse
import joblib
import matplotlib.pyplot as plt
import numpy as np
import os

from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.utils.multiclass import unique_labels

from amlrun import get_AMLRun


def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return fig, ax


def train(output_dir='outputs', kernel='linear', penalty=1.0):
    # Safely get the Azure ML run
    run = get_AMLRun()

    # loading the iris dataset
    iris = datasets.load_iris()

    # X -> features, y -> label
    X = iris.data
    y = iris.target
    class_names = iris.target_names

    # dividing X, y into train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    # training a linear SVM classifier
    from sklearn.svm import SVC
    svm_model_linear = SVC(kernel=kernel, C=penalty).fit(X_train, y_train)
    y_pred = svm_model_linear.predict(X_test)

    # model accuracy for X_test
    accuracy = svm_model_linear.score(X_test, y_test)
    print('Accuracy of SVM classifier on test set: {:.2f}'.format(accuracy))

    if run is not None:
        run.log('Accuracy', np.float(accuracy))

    # Plot non-normalized confusion matrix
    fig, _ = plot_confusion_matrix(y_test, y_pred, classes=class_names,
                                   title='Confusion matrix, without normalization')
    plt.savefig(os.path.join(output_dir, 'confusion_matrix.png'))
    if run is not None:
        run.log_image('Confusion matrix, without normalization', plot=fig)

    # Plot normalized confusion matrix
    fig, _ = plot_confusion_matrix(y_test, y_pred, classes=class_names,
                                   normalize=True,
                                   title='Normalized confusion matrix')
    # plt.plot()
    plt.savefig(os.path.join(output_dir, 'confusion_matrix_normalised.png'))
    if run is not None:
        run.log_image('Normalized confusion matrix',  plot=plt)

    # os.makedirs(output_dir, exist_ok=True)

    # files saved in the "outputs" folder are automatically uploaded into
    # Azure ML Service run history
    joblib.dump(svm_model_linear,
                os.path.join(output_dir, 'model', 'model.joblib'))


def main():
    parser = argparse.ArgumentParser()
    # environment parameters
    # parser.add_argument(
    #     '--data-folder',
    #     help="GCS or local path to training data",
    #     required=True
    # )
    parser.add_argument(
        "--output-dir", type=str, default="outputs",
        help="GCS location to write checkpoints and export models"
    )

    # training specific parameters
    parser.add_argument('--kernel', type=str, default='linear',
                        help='Kernel type to be used in the algorithm')
    parser.add_argument('--penalty', type=float, default=1.0,
                        help='Penalty parameter of the error term')

    # parse the arguments
    args = parser.parse_args()

    # setup output directory
    model_output_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        args.output_dir)
    os.makedirs(model_output_dir, exist_ok=True)

    train(model_output_dir, args.kernel, args.penalty)


if __name__ == '__main__':
    main()
