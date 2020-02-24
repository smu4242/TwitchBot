# THIS IS IN PYTHON 2!!!

import json
import os

ScriptName = "DiscordRoleBot"
Website = "http://www.example.com/todo"
Description = "Read roles from Streamlabs Chatbot and put them into discord."
Creator = "smu4242"
Version = "0.0.0"

configFile = "config.json"
settings = {}

def ScriptToggled(state):
    return

def Init():
    global settings

    settings = {
        "liveOnly": False,
        "command": "!sync",
        "permission": "Mod"
    }


def SendBack(data, message):
    if data.IsFromDiscord():
        Parent.SendDiscordMessage(message)
    else:
        Parent.SendStreamMessage(message)

def HandleChat(data):
    # SendBack(data, "DEBUG: " + str(data.User))
    if data.IsChatMessage() and data.GetParam(0).lower() == settings["command"] and Parent.HasPermission(data.User, settings["permission"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
        outputMessage = ""
        userId = data.User
        username = data.UserName
        points = Parent.GetPoints(userId)

        viewers = Parent.GetActiveUsers() # TODO These are only the ACTIVE viewers! maybe get all viewers?
        viewerRanksMap = {}
        for name in viewers:
            viewerRanksMap[name] = Parent.GetRank(name)
        SendBack(data, "ranks: " + str(viewerRanksMap.values()))

        # SendBack(data, outputMessage)

def Execute(data):
    if data.IsChatMessage():
        return HandleChat(data);
    return

def ReloadSettings(jsonData):
    Init()
    return

def OpenReadMe():
    location = os.path.join(os.path.dirname(__file__), "README.txt")
    os.startfile(location)
    return

def Tick():
    return
