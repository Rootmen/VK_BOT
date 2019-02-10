import datetime
import threading

import vk
from vk import API, Session

from db_time.db_control import getThisDayTable
from vk_mainlogik.vk_tokens import ConfirmToken, GetToken
from db_recipients.db_recipentscontrol import addRecipient, startRecipientCall


def sendMesgAll(data):
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return ConfirmToken
    elif data['type'] == 'message_new':
        controlMeseg(data)
    return "ok"


def controlMeseg(data):
    user_id = data['object']['user_id']
    user_id = str(user_id)
    message = data['object']['body'].lower()
    if message == "/connect":
        addRecipient(user_id)


def sendMesg(user_id, mass):
    time_to_go, roll = mass
    session = vk.Session()
    api = vk.API(session, v=5.8)
    message = "Через " + time_to_go + " минут в аудитории " + roll[2] + " будет " + roll[0] + " с преподователем " + \
              roll[1]
    api.messages.send(access_token=GetToken, user_id=str(user_id), message=message)


def sendMesgText(user_id, text):
    session = vk.Session()
    api = vk.API(session, v=5.8)
    api.messages.send(access_token=GetToken, user_id=str(user_id), message=str(text))


def treadControl():
    this_day_mass = getThisDayTable()
    this_time = datetime.datetime.now()
    this_time = this_time.hour * 60 + this_time.minute
    if this_day_mass is []:
        threading.Timer(60 * 60 * 24, treadControl).start()
        sendMesgText("200152858", 60 * 24)
        return
    for roll in this_day_mass:
        time_start = roll[3] * 60 + roll[4]
        time_to_go = time_start - this_time
        if 0 < time_to_go < 15:
            startRecipientCall(sendMesg, (time_to_go, roll))
            threading.Timer(80 * 60, treadControl).start()
            sendMesgText("200152858", 80)
            return
        if time_to_go > 30:
            threading.Timer((time_to_go - 10) * 60, treadControl).start()
            sendMesgText("200152858", (time_to_go - 10))
            return
    threading.Timer((24 * 60 - time_to_go) * 60, treadControl).start()
    sendMesgText("200152858", (24 * 60 - time_to_go))
    return
