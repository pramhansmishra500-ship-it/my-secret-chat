from flask import Flask, render_template
from flask_socketio import SocketIO, send

# 1. Flask App aur SocketIO ko initialize karein
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret_chat_key_123'  # Yeh secure key hai sessions ke liye
socketio = SocketIO(app, cors_allowed_origins="*")

# 2. Main Route - Jab koi website kholega to use chat page dikhega
@app.route('/')
def index():
    return render_template('index.html')

# 3. Message Handle - Jab koi user message bhejega, to ye code chalega
@socketio.on('message')
def handle_message(msg):
    print(f"Message received: {msg}")
    # Ye received message ko baki sabhi connected users ko bhej (broadcast) dega
    send(msg, broadcast=True)

# 4. Server ko run karein
if __name__ == '__main__':
    socketio.run(app, debug=True)
