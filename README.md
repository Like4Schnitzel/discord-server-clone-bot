# discord-server-clone-bot
This is a Discord bot that scans a server and stores all visible channels, messages, roles and role assignments into a json file.
Once saved, it can recreate a given server. You can use the restore command in any server.
Both of these commands require elevated permissions within the server you're using them in.

HOW TO USE
---
0. In the src directory, rename `env_TEMPLATE.json` to `env.json`.
1. In Discord, go to your User Settings, select "Advanced" and enable "Developer Mode".
2. Open a web browser of your choice and go to https://discord.com/developers/applications. 
3. Click the "New Application" button in the upper right corner, enter a Name (any will do), click the checkmark and choose "Create".
4. Navigate to the "Bot" section in the menu on the left side, then click the "Add Bot" button and confirm.
5. Choose "Reset Token", follow the steps and copy the new one to the "TOKEN" field in `env.json`
6. Scroll down to "Bot Permissions" and choose the following: TODO.
7. In the menu on the lefthand side, open the "OAuth2" section and go to "URL Generator".
8. For "Scopes" choose "bot", then for "Bot Permissions" select the same ones as earlier.
9. Open the link at the bottom in your browser.
10. Choose a Server to add it to from the dropdown menu.

env.json
---
**TOKEN**

As mentioned earlier, "TOKEN" is where you put the token of the discord bot.

Final Steps
---
Make sure you have python 3 installed. If not, install it.\
Run the following commands to install the python discord library: `pip install discord.py`\
Then, put `bot.py` and `env.json` in any directory, just make sure they're in the same one.
Finally, run bot.py with `python3 bot.py` (or some other way of running a python script) and you're done.
