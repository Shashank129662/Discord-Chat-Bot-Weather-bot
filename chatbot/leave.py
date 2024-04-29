import discord


client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):

    if message.content.startswith('!join'):

        voice_channel = message.author.voice.channel

        await voice_channel.connect()
    elif message.content.startswith('!leave'):

        voice_channel = client.voice_clients[0].channel

        await voice_channel.disconnect()


client.run('TOKEN')