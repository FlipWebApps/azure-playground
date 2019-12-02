# azure-playground

A repository for testing various Azure functionality.

## Setup

Open a command prompt int eh repository root and then create and activate a python virtual environment. Here using venv, alternatively use conda:

```bash
python3 -m venv .env
.env\Scripts\activate
pip install --user ipykernel
python -m ipykernel install --user --name=azure-playground.venv
```

See any additional readme in each folder for further setup or run instructions.

## azure-functions

[![Build Status](https://dev.azure.com/mhew/azure-playground/_apis/build/status/azure-functions)](https://dev.azure.com/mhew/azure-playground/_build/latest?definitionId=11)

Basic Python HTTP and HTTP with route->Azure storage functions.

Deploys automatically using Azure DevOps. Alternatively through VS Code or the azure CLI.

## data-factory

## devops-databricks

[![Build Status](https://dev.azure.com/mhew/test/_apis/build/status/devops-databricks?branchName=master)](https://dev.azure.com/mhew/test/_build/latest?definitionId=8&branchName=master)

## ml-service

[![Build Status](https://dev.azure.com/mhew/azure-playground/_apis/build/status/ml-service)](https://dev.azure.com/mhew/azure-playground/_build/latest?definitionId=12)

ML Service experiment with DevOps / MLOps

## python-testing

[![Build Status](https://dev.azure.com/mhew/test/_apis/build/status/python-testing)](https://dev.azure.com/mhew/test/_build/latest?definitionId=3)

Azure DevOps example for running python tests

## python-webapp

[![Build Status](https://dev.azure.com/mhew/test/_apis/build/status/python-webapp)](https://dev.azure.com/mhew/test/_build/latest?definitionId=4)<br />
