Hey Thanks for reading me.  Warning: My English is not the best


I have programmed this bot to show me statistics about the player numbers and ping of my Minecraft server on a Discord server. Yes I love statistics XD.

And I thought this bot could be useful for others too.

This bot uses Python3 and Discord.py

So the Setup is really easy.

First install Python3 or make sure it is installed

First you have to install all Requirements on your Server:
```
pip install matplotlib
pip install numpy
pip install asyncio
pip install discord.py
pip install pathlib
```

If this command dont work try to replace "pip" with "pip3"

Then you have to Create a Bot in the Discord-Developer Portal.

Tutorial:  <https://www.youtube.com/watch?v=ibtXXoMxaho>

than you need to invite the bot to your Discord.

So its time to edit the bot.py

Just Enter Your Server-Ip, Port and the Bot-Token:

```
serverip = "play.spaffel.de"
port = "25565"
bottoken = "your-bot-token"
```

Move all Files (also data.csv) to your Server. (Linux Server to run the bot on)

Grab your Terminal and cd to the Directory of the Bot.

You can use Screen to run the bot 24/7:

```
screen -s Stats-Bot python3 bot.py
```

If its running press ctrl + a + d

**Usage on Discord:**

After the Setup the bot will take 2-3 Hours to collect the first data.

After that you can use:

**!serverstats** To get Statistics about the Playercount and Ping

**!pcount** to get Information from Now

I hope this Explains Enough if you have problems feel free to Contact me: Spaffel#0581
