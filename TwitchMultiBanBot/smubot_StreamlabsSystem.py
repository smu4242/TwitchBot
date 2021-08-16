import clr
import sys
import json
import os
import time

ScriptName = "Multiban"
Website = "http://www.example.com/todo"
Description = "Bans multiple accounts, e.g. all users that raided in the last 3 minutes"
Creator = "smu4242"
Version = "0.0.2"

configFile = "config.json"
settings = {}

nothing = lambda x,y: ""

raidData = {}


def ScriptToggled(state):
    return

def Init():
    global settings

    settings = {
        "liveOnly": False,
        "command": "!multiban",
        "permission": "Mod"
    }

def SendBack(data, message):
    if data.IsFromDiscord():
        Parent.SendDiscordMessage(message)
    else:
        Parent.SendStreamMessage(message)

def Log(msg):
    Parent.Log("TwitchMultiBan", str(msg))

def getAllRaidsSince(durationMinutes):
    global raidData
    timeCutOff = time.time() - (durationMinutes*60)
    result = []
    for userName, raidTimeOfUser in raidData.items():
        if raidTimeOfUser > timeCutOff:
            result.append(userName)
    return result

def HandleRaw(data):
    global raidData
    array = data.RawData.split(";")
    user = ""
    isRaid = False
    for val in array:
        inner = val.split("=")
        if inner[0] == "msg-id" and inner[1] == "raid":
            Log("Found a raid: " + inner[0] + "=" + inner[1])
            isRaid = True
        elif inner[0] == "login":
            Log("found the name: " + inner[1])
            user = inner[1]
    if isRaid:
        raidData[user] = time.time()
        Log("Result: " + json.dumps(raidData, indent = 2))

def HandleChat(data):
    if not (data.IsChatMessage() and data.GetParam(0).lower() == settings["command"] and Parent.HasPermission(data.User, settings["permission"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"]))):
        #SendBack(data, "Not reacting to this")
        return

    reallyBan = False
    if data.GetParam(2).lower() == "ban":
        reallyBan = True

    durationStr = data.GetParam(1)
    try:
        durationMinutes = int(durationStr)
    except Exception, e:
        SendBack(data, "Sorry, I didn't get that. Try !multiban 3")

    outputMessage = ""
    userId = data.User
    username = data.UserName

    allRaids = getAllRaidsSince(durationMinutes)

    allMessages = []
    for userName in allRaids:
        if reallyBan:
            SendBack(data, "/ban " + userName)
        else:
            allMessages.append("preparing to ban " + userName)

    if not reallyBan:
        SendBack(data, "Would ban " + str(len(allRaids)) + " users that raided recently.")
        SendBack(data, "Run the same command with added 'BAN' at the end to actually ban them all.")
    else:
        SendBack(data, "I banned " + str(len(allRaids)) + " users that raided recently. Please double check that this was correct!")

    Log(allMessages)


def Execute(data):
    if data.IsChatMessage():
        return HandleChat(data);
    elif data.IsRawData():
        # raids happen here
        return HandleRaw(data)

def ReloadSettings(jsonData):
    Init()
    return

def OpenReadMe():
    location = os.path.join(os.path.dirname(__file__), "README.txt")
    os.startfile(location)
    return

def Tick():
    return
