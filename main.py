import discord
from discord.ext import commands

import keys
import weather.weather

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(intents = intents, command_prefix='!')
tree = bot.tree

@bot.event
async def on_ready():
    print(f'{bot.user} is connected to the following server(s):\n')
    for server in bot.guilds:
        print(f'{server.name}(id: {server.id})')

@bot.command(name = 'weather', pass_context=True)
async def get_weather(ctx: discord.ext.commands.context.Context, *, content:str):
        await ctx.send(f'Requesting weather for your location')
        response = await weather.weather.get_weather_data(content, keys.WEATHER_API_KEY)
        await ctx.send(f'{response}')

@bot.command(name = 'echo')
async def echo(ctx: discord.ext.commands.context.Context, *, content:str):
    await ctx.send(content)

@bot.command(name = 'echoMe')
async def echo_me(ctx: discord.ext.commands.context.Context, *, content:str):
    await ctx.author.send(content)

bot.run(keys.DISCORD_TOKEN)