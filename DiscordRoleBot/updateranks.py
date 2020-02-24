#!/c/Users/SU/AppData/Local/Programs/Python/Python38/python
# THIS IS IN PYTHON 3!!!
# Path: ~/AppData/Local/Programs

import traceback
import os
import discord
import sys
import asyncio
import json

client = discord.Client(fetch_offline_members = True)

@client.event
async def on_ready():
    debug('We have logged in as {0.user}'.format(client))


def role_exists(guild, role):
    for r in guild.roles:
        if str(r) == role:
            return True
    return False


def read_roles_json():
    with open('./roles.json') as jsonfile:
        debug("reading file inner aaa")
        data = json.load(jsonfile)
        # debug(data['roles'])
        # debug(data['users'])
        # sys.stdout.flush()
        return data


def debug(s):
    print(s)
    sys.stdout.flush()


def getMemberByName(name):
    return discord.utils.get(message.guild.members, name=name)


# @client.event
async def sync_roles(message):
    try:
        debug("A")
        await message.channel.send('Starting!')
        debug("B")
        data = read_roles_json()
        # debug("num members:" + str(len(client.users)))
        # member = discord.utils.get(message.guild.members, name='AmaliRae')
        # for guildMember in
        # debug("We got a member!" + str(member))
        for role in data['roles']:
            debug("role in json exists? " + str(role_exists(message.guild, role['name'])))
            if not role_exists(message.guild, role['name']):
                await message.guild.add_roles(name=role['name'], hoist=True, mentionable=False)
        for user in data['users']:
            debug("user in streamlabs:" + user)
            member = discord.utils.get(message.guild.members, name=user)
            debug("user in discord:" + str(member))
        #     await message.guild.assign_role(name=role['name'], hoist=True, mentionable=False)
        await message.channel.send('Done!')
    except Exception as e:
        debug("Unexpected error:", traceback.format_exc())
        sys.stdout.flush()


@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            # ignore message by ourself!
            return
        if message.content.startswith('!s'):
            debug("I am ready")
            await sync_roles(message)
    except Exception as e:
        debug("Unexpected error:", traceback.format_exc())
        sys.stdout.flush()


def readfile(filename):
    with open(filename) as f:
        return f.readline().replace("\n", "").replace("\r", "")


location = os.path.join(os.path.dirname(__file__), ".discord.token")
token = readfile(location)
client.run(token)
sys.stdout.flush()
