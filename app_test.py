import discord
import os

token = os.environ['app_test_token']

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

client.run(token)