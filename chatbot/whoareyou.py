import discord
import random
client = discord.Client(intents=discord.Intents.all())
@client.event
async def on_ready():
    print('BOT IS READY')

@client.event
async def on_message(message):

    username = str(message.author).split('#')[0]

    user_message = str (message.content)
    channel=str(message.channel.name)
    print(f'{username}: {user_message}({channel})')

    if message.author == client.user:
        return
    if message.channel.name == 'game' or 'general' or 'music':

        if message.content.startswith('who are you JARVIS'):
            await message.channel.send(f'HI MY NAME IS JARVIS I AM AI CREATE CHAT BOT I AM HERE TO MANGE THIS SERVER I AM RUNNING ON PYTHON CODE ;)')




            await client.process_commands(message)

client.run('TOKEN')