from fastapi import FastAPI, Response, status
from .models import InputModel, ConvertModel
import requests
from os import getenv

app = FastAPI()

@app.get('/')
def home():
    return {"Hello world"}

@app.post('/input/')
async def input(input: InputModel, response: Response):
    converted = ConvertModel(input)

    if converted is not None:
        response.status_code = status.HTTP_200_OK
        callAPI(converted, 'hello', 'world')
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return


def callAPI(data, param1, param2):
    url = "https://example.com/api?value1={0}&value2={1}".format(param1, param2)
    headers = {
        "Content-Type": "application/json",
        "Authorization": getenv("token", "")
    }
    response = requests.get(url, json=data, headers=headers)