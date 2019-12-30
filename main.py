import os
import threading
import discord
from discord.ext import tasks
from dotenv import load_dotenv

client = discord.Client()

@tasks.loop(seconds=0.1)
async def do_operate ():
    line = input()
    is_status = False
    if line[:8] == "[Status]":
        is_status = True
        line = line[8:]
    if line == "":
        return
    print(is_status, line)
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
                print(new_words)
                if not is_status:
                    await channel.send(content=new_words)
                else:
                    await client.change_presence(activity=discord.Game(line))

@client.event
async def on_ready():
    do_operate.start()

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
channel_name = os.getenv('CHANNEL')

client.run(token)
