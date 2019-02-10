from flask import Flask, request, json
from vk_mainlogik.mesg_logik import treadControl, sendMesgAll

app = Flask(__name__)
treadControl()


@app.route('/', methods=['POST'])
def processing():
    return sendMesgAll(json.loads(request.data))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
