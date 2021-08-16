# MultiBan
A Script for Streamlabs Chatbot to ease banning multiple accounts at once.

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
Download (the latest version as zip)[github.com/...] and drop it in your
streamlabs chatbot scripts directory.
Full instruction (can be found here)[https://streamlabs.com/content-hub/post/chatbot-scripts-desktop]
