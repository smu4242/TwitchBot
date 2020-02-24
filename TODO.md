# BACKGROUND:
current there is only 1 script for the converter (!convert command)

# Current GOAL:
- [ ] assign the roles to people(?)
  - [x] write the people in the json file (streamlabs bot)
  - [ ] read the people from the json file (discord bot)
- [ ] streamlabs bot and discord bot are seperated! We need to make sure that whenever the streamlabs bot is active, the discord bot reads its file!
- [ ] remember all roles ever created by the bot, so that we can clean up!
- [ ] sort the rank list by rank hierarchy

SOLUTION 1:
 streamlabs chatbot (in py 2) just calls another scripts to create the roles
 other script (in py 3) actually creates the roles


# DONE:
- [X] remove the "V 1.1"
- [X] split up the converter script into "converter" and "discord roles"
- [X] put the roles into discord
- [X] get the ranks from streamlabs chatbot (!derps like "True SmuSmu", "NewSmu")
