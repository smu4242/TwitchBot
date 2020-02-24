# BACKGROUND:
current there is only 1 script for the converter (!convert command)

# Current GOAL:
- [X] get the ranks from streamlabs chatbot (!derps like "True SmuSmu", "NewSmu")
  - [ ] write the ranks to a json file
- [ ] streamlabs bot and discord bot are seperated! We need to make sure that whenever the streamlabs bot is active, the discord bot reads its file!
- [ ] assign the roles to people(?)
  - [ ] write the people in the json file (streamlabs bot)
  - [ ] read the people from the json file (discord bot)
- [ ] remember all roles ever created by the bot, so that we can clean up!

SOLUTION 1:
 streamlabs chatbot (in py 2) just calls another scripts to create the roles
 other script (in py 3) actually creates the roles


# DONE:
- [X] remove the "V 1.1"
- [X] split up the converter script into "converter" and "discord roles"
- [X] put the roles into discord
