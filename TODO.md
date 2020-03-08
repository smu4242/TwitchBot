# BACKGROUND:
current there is only 1 script for the converter (!convert command)

# Current GOAL:
- [x] make it so that writing the json file does not remove previous entries!
  - [x] make a backup everytime we write the json file
  - [x] read the file, add data, write the file
- [x] streamlabs bot and discord bot are separated! We need to make sure that whenever the streamlabs bot is active, the discord bot reads its file!
- [x] run the bot repeatedly while I'm live
- [ ] remember all roles ever created by the bot, so that we can clean up!
- [ ] sort the rank list by rank hierarchy
- [ ] remove dyno.gg bot

SOLUTION 1:
 streamlabs chatbot (in py 2) just calls another scripts to create the roles
 other script (in py 3) actually creates the roles


# DONE:
- [x] assign the roles to people(?)
  - [x] write the people in the json file (streamlabs bot)
  - [x] read the people from the json file (discord bot)
- [X] remove the "V 1.1"
- [X] split up the converter script into "converter" and "discord roles"
- [X] put the roles into discord
- [X] get the ranks from streamlabs chatbot (!derps like "True SmuSmu", "NewSmu")


# Ideas for later
- [ ] a key input - type in chat and that gets send as key input to the streamer LOL
- [ ] make a "speedmeter" that shows how nice chat is. AI?
  - this could be for some different input as well, like twitter

- [ ] SOMETHING with evolution in it

- [ ] A game that integrates with twitch somehow - kinda like twitch plays
    * maybe something with a grid, so that it's easy to type coordinates
    * maybe something where the streamer/AI needs to escape a maze and the viewers stop them
    * maybe minecraft tetris?
