#!/usr/bin/env python
import json
from time import sleep
from flask import Flask, render_template, session, request, Response, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from flask_bootstrap import Bootstrap
from gevent import monkey;monkey.patch_all()
# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
bootstrap = Bootstrap(app)
thread = None


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/test')


@app.route('/stream')
def stream():
    def generate():
        with open('test.log', 'r') as f:
            while True:
                yield f.read()
                sleep(1)

    return Response(generate(), mimetype='text/plain')


@app.route('/')
def index():
    with open('test.log', 'r') as f:
        log_content = json.dumps(f.read())
    return render_template('index.html', async_mode=socketio.async_mode, log_content=log_content, mimetype='text/plain')


@socketio.on('my_ping', namespace='/test')
def ping_pong():
    # data = {'fuck': 'fuck'}
    with open('test.log', 'r') as f:
        log_content = f.read()
    emit('my_pong', log_content, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)