import asyncio
import json
import discord
import discord as discord
import datetime
import time
import websockets

Token = "Discord_token_here"
client = discord.Client()


async def embedMessage(msg, message):

    await client.edit_message(message, new_content=str(msg))


class RCON:

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


@client.event
async def on_ready():
    #BackendAPI.Load()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    channel = message.channel
    if message.content == "?RconHere" :
        #print(''.join(message.author.roles[1].name.lower()))

        for role in message.author.roles:

            if role.name == "Admin":
                #print("Success")
                await client.send_message(channel, "RCON")




    if(message.author == client.user):
        conn = RCON("IP", "PORT", "RCON_PW", channel, message)

        await conn.on_conn()
        await conn.on_recv()




client.run(Token)
