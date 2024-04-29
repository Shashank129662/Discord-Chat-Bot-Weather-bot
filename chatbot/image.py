import discord

import requests

import json



client = discord.Client(intents=discord.Intents.all())

# Replace YOUR_API_KEY with your Google Custom Search API key
# Replace YOUR_CSE_ID with your Google Custom Search Engine ID
api_key = "AIzaSyBrk1nrorLg1eIqwTj-e4LJNw4GDWC424w"
cse_id = "AIzaSyBrk1nrorLg1eIqwTj-e4LJNw4GDWC424w"

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message}({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'games' or 'general' or 'music':
      if message.content.startswith("!image"):
        query = message.content[6:]
        url = (f"https://www.googleapis.com/customsearch/v1?q={query}&imgSize=large&imgType=photo&num=1&key={api_key}&cx={cse_id}")
        response = requests.get(url).json()
        data = json.dumps(response)
        image_url = data['item'][0]['link']
        await message.channel.send(image_url)

client.run("TOKEN")
