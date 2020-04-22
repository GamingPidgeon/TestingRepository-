# bot.py
import os
import random
import discord



TOKEN = "NzAyNTUxMDIzMTU1NDEyOTk2.XqBtJQ.47SHqLAys9hzxX7IzbpdQraIGXM"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    RankMessage="The current ranks are Corporal and Soldier"
    if message.content == '!Ranks':
        response = RankMessage
        print(response)
        await client.send_message(message.channel, response)







client.run(TOKEN)