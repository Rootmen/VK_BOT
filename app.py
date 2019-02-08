from flask import Flask, request, json
from vk_mainlogik.mesg_logik import SendMesgAll
app = Flask(__name__)


@app.route('/vk_call', methods=['POST'])
def processing():
    return SendMesgAll(json.loads(request.data))


if __name__ == '__main__':
    app.run()
