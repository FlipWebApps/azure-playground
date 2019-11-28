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

A basic Python HTTP->Azure storage function app.

Deploys automatically using Azure DevOps. Alternatively open the folder azure-functions in VS Code with the Azure Functions extension added to be able to deploy manually through VS Code (doesn't work if opened from the repo root).

## data-factory

## devops-databricks

[![Build Status](https://dev.azure.com/mhew/test/_apis/build/status/devops-databricks?branchName=master)](https://dev.azure.com/mhew/test/_build/latest?definitionId=8&branchName=master)

## python-testing

[![Build Status](https://dev.azure.com/mhew/test/_apis/build/status/python-testing)](https://dev.azure.com/mhew/test/_build/latest?definitionId=3)

Azure DevOps example for running python tests

## python-webapp

[![Build Status](https://dev.azure.com/mhew/test/_apis/build/status/python-webapp)](https://dev.azure.com/mhew/test/_build/latest?definitionId=4)<br />
