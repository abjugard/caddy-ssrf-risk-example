import os, requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', greeting=f"Hello {request.remote_addr}, let's send some webhooks!")


def send_webhook(target, method, content):
    return requests.request(method, target, data=content, headers={'content-type': 'application/json'})


@app.route('/', methods=['POST'])
def post():
    try:
        response = send_webhook(**request.form)
    except Exception as e:
        raise e
    return render_template('index.html', greeting=f"Nicely done {request.remote_addr}, send another?", result=response)


@app.route('/env')
def debug():
    if 'X-Forwarded-For' in request.headers:
        return render_template('illegal.html', msg=f"Sorry, this page is not accessible from {request.headers['X-Forwarded-For']}"), 400
    if 'X-Webhook-Admin' not in request.headers:
        return render_template('illegal.html', msg=f"Sorry, no access without the X-Webhook-Admin header set!"), 400
    env = [f'{name}: {value}\n' for name, value in os.environ.items()]
    return render_template('env.html', env=env)
