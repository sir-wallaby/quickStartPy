import discord
import os

token = os.environ['app_test_token']

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('apex'):
        channel = message.channel
        await channel.send('I guess')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send(f'Hello {msg.author}!')


client.run(token)