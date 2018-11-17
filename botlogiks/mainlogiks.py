import os
import random

import requests
import vk
from docxtpl import DocxTemplate
from flask import Flask, request, json
from database.modelsdatabase import User
from static_data import *


def NewPostVkCallBack(requestMy):
    data = json.loads(requestMy)
    # Вконтакте в своих запросах всегда отправляет поле типа
    if 'type' not in data.keys():
        return
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        session = vk.Session()
        api = vk.API(session, v=5.8)
        user_id = data['object']['from_id']
        text = data['object']['text']
        text = str(text).split(" ")
        # Установка рандомного числа
        random.seed()
        # Загрузка шаблона
        doc = DocxTemplate("template.docx")
        # Загрузка параметров
        context = { 'fastname':text[0],
                    'lastname':text[1],
                    'surename':text[2],
                    'gender'  :text[3],
                    'number'  :text[4],
                    'type'    :text[5]}
        doc.render(context)
        # Создание документа
        LogFile = True
        NameFail = ""
        while LogFile:
            try:
                NameFail = "temp" + str(random.randint(1, 10000)) + ".docx"
                file = open(NameFail)
                file.close()
            except IOError as e:
                break
        doc.save(NameFail)
        excel_file_name  = os.path.abspath(NameFail)
        upload_url = api.docs.getMessagesUploadServer(type='doc', peer_id=user_id)['upload_url']
        response = requests.post(upload_url, files={'file': open(NameFail, 'rb')})
        result = json.loads(response.text)
        file = result['file']

        jsonmy = api.save(file=file, title='Документ', tags=[])[0]

        owner_id = jsonmy['owner_id']
        photo_id = jsonmy['id']
        api.messages.send(access_token=token, user_id=str(user_id), message='Вот твое заявление!')
        # Сообщение о том, что обработка прошла успешно
        os.remove(excel_file_name)
        return


def SearhToDb(user_id):
    u = User.query.get(user_id)
    if u is not None:
        return u


