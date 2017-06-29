#!/usr/bin/env python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
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

@app.route('/')
def index():
    return render_template('beauty.html', async_mode=socketio.async_mode)


@socketio.on('my_ping', namespace='/test')
def ping_pong():
    with open('test.log', 'r') as f:
        log_content = f.read()
    emit('my_pong', log_content, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)