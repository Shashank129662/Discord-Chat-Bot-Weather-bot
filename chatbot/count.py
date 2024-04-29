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

        if message.content.startswith("p! count"):
              guild = message.guild
              member_count = len(guild.members)
              await message.channel.send(f"There are {member_count} members in this server.")
              await client.process_commands(message)

client.run('TOKEN')