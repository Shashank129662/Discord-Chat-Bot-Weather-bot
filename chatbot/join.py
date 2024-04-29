import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'p! join' in message.content.lower():
        channel_name = 'Lounge'
        channel = discord.utils.get(message.guild.channels, name=channel_name)

        if not channel:
            await message.channel.send(f'Channel {channel_name} not found')
        else:
            await channel.connect()
            await message.channel.send(f'Connected to {channel_name}')

client.run('TOKEN')