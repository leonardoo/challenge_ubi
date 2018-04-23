import asyncio
import json
import requests


class ServerReceiver(asyncio.Protocol):

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data, *args, **kwargs):
        message = data.decode()
        try:
            data = json.loads(message)
            requests.post("http://localhost:5000/points", json=data, timeout=3)
        except Exception:
            pass
        self.transport.close()

    def eof_received(self):
        print("end")

loop = asyncio.get_event_loop()
# Each client connection will create a new protocol instance
coro = loop.create_server(ServerReceiver, '0.0.0.0', 27878)
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
