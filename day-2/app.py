import os
import discord

token = os.environ.get('TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'Hello World! -- {client.user}')


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '!hello':
        await message.channel.send('Hello! 😃')
    elif message.content == '!ping':
        await message.reply('Pong! :ping_pong:')
    elif message.content == '!embed': # '!embed' command
        embed_dictionary = { # Create a dictionary for our embed
            'title': 'My Embed', # Title of the embed
            'image': { # Image of the embed
                'url': 'https://www.cameraegg.org/wp-content/uploads/2016/01/Nikon-D500-Sample-Images-2.jpg' # URL for the image
            },
            'color': 0x328056 # Color of the embed -- https://g.co/kgs/YDYY9Q
        }
        await message.channel.send(embed=discord.Embed.from_dict(embed_dictionary))

client.run(token)
