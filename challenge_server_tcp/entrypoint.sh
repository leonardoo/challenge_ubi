#!/bin/sh

python challenge_server_tcp.py &
python register_server.py &
python app.py