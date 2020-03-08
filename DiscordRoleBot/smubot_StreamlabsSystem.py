# THIS IS IN PYTHON 2!!!

import json
import os
import os.path
from datetime import datetime


ScriptName = "DiscordRoleBot"
Website = "http://www.example.com/todo"
Description = "Read roles from Streamlabs Chatbot and put them into discord."
Creator = "smu4242"
Version = "0.0.0"

configFile = "config.json"
settings = {}

dir_path = os.path.dirname(os.path.realpath(__file__))

def ScriptToggled(state):
    return

def Init():
    global settings

    settings = {
        "liveOnly": False,
        "command": "!write",
        "permission": "Mod"
    }


def moveFile(existingFilename, newFilename):
    os.rename(existingFilename, newFilename)

def writeJsonToFile(jsonBlob, filename):
    with open(filename, 'w') as outfile:
        outfile.write(json.dumps(jsonBlob, indent=4))


def SendBack(data, message):
    if data.IsFromDiscord():
        Parent.SendDiscordMessage(message)
    else:
        Parent.SendStreamMessage(message)


def RolesMapToArray(rolesMap):
    list = []
    for key, value in rolesMap.iteritems():
        list.append(value)
    return list


def HandleChat(data):
    # SendBack(data, "DEBUG: " + str(data.User))
    if (data.IsFromDiscord() or data.IsChatMessage()) and data.GetParam(0).lower() == settings["command"] and Parent.HasPermission(data.User, settings["permission"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
        outputMessage = ""
        userId = data.User
        username = data.UserName
        points = Parent.GetPoints(userId)

        # viewers = Parent.GetActiveUsers() # TODO These are only the ACTIVE viewers! maybe get all viewers?
        viewers = Parent.GetViewerList()
        viewerRanksMap = {}
        rolesMap = {}
        for name in viewers:
            rank = Parent.GetRank(name)
            viewerRanksMap[name] = rank
            rolesMap[rank] = {"name": rank}
        fileData = {}
        fileData['users'] = viewerRanksMap
        fileData['roles'] = RolesMapToArray(rolesMap)
        # SendBack(data, "ranks: " + str(viewerRanksMap.values()))
        # SendBack(data, dir_path)

        filename = dir_path + "\\" + "roles.json"
        now = datetime.now()
        newFilename = filename + now.strftime("%m_%d_%Y__%H_%M_%S") + ".json"
        SendBack(data, "trying to move file: " + filename + " -> " + newFilename + " was there: " + str(os.path.isfile(filename)))
        if os.path.isfile(filename):
            moveFile(filename, newFilename)

        writeJsonToFile(fileData, filename)
        # SendBack(data, outputMessage)

def Execute(data):
    if data.IsChatMessage() or data.IsFromDiscord():
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
