# TwitchChatConverter
A Script for Streamlabs Chatbot to convert temperatures (C/F), weight (kg/lbs) and distances (cm,in,km,mi)!

## Prerequisites
1) You need [Streamlabs Chatbot](https://streamlabs.com/desktop-chatbot) up and running.
1) Streamlabs Chatbot requires python, install it as described [in the official docs](https://streamlabs.com/de-de/content-hub/post/chatbot-scripts-desktop).
1) Download the [TwitchConverterBot](https://github.com/smu4242/TwitchBot/tree/master). Click on **Code** and **Download ZIP**.
1) In Chatbot  hit **Scripts** (bottome left), then "Import" (top right) <img width="25" alt="Streamlabs_Chatbot_2023-07-13_15-40-37" src="https://github.com/smu4242/TwitchBot/assets/1223335/1b6f1c51-2c95-4afc-9dea-3931418e9925">
1) Select the file you want, e.g. "smubot_StreamlabsSystem.py".
1) It should work now, e.g. type "!convert 42F" and it should respond, see examples below.
1) You may want to changes some settings [here](https://github.com/smu4242/TwitchBot/blob/master/TwitchConverterBot/smubot_StreamlabsSystem.py#L149), e.g. set `"costs": 0,` in case you don't have ChatBot currency set up or `"showSassyMessage": False,` if you're not feeling as sassy as I am. (The sassy messages only work for temperatures as of now!)

## Example
<img width="304" alt="chrome_2023-07-13_15-36-51" src="https://github.com/smu4242/TwitchBot/assets/1223335/7c6df729-3c63-444e-8a4e-e2cf9f71a24a">
