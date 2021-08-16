# import clr
# import sys
import json
import os
# import ctypes
# import codecs

ScriptName = "Calculator"
Website = "http://www.example.com/todo"
Description = "Calculator for different units (Celcius, Fahrenheit, kg, lbs, mi, km, inches & cm)"
Creator = "smu4242"
Version = "0.0.5"

configFile = "config.json"
settings = {}

nothing = lambda x,y: ""

def calcSassyMessage(celcius):
    if not settings["showSassyMessage"]:
        return "";
    if celcius > 1200:
        return "That is as literally HOTTER THAN LAVA! I doubt your thermometer showed that number!"
    if celcius > 700:
        return "That is as hot as lava! Run away!"
    if celcius > 100:
        return "That is LITERALLY boiling!"
    if celcius > 50:
        return "That is boiling hot!"
    if celcius > 40:
        return "Too hot! Get into the fridge!"
    if celcius > 30:
        return "smu has trouble sleeping at this temperature!"
    if celcius > 25:
        return "That is pretty warm!"
    if celcius > 20:
        return "smu approves of this temperature"
    if celcius > 18:
        return "That is not too bad"
    if celcius > 14:
        return "Eh, kinda cold"
    if celcius > 0:
        return "Too cold, man!"
    if celcius > -10:
        return "That is LITERALLY freezing! Make a fire!"
    if celcius > -20:
        return "That is really fricking cold! Make two fires!"
    if celcius > -40:
        return "This is in the Frostpunk range. Move to the equator dude!"
    if celcius > -60:
        return "Boiling water will freeze instantly. Seriously, move closer to the equator!"
    if celcius > -273.15:
        return "I doubt your thermometer showed that number!"
    if celcius <= -273.15:
        return "Liar, liar pants on fire! This temperature does not even exist in this universe! NotLikeThis"

kgToLbFactor = 2.20462
def kgToLb(kg):
    return round(kg * kgToLbFactor, 2)
def lbToKg(lb):
    return round(lb / kgToLbFactor, 2)

def CtoF(celcius):
    return round((celcius * 1.8) + 32, 1)
def FtoC(fahrenheit):
    return round((fahrenheit - 32) / 1.8, 1)

cmToInchFactor = 0.393701
def cmToInch(cm):
    return round(cm * cmToInchFactor, 1)
def inchToCm(inch):
    return round(inch / cmToInchFactor, 1)

miToKmFactor = 1.6093
def miToKm(mi):
    return round(mi * miToKmFactor, 1)
def kmToMi(km):
    return round(km / miToKmFactor, 1)

converterMap = {
    "c": {
        'sourceUnit': u"\u00B0C",
        'targetUnit': u"\u00B0F",
        'transformFun': CtoF,
        'fuzzyFun': lambda x,y: calcSassyMessage(x)
    },
    "f": {
        'sourceUnit': u"\u00B0F",
        'targetUnit': u"\u00B0C",
        'transformFun': FtoC,
        'fuzzyFun': lambda x,y: calcSassyMessage(y)
    },
    "cm": {
        'sourceUnit': "cm",
        'targetUnit': "in",
        'transformFun': cmToInch,
        'fuzzyFun': nothing
    },
    "km": {
        'sourceUnit': "km",
        'targetUnit': "mi",
        'transformFun': kmToMi,
        'fuzzyFun': nothing
    },
    "mi": {
        'sourceUnit': "mi",
        'targetUnit': "km",
        'transformFun': miToKm,
        'fuzzyFun': nothing
    },
    "in": {
        'sourceUnit': "in",
        'targetUnit': "cm",
        'transformFun': inchToCm,
        'fuzzyFun': nothing
    },
    "kg": {
        'sourceUnit': "kg",
        'targetUnit': "lb",
        'transformFun': kgToLb,
        'fuzzyFun': nothing
    },
    "lb": {
        'sourceUnit': "lbs",
        'targetUnit': "kg",
        'transformFun': lbToKg,
        'fuzzyFun': nothing
    }
}
# aliases:
converterMap["lbs"] = converterMap["lb"]
converterMap["''"] = converterMap["in"]

def findConverter(inputStr):
    for key in converterMap:
        keyLength = len(key)
        value = converterMap[key]
        if inputStr[-keyLength:] == key:
            sourceValue = float(inputStr[:-keyLength])
            return value, sourceValue
    return None, None

def ScriptToggled(state):
    return

def Init():
    global settings

    settings = {
        "liveOnly": False,
        "command": "!convert",
        "permission": "Everyone",
        "costs": 1,
        "useCooldown": True,
        "useCooldownMessages": True,
        "showSassyMessage": True,
        "cooldown": 1,
        "userCooldown": 1,
        "onCooldown": "$user, $command is still on cooldown for $cd minutes!",
        "onUserCooldown": "$user $command is still on user cooldown for $cd minutes!",
        "responseNotEnoughPoints": "$user you have only $points $currency to convert things smuConfused",
        "response": u"$sourceValue$sourceUnit = $targetValue$targetUnit @$user $fuzzy"
    }

def SendBack(data, message):
    if data.IsFromDiscord():
        Parent.SendDiscordMessage(message)
    else:
        Parent.SendStreamMessage(message)

def HandleChat(data):
    if data.IsChatMessage() and data.GetParam(0).lower() == settings["command"] and Parent.HasPermission(data.User, settings["permission"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
        if len(data.GetParam(1).lower()) == 0:
            SendBack(data, "You need to provide the unit (temperature or weight), e.g. 42C, 4242F, 42kg, 42lb")
            return

        outputMessage = ""
        userId = data.User
        username = data.UserName
        points = Parent.GetPoints(userId)
        costs = settings["costs"]

        if (costs > Parent.GetPoints(userId)) or (costs < 1):
            outputMessage = settings["responseNotEnoughPoints"]
        elif settings["useCooldown"] and (Parent.IsOnCooldown(ScriptName, settings["command"]) or Parent.IsOnUserCooldown(ScriptName, settings["command"], userId)):
            if settings["useCooldownMessages"]:
                if Parent.GetCooldownDuration(ScriptName, settings["command"]) > Parent.GetUserCooldownDuration(ScriptName, settings["command"], userId):
                    cdi = Parent.GetCooldownDuration(ScriptName, settings["command"])
                    cd = str(cdi / 60) + ":" + str(cdi % 60).zfill(2)
                    outputMessage = settings["onCooldown"]
                else:
                    cdi = Parent.GetUserCooldownDuration(ScriptName, settings["command"], userId)
                    cd = str(cdi / 60) + ":" + str(cdi % 60).zfill(2)
                    outputMessage = settings["onUserCooldown"]
                outputMessage = outputMessage.replace("$cd", cd)
            else:
                outputMessage = ""
        else:
            outputMessage = settings["response"]
            if settings["useCooldown"]:
                Parent.AddUserCooldown(ScriptName, settings["command"], userId, settings["userCooldown"])
                Parent.AddCooldown(ScriptName, settings["command"], settings["cooldown"])

        fuzzy = ""
        inputStr = data.GetParam(1).lower() + data.GetParam(2).lower()
        try:
            if len(data.GetParam(1).lower()) == 0:
                # SendBack(data, ("You need to provide the temperature, e.g. 42C or 4242F WHY HERE???")
                return
            value, sourceValue = findConverter(inputStr)
            if value is None:
                SendBack(data, "This did not work smuConfused Provide a number and then a unit (kg,lb,lbs,F,C,km,mi,cm,in) for example !convert 42kg")
                return
            sourceUnit = value['sourceUnit']
            targetUnit = value['targetUnit']
            targetValue = value['transformFun'](sourceValue)
            fuzzy = value['fuzzyFun'](sourceValue, targetValue)
        except Exception, e:
            outputMessage = "@$user Invalid input NotLikeThis Try $command 42C Error: " + str(e)

        outputMessage = outputMessage.replace("$sourceValue", str(sourceValue))
        outputMessage = outputMessage.replace("$targetValue", str(targetValue))
        outputMessage = outputMessage.replace("$sourceUnit", sourceUnit)
        outputMessage = outputMessage.replace("$targetUnit", targetUnit)
        outputMessage = outputMessage.replace("$cost", str(costs))
        outputMessage = outputMessage.replace("$user", username)
        outputMessage = outputMessage.replace("$points", str(points))
        outputMessage = outputMessage.replace("$currency", Parent.GetCurrencyName())
        outputMessage = outputMessage.replace("$command", settings["command"])
        outputMessage = outputMessage.replace("$fuzzy", fuzzy)

        SendBack(data, outputMessage)

def Execute(data):
    if data.IsChatMessage():
        #SendBack(data, "V 1.1")
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
