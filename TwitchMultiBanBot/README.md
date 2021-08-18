# MultiBan
A Script for Streamlabs Chatbot to ease banning multiple accounts at once.

# Why?
Because twitch is too slow when it comes to protecting marginalized creators. [Please read this petition for more details, and sign it too](https://www.change.org/p/amazon-twitch-do-better-stop-hate-raids-against-people-of-color-and-marginalized-creators).

# Other tools
This tool is in a very early stage and only works on one specific case.

There are other tools for mass-banning that you might want to take a look at, e.g. [CommanderRoot](https://twitch-tools.rootonline.de/blocklist_manager.php#).

## What does it do?
Once installed, entering
`!multiban 3`
in twitch chat will print out a list of everyone who raided in the last 3 minutes.

If you enter
`!multiban 3 ban`
it will actually ban people.

### Careful
The time starts new with every command.
If you first just get a list of names to check, and take a minute to read them,
you need to add one minute when issueing the actual ban.




## How it works
When Streamlabs Chatbot is started with MultiBanBot enabled,
it will read chat messages and store all users who raid and host!

When you enter the command (multiban) it will go through the list of raids/hosts
and see if it should ban them, given the timing.

## Installation Instructions
* Download [the latest version as zip](https://github.com/smu4242/TwitchBot/releases) and drop it in your
streamlabs chatbot scripts directory.
* In Chatbot, go to Scripts (at the bottom) and then click the "import" button at the top right and select the zip file.
* Full instruction [can be found here](https://streamlabs.com/content-hub/post/chatbot-scripts-desktop).

