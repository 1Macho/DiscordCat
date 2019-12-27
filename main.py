import os
import threading
import discord
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
channel_name = os.getenv('CHANNEL')

client = discord.Client()

@client.event
async def on_ready():
    do_operate.start()

@tasks.loop(seconds=1)
async def do_operate ():
    line = input()
    for guild in client.guilds:
        words = line.split(" ")
        new_words = ""
        for word in words:
            if word[0] == '@':
                role_name = word[1:]
                for role in guild.roles:
                    if role.name == role_name:
                        new_words += role.mention + " "
                        break
            else:
                new_words += word + " "
        for channel in guild.channels:
            if channel.name == channel_name:
                await channel.send(content=new_words)

print(token)
client.run(token)
