import datetime
import os
import time

import requests
from config import Token


def send_message_to(chat_id: int, text: str, title: str = None):
    link = f'https://eitaayar.ir/api/{Token}/sendMessage'
    res = requests.post(url=link, data={'chat_id': chat_id, 'text': text, 'title': title})

    print(res.text)


def send_file_to(chat_id: int, file_name, caption: str = None):
    link = f'https://eitaayar.ir/api/{Token}/sendFile'
    file = open(f'downloads/{file_name}', 'rb')
    files = {'file': file}
    data = {'chat_id': chat_id, 'caption': caption}
    res = requests.post(url=link, files=files, data=data)
    print(res.text)

def send_by_binary_to(chat_id:int,data_bit,caption:str = None):
        link = f'https://eitaayar.ir/api/{Token}/sendFile'
        files = {'file': data_bit}
        data = {'chat_id': chat_id, 'caption': caption}
        res = requests.post(url=link, files=files, data=data)
        print(res.text)


#
# send_message_to(chat_id=8169026, text='hi every body')
#send_file_to(chat_id=8169026, file_name='downloads/kart meli.pdf')
