from flask import Flask, request, json, render_template, redirect
from vk_mainlogik.mesg_logik import treadControl, sendMesgAll

app = Flask(__name__)


# treadControl()


@app.route('/')
def any_page():
    return redirect("/auth", code=302)


@app.route('/auth')
def auth():
    return render_template("auth.html", is_valid_pass="True")


@app.route('/index')
def index():
    return render_template("admin-panel.html")


@app.route('/upload', methods=['GET'])
def upload():
    if request.method == "GET":
        username = request.args.get('username')
        password = request.args.get('password')

        if username == 'admin' and password == 'admin':
            return redirect("/index", code=302)
        else:
            return render_template("auth.html", is_valid_pass=False)


# @app.route('/', methods=['POST'])
# def processing():
#     return sendMesgAll(json.loads(request.data))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
