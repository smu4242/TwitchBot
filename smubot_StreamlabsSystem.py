# import clr
# import sys
import json
import os
# import ctypes
# import codecs

ScriptName = "Calculator"
Website = "http://www.example.com/todo"
Description = "Calculator for different temperature units (Celcius & Fahrenheit) and now also weight units (kg & lb)!"
Creator = "smu4242"
Version = "0.0.2"

configFile = "config.json"
settings = {}

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
        "responseNotEnoughPoints": "$user you have only $points $currency to convert things smuDerp",
        "response": u"$sourceValue$sourceUnit = $targetValue$targetUnit @$user $fuzzy"
    }

def Execute(data):
    if data.IsChatMessage() and data.GetParam(0).lower() == settings["command"] and Parent.HasPermission(data.User, settings["permission"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
        if len(data.GetParam(1).lower()) == 0:
            Parent.SendStreamMessage("You need to provide the unit (temperature or weight), e.g. 42C, 4242F, 42kg, 42lb")
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

        inputStr = data.GetParam(1).lower() + data.GetParam(2).lower()

        sourceValue = 0
        targetValue = 0
        sourceUnit = "INVALID"
        targetUnit = "INVALID"
        celcius = 0
        try:
            if len(data.GetParam(1).lower()) == 0:
                # Parent.SendStreamMessage("You need to provide the temperature, e.g. 42C or 4242F WHY HERE???")
                return
            last2 = inputStr[-2:]
            last3 = inputStr[-3:]
            exceptLast2 = inputStr[:-2]
            exceptLast3 = inputStr[:-3]
            if inputStr[len(inputStr)-1] == "c":
                sourceValue = float(inputStr[0:len(inputStr)-1])
                sourceUnit = u"\u00B0C"
                targetUnit = u"\u00B0F"
                targetValue = CtoF(sourceValue)
                fuzzy = calcSassyMessage(sourceValue)
            elif inputStr[len(inputStr)-1] == "f":
                sourceValue = float(inputStr[0:len(inputStr)-1])
                sourceUnit = u"\u00B0F"
                targetUnit = u"\u00B0C"
                targetValue = FtoC(sourceValue)
                fuzzy = calcSassyMessage(targetValue)
            elif last2 == "kg":
                sourceValue = float(exceptLast2)
                sourceUnit = "kg"
                targetUnit = "lb"
                targetValue = kgToLb(sourceValue)
                fuzzy = ""
            elif last2 == "lb":
                sourceValue = float(exceptLast2)
                sourceUnit = "lb"
                targetUnit = "kg"
                targetValue = lbToKg(sourceValue)
                fuzzy = ""
            elif last3 == "lbs":
                sourceValue = float(exceptLast3)
                sourceUnit = "lbs"
                targetUnit = "kg"
                targetValue = lbToKg(sourceValue)
                fuzzy = ""
            else:
                Parent.SendStreamMessage("This did not work smuDerp Provide a number and then a unit (kg,lb,lbs,F,C) for example !convert 42kg")
        except Exception, e:
            outputMessage = "@$user Invalid input NotLikeThis Try $command 42C" + str(e)

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

        Parent.SendStreamMessage(outputMessage)
    return

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

def FtoC(fahrenheid):
    return round((fahrenheid - 32) / 1.8, 1)

def ReloadSettings(jsonData):
    Init()
    return

def OpenReadMe():
    location = os.path.join(os.path.dirname(__file__), "README.txt")
    os.startfile(location)
    return

def Tick():
    return
