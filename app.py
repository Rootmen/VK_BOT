from botlogiks.mainlogiks import NewPostVkCallBack
from flask import Flask, request
from database.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/vk_call', methods=['POST'])
def processing():
    return NewPostVkCallBack(request.data)


@app.route('/', methods=['GET'])
def processing2():
    return 'Здесь пока ничего нету'


if __name__ == '__main__':
    app.run()
