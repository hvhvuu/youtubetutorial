import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
TOKEN = 'NzEzNDY2OTI5NDI3MjUxMjkx.Xsgh5w.YR4SpzE-74VRvysEgdsfUskKY-U'


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)