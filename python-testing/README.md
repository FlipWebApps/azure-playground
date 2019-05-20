# Azure DevOps example for running python tests

wallet.pt / test_wallet.py example from: 

https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

## Running locally

Setup using:
```
mkdir pytest_project
cd pytest_project
python3 -m venv pytest-env
```
Activate environment:
```
source pytest-env/bin/activate
```

Run tests using:

```
pytest -q test_wallet.py
```

## Azure DevOps Pipeline
Configure a new pipeline to reference this repository and the included azure-pipelines.yml
