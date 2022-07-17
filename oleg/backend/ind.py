from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Index!"


@app.route('/rickroll/')
def rickroll():
    return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


@app.route('/user_id/<string:user>/<int:i_d>/')
def user_id(user, i_d):
    return "Hello, " + user + " - " + str(i_d)


if __name__ == '__main__':
    app.run(host='0.0.0.0')