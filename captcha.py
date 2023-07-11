import base64
from time import sleep
import cv2
import requests
from PIL import Image
 


def solve_captcha(uri):
    gif_file_path = uri

    with open(gif_file_path, 'rb') as file:
        imgcontent = file.read()
        
    data = {
        "clientKey": "438230e974574a76828d65b4efbe4493",
        "task": {
            "type": "ImageToTextTask",
            "body": base64.b64encode(imgcontent).decode("utf-8")
        }
    }
    get_id = requests.post('https://api.anycaptcha.com/createTask', json=data, headers={'Host': 'api.anycaptcha.com', 'Content-Type': 'application/json'}).json()
    taskId = get_id.get('taskId')
    payload = {
        'clientKey': '438230e974574a76828d65b4efbe4493',
        'taskId': taskId
    }
    while True:
        sleep(0.5)
        response = requests.post('https://api.anycaptcha.com/getTaskResult', json=payload,
                                 headers={'Host': 'api.anycaptcha.com', 'Content-Type': 'application/json'}).json()
        if response.get('status') == 'processing':
            pass
        elif response.get('status') == 'ERROR_CAPTCHA_UNSOLVABLE':
            break
        else:
            return response.get('solution').get('text')
