# azure-functions

A repository for testing Azure Functions Service

## Setup

Setup a python environment as discussed in the main README.md and then from this folder run:

```bash
cd azure-functions
pip install -r requirements.txt
```

## Running

Deploy through VS Code, DevOps or otherwise and see the Azure portal for URL's.

If running locally you will need to include a local.settings.json with a pointer to a storage account where an output queue will be accessed / created.

Run locally using the command below and then browse the end points.

```bash
func host start
```

See [this link](https://docs.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-storage-queue-python) for more information and accessing queues through the command line.

The functions can be accessed through different URL's where hte latter takes a category and optional id in the path

http://localhost:7071/api/HttpTrigger?name=Myname
http://localhost:7071/api/products/cat/10?name=HiRoute