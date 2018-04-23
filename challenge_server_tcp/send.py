import socket
import random
import time
import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 27877
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
try:
    while True:
        for i in range(5):
            print(datetime.datetime.now())
            count = random.randint(0, 20)
            msg = str(count)
            s.send(str.encode(msg))
            sl = float(random.randint(50, 200)) / 1000
            time.sleep(sl)
            print(datetime.datetime.now())
            print(msg, "mesage", sl, "sleep")
        #time.sleep(0.5)

except socket.timeout:
    s.close()
else:
    s.close()

#print "received data:", data
