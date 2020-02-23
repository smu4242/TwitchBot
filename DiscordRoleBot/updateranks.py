#!/c/Users/SU/AppData/Local/Programs/Python/Python38/python
# THIS IS IN PYTHON 3!!!
# Path: ~/AppData/Local/Programs

import traceback
import os
import discord
import sys
import asyncio
import json

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


def role_exists(guild, role):
    for r in guild.roles:
        if str(r) == role:
            return True
    return False


def read_roles_json():
    with open('./roles.json') as jsonfile:
        print("reading file inner")
        data = json.load(jsonfile)
        print(data['roles'])
        sys.stdout.flush()
        return data


@client.event
async def sync_roles(message):
    await message.channel.send('Starting!')
    data = read_roles_json()
    for role in data['roles']:
        print("role in json exists? " + str(role_exists(message.guild, role['name'])))
        if not role_exists(message.guild, role['name']):
            await message.guild.create_role(name=role['name'], hoist=True, mentionable=False)
    await message.channel.send('Done!')


@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            # ignore message by ourself!
            return
        if message.content.startswith('!s'):
            await sync_roles(message)
    except Exception as e:
        print("Unexpected error:", traceback.format_exc())
        sys.stdout.flush()


def readfile(filename):
    with open(filename) as f:
        return f.readline().replace("\n", "").replace("\r", "")


location = os.path.join(os.path.dirname(__file__), ".discord.token")
token = readfile(location)
with open('./roles.json') as jsonfile:
    print("reading file")
    print(json.load(jsonfile))
    sys.stdout.flush()
client.run(token)
sys.stdout.flush()
