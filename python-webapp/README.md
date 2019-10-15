# Azure DevOps example for a Flask App Service webapp

## Running locally

Setup using:
```
cd python-webapp
python -m venv python-webapp
```
Activate environment:
```
source python-webapp/bin/activate
```

Run tests using:

```
pytest -q test_wallet.py
```

## Azure DevOps Pipeline
Configure a new pipeline to reference this repository and the included azure-pipelines.yml:
* Select Builds -> New
* Select the *classic editor* option
* Select *GitHub* and chose a repository
* Select the template *Configuration as code -> YAML*
* Set the YAML file path to python-webapp/azure-pipelines.yaml
* Fill out variables:
	* ConnectedServiceName - 
	* WebAppName - The name of your web app

This pipeline will build and deploy as one step.