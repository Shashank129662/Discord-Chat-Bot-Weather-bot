import requests
import json


def get_weather_data(api_key, city):

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={28.70}&lon={77.10}&appid={api_key}'
    response = requests.get(url)
    return json.loads(response.text)


def get_temperature_in_celsius(weather):
    temp_kelvin = weather['main']['temp']
    return temp_kelvin - 273.15


def get_weather_conditions(weather):
    conditions = weather['weather'][0]['description']
    return conditions


import discord


client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'today weather':

        api_key = '7f02a09652e01aa4fab479d5a9fa0b95'
        weather = get_weather_data(api_key, 'Delhi')
        temp = get_temperature_in_celsius(weather)
        conditions = get_weather_conditions(weather)
        await message.channel.send(f'The temperature in Delhi is {temp:.1f}°C, with {conditions}.')

client.run('TOKEN')
