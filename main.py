import discord

import keys
import weather.weather

intents = discord.Intents.all()
intents.members = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is connected to the following server:\n')
    for server in bot.guilds:
        print(f'{server.name}(id: {server.id})')

@bot.event
async def on_message(message):
    if message.content.startswith('!weather'):
        response = await weather.weather.get_weather_data("Budapest", keys.WEATHER_API_KEY)
        await message.channel.send(f'{response}')

bot.run(keys.DISCORD_TOKEN)