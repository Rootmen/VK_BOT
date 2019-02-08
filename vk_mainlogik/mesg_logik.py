import time

from vk import API, Session

from vk_mainlogik.vk_tokens import GetConfirmToken, GetToken


def SendMesgAll(data):
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return GetConfirmToken()
    elif data['type'] == 'message_new':
        session = Session()
        api = API(session, v=5.92)
        user_id = data['object']['user_id']
        api.messages.send(access_token=GetToken(), user_id=str(user_id), message="Хай")
