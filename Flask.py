from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/service')
def eiInfo():
    return '{__sys__: {}, __version__:2.0}'


if __name__ == '__main__':
    app.run()
