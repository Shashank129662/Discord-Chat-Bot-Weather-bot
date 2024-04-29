import discord
import random
import emoji
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

        if message.content.startswith("send random emoji"):
            gifs = "\U0001f600","\U0001F606","\U0001F923","\U0001F610","\U0001F611","\U0001F636","\U0001F60F","\U0001F644","\U00011F62C","\U0001F61B","\U0001F61C","\U0001F92A","\U0001F61D","\U0001F911","\U0001F917","\U0001F92D","\U0001F92B","\U0001F914","\U0001F910","\U0001F928"
            gif = random.choice(gifs)
            await message.channel.send(f'{gif}')
            await client.process_commands(message)

client.run('TOKEN')