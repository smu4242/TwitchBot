# DiscordRoleBot
Read roles from Streamlabs Chatbot and put them into discord.
To run it:
./updateranks.py

The following part can still be done manually, but also runs every 5 minutes automatically, assuming streamlabs chatbot is running:

go to discord #test123
type in discord:
!write
this should create a file roles.json
then the *bot* types in discord
!s
this should create missing roles and assign roles to people in discord
then, we still need to manually sort the roles in discord
