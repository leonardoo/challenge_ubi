import json
import unittest

from app import app, socketio


class TestApp(unittest.TestCase):

    def test_client_message(self):
        client = socketio.test_client(app)
        test_client = app.test_client()
        test_client.post('/points',
                         data=json.dumps({"client": "client-1", "count": 1}),
                         content_type='application/json')
        received = client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(len(received[0]["args"]), 1)
        self.assertEqual(received[0]["args"][0]["count"], 1)
        self.assertEqual(received[0]["args"][0]["client"], "client-1")
        client.disconnect()

    def test_client_message_end(self):
        client = socketio.test_client(app)
        test_client = app.test_client()
        test_client.post('/points',
                         data=json.dumps({"client": "client-1", "end": True}),
                         content_type='application/json')
        received = client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(len(received[0]["args"]), 1)
        self.assertEqual(received[0]["args"][0]["end"], True)
        self.assertEqual(received[0]["args"][0]["client"], "client-1")
        client.disconnect()

if __name__ == '__main__':
    unittest.main()
