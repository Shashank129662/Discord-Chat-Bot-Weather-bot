import discord
from discord.ext.commands import Bot
intents = discord.Intents.all()
bot = Bot(command_prefix='!',intents=intents)

@bot.command()
async def kick(ctx):
    user_to_kick = discord.utils.find(lambda u: u.name == 'user_to_kick', ctx.message.guild.members)
    if user_to_kick is not None:
        await ctx.message.guild.kick(user_to_kick)
        await ctx.send(f'{user_to_kick} was kicked by {ctx.message.author}.')
    else:
        await ctx.send(f'No user with the name "user_to_kick" found in this server.')

bot.run('TOKEN')