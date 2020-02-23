BACKGROUND:
current there is only 1 script for the converter (!convert command)

GOAL:
 [X] remove the "V 1.1"
 [X] split up the converter script into "converter" and "discord roles"
 [X] get the ranks from streamlabs chatbot (!derps like "True SmuSmu", "NewSmu")
 [ ] put the roles into discord
 [ ] assign the roles to people(?)

PROBLEM:
  streamlabs chatbot scripts WITH discord.py
  streamlabs chatbot requires python 2.X
  discord.py requires python 3.5

SOLUTION 1:
 streamlabs chatbot (in py 2) just calls another scripts to create the roles
 other script (in py 3) actually creates the roles

SOLUTION 2:
 NO streamlabs script
 just one script with py 3 and discord.py: this then reads the file where streamlabs saves the ranks
 [ ] has streamlabs an open format for the ranks? NO?

SOLUTION 3:
 NO discord.py! instead do the requests manually
