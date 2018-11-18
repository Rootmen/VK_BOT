import os
import random

import requests
import vk
from docxtpl import DocxTemplate
from flask import Flask, request, json
from database.modelsdatabase import User
from static_data import *


def NewPostVkCallBack(requestMy):
    try:
        data = json.loads(requestMy)
        # Вконтакте в своих запросах всегда отправляет поле типа
        if 'type' not in data.keys():
            return
        if data['type'] == 'confirmation':
            return confirmation_token
        elif data['type'] == 'message_new':
            session = vk.Session(access_token=token)
            api = vk.API(session, v=5.8)
            user_id = data['object']['from_id']
            text = data['object']['text']
            text = str(text).split(" ", 7)
            # Установка рандомного числа
            random.seed()
            # Загрузка шаблона
            doc = DocxTemplate("template.docx")
            # Загрузка параметров
            context = {'surname': text[0],
                       'name': text[1],
                       'lastname': text[2],
                       'gender': text[3],
                       'number': text[4],
                       'group': text[5],
                       'type': text[6]}
        doc.render(context)
        # Создание документа
        LogFile = True
        NameFail = os.path.abspath("temp" + str(random.randint(1, 10000)) + ".docx")
        doc.save(NameFail)
        excel_file_name = NameFail

        upload_url = api.docs.getMessagesUploadServer(type='doc', peer_id=user_id)['upload_url']
        response = requests.post(upload_url, files={'file': open(excel_file_name, 'rb')})
        result = json.loads(response.text)
        file = result['file']

        jsonmy = api.docs.save(file=file, title='Заявление на Мат.Пом.', tags=[])[0]

        owner_id = jsonmy['owner_id']
        photo_id = jsonmy['id']
        api.messages.send(attachment='doc' + str(owner_id) + '_' + str(photo_id), access_token=token,
                          user_id=str(user_id), message='Вот твое заявление!',
                          )
        # Сообщение о том, что обработка прошла успешно
        os.remove(excel_file_name)
        return 'ok'
    except Exception as All:
        session = vk.Session(
            access_token=token)
        api = vk.API(session, v=5.8)
        user_id = data['object']['from_id']
        api.messages.send(access_token=token, user_id=str(user_id),
                          message='Увы я пока не могу тебя понять, '
                                  'Напиши мне свои данные в формате'
                                  '1)Фамилия Имя Отчество в родительском падеже'
                                  '2)Твой пол, парень ты или девушка'
                                  '3)Твой номер телефона в формате 8ХХХХХХХХХ'
                                  '4)Группу в которой ты учишься'
                                  ' заявление')


def SearhToDb(user_id):
    u = User.query.get(user_id)
    if u is not None:
        return u
