from flask import Flask, render_template, request
from flask_socketio import SocketIO
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/points', methods=['POST'])
def points():
    content = request.json
    data = {'client': content['client']}
    if "count" in content:
        data["count"] = content["count"]
    if "end" in content:
        data["end"] = content["end"]
    print(data)
    socketio.emit('update_client', data)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app, debug=True)
