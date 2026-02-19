import requests
import config
import data

def post_create_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER,
                         json=body,
                         headers=data.headers)

def get_order(track):
    return requests.get(f"{config.URL_SERVICE}{config.GET_ORDER}{track}")