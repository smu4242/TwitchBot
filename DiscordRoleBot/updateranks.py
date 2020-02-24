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


def getRoleByName(guild, roleName):
    for r in guild.roles:
        if str(r) == roleName:
            return r
    return None


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


def compareName(m):
    debug("comparing: " + m.nick)
    return m.name.lower() == name.lower() or m.nick.lower() == name.lower()

def getMemberByName(guild, name):
    # return discord.utils.get(message.guild.members, name=name)
    return discord.utils.find(lambda m: (m.name.lower() == name.lower()) or (m.nick and (m.nick.lower() == name.lower())), guild.members)

# @client.event
async def sync_roles(message):
    try:
        await message.channel.send('Starting!')
        data = read_roles_json()
        # member = getMemberByName(message.guild, 'amalIraE')
        # debug("We got a member!" + str(member))
        discordRoles = {}
        for role in data['roles']:
            debug("role in json exists? " + str(role_exists(message.guild, role['name'])))
            roleName = role['name']
            discordRole = getRoleByName(message.guild, roleName)
            if not discordRole:
                await message.guild.add_roles(name=role['name'], hoist=True, mentionable=False)
            discordRoles[roleName] = discordRole
        for user in data['users']:
            roleName = data['users'][user]
            debug("user in streamlabs:" + user)
            discordMember = getMemberByName(message.guild, user)
            if discordMember:
                discordRole = discordRoles[roleName]
                debug("user in discord:" + str(discordMember) + " will get role " + str(discordRole))
                await discordMember.add_roles(discordRole, reason="update ranks script 1")
                debug("A")
            debug("B")
        debug("C")
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
