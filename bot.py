import discord
from discord.ext import commands

TOKEN = 'NzEzMjQwNDM3MjI5NjE3MjEz.XsdPHA.7ACghbwzn7j1stGfrOBlaXBxPJI'


client = commands.Bot(command_prefix= '>')

@client.command()
async def clear(ctx, amount):
    amount = int(amount) + 1
    await ctx.channel.purge(limit=amount)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    activity = discord.Activity(name=">help", type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)
    print('------')


client.run(TOKEN)
