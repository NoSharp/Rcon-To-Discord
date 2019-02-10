import asyncio
import datetime
import json
import time
import websockets


class Rcon:
    def __init__(self, ip, port, password, channel, message):
        self._ip = ip
        self._port = port
        self._pw = password
        self._url = "ws://" + self._ip + ":" + self._port + "/" + self._pw
        self.websocket = None
        self.channel = channel
        self.messages = []
        self.message = message

    async def on_conn(self):
        self.websocket = await websockets.connect(
            self._url)
        print("Connected")

    async def on_recv(self):

        name = await self.websocket.recv()
        json_name = json.loads(name)

        if(json_name["Identifier"] == -1):
            await asyncio.sleep(0.1)

            await self.on_recv()

        self.messages.append("<" + datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S') + "> " + json_name["Message"] + "\n")
        await embedMessage("```" + ''.join(self.messages) + "```", self.message)
        await asyncio.sleep(0.1)

        await self.on_recv()




