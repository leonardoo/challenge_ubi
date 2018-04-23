import asyncio
import threading
import json
import socket


class ServerTcp(asyncio.Protocol):

    lock = threading.Lock()
    count = 0
    delay_send = False
    t = None

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data, *args, **kwargs):
        message = data.decode()
        try:
            number = int(message)
            if 0 <= number <= 20:
                with self.lock:
                    self.count += number
                    if not self.delay_send:
                        self.delay_send = True

                        self.t = threading.Timer(1, self.send_sum)
                        self.t.start()
            else:
                self.transport.close()
        except Exception:
            self.transport.close()

    def send_sum(self):
        with self.lock:
            # print(datetime.datetime.now(), "send_sum", self.count)
            self.delay_send = False
            peername = self.transport.get_extra_info('peername')
            msg = json.dumps({"client": "{}".format(peername), "count": self.count})
            self.count = 0
            self.send_tcp_msg(msg)

    def send_tcp_msg(self, msg):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("127.0.0.1", 27878))
            s.send(str.encode(msg))
        except Exception:
            pass

    def eof_received(self):
        peername = self.transport.get_extra_info('peername')
        msg = json.dumps({"client": "{}".format(peername), "end": True})
        self.send_tcp_msg(msg)


loop = asyncio.get_event_loop()
# Each client connection will create a new protocol instance
coro = loop.create_server(ServerTcp, '0.0.0.0', 27877)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
