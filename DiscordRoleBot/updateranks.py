#!/c/Users/SU/AppData/Local/Programs/Python/Python38/python
# THIS IS IN PYTHON 3!!!
# Path: ~/AppData/Local/Programs

import os
import discord
import sys
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print("SOME MESSAGE")
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

def readfile(filename):
    with open(filename) as f:
        return f.readline().replace("\n", "").replace("\r", "")

# async def main():
print("1")
location = os.path.join(os.path.dirname(__file__), ".discord.token")
print("2")
token = readfile(location)
sys.stdout.flush()
print("4")
client.run(token)
sys.stdout.flush()
channel = client.get_channel(681138135391797345)
# await channel.send('hello')
