# Azure DevOps example for running python tests

wallet.pt / test_wallet.py example from: 

https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

## Setup

Setup a python environment as discussed in the main README.md and then from this folder run:

```bash
cd python-testing
pip install -r requirements.txt
```

## Lint

```bash
flake8
```

## Test

```bash
pytest
```

## Azure DevOps Pipeline
Configure a new pipeline to reference this repository and the included azure-pipelines.yml
