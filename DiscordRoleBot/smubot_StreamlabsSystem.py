# THIS IS IN PYTHON 2!!!

import json
import os
import os.path
from datetime import datetime
import threading

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
    onTimer()

class FakeData:
	"This is my second class"
	def IsFromDiscord(self):
		return True


def onTimer():
    data = FakeData()
    SendBack(data, "I am a timer!")
    OnWriteCommand(data)
    thread = threading.Timer(5 * 60.0, onTimer)
    thread.daemon = True
    thread.start()

def moveFile(existingFilename, newFilename):
    os.rename(existingFilename, newFilename)

def writeJsonToFile(jsonBlob, filename):
    with open(filename, 'w') as outfile:
        outfile.write(json.dumps(jsonBlob, indent=4))

def readJsonFromFileIfExists(filename):
    with open(filename) as jsonfile:
        data = json.load(jsonfile)
        return data

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

def OnWriteCommand(data):
    outputMessage = ""
    # userId = data.User
    # username = data.UserName
    # points = Parent.GetPoints(userId)

    filename = dir_path + "\\" + "roles.json"
    existingData = readJsonFromFileIfExists(filename)
    viewerRanksMap = {}
    rolesMap = {}
    for role in existingData['roles']:
        rank = role['name']
        rolesMap[rank] = {"name": rank}
    for name in existingData['users']:
        rank = existingData['users'][name]
        viewerRanksMap[name] = rank

    # viewers = Parent.GetActiveUsers() # TODO These are only the ACTIVE viewers! maybe get all viewers?
    viewers = Parent.GetViewerList()
    for name in viewers:
        rank = Parent.GetRank(name)
        viewerRanksMap[name] = rank
        rolesMap[rank] = {"name": rank}
    fileData = {}
    fileData['users'] = viewerRanksMap
    fileData['roles'] = RolesMapToArray(rolesMap)
    # SendBack(data, "ranks: " + str(viewerRanksMap.values()))
    # SendBack(data, dir_path)

    now = datetime.now()
    newFilename = filename + now.strftime("%m_%d_%Y__%H_%M_%S") + ".json"
    if os.path.isfile(filename):
        moveFile(filename, newFilename)

    writeJsonToFile(fileData, filename)
    SendBack(data, "Done writing file!")
    SendBack(data, "!s")


def HandleChat(data):
    if (data.IsFromDiscord() or data.IsChatMessage()) and data.GetParam(0).lower() == settings["command"] and Parent.HasPermission(data.User, settings["permission"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
        OnWriteCommand(data)

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
