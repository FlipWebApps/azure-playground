# Azure DevOps example for running python tests

wallet.pt / test_wallet.py example from: 

https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

## Running locally

### Setup using
```
cd python-testing
python -m venv pytest-env
```

### Activate environment
Max / Linux
```
source pytest-env/bin/activate
```

Windows
```
python-webapp\Scripts\activate
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Run using

```
flask run
```

## Azure DevOps Pipeline
Configure a new pipeline to reference this repository and the included azure-pipelines.yml
