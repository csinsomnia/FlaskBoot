# coding=utf-8
from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap

# app = Flask(__name__, static_url_path='/static')
# Bootstrap(app)

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app

app = create_app()

# 指明静态文件名
@app.route('/')
def index():
    return app.send_static_file('index.html')

# 带参数的文件 使用send_from_directory 防止其他的静态资源被随意读取??
@app.route('/v2/<path:path>')
def v2path(path):
    return send_from_directory('static', path)


@app.route('/tpl')
def tpl():
    return render_template("item.html")

@app.route('/service')
def eiInfo():
    return '{__sys__: {}, __version__:2.0}'

@app.route('/message')
def hello_world():
    return 'Flask 发车'


if __name__ == '__main__':
    app.run()
