import logging

import azure.functions as func


def main(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> str:
    # For testing we log the content
    logging.info(f"HTTP trigger executed!")
    logging.info(f"Headers: {req.headers}")
    logging.info(f"Params: {req.params}")
    logging.info(f"Route Params: {req.route_params}")
    logging.info(f"Body: {req.get_body()}")
    try:
        logging.info(f"Body JSON: {request.get_json()}")
    except ValueError:
        pass

    name = req.params.get('name')
    category = req.route_params.get('category')
    id = req.route_params.get('id')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        # send a message to the QueueMessage output binding
        msg.set(name)

        # Return the HttpResponse
        return func.HttpResponse(f"Hello to {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )