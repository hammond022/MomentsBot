import os 

import discord
import interactions 


discord_token = os.environ['DISCORD_TOKEN']
client = interactions.Client(token=discord_token)


@client.command


client.start()
