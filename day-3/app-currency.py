import os
import discord
import requests

token = os.environ.get('TOKEN')

client = discord.Client()

async def get_quote(message):
    res = requests.get('https://quoste-garden.herokuapp.com/api/v3/quotes/random')
    
    if not res.ok:
        await message.channel.send(f':warning: Error Getting Quote: `{res.status}`')
        return
    
    
    quote_json = res.json()
    quote = quote_json['data'][0]

    quote_text = quote['quoteText']
    quote_author = quote['quoteAuthor']
    quote_genre = quote['quoteGenre']
    
    quote_embed = {
        'title': 'Quote',
        'fields': [
            {
                'name': 'Author',
                'value': quote_author,
                'inline': True,
            },
            {
                'name': 'Genre',
                'value': quote_genre,
                'inline': True,
            },
            {
                'name': 'Quote',
                'value': f'```{quote_text}```',
            }
        ]
    }
    
    await message.channel.send(embed=discord.Embed.from_dict(quote_embed)))

async def get_image(message): 
    res = requests.get('https://inspirobot.me/api?generate=true')
    
    if not res.ok:
        await message.channel.send(f':warning: Error Getting Quote: `{res.status}`')
        return
    
    embed = {
        'title': 'Inspirobot',
        'image': {
            'url': res.text
        }
    }
    
    await message.channel.send(embed=discord.Embed.from_dict(embed))

money = {
    'funnyboy_roks#0001': 100,
}    

@client.event
async def on_ready():
    print(f'Hello World! -- {client.user}')


@client.event
async def on_message(message):
    global money
    
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
    elif message.content == '!quote':
        get_quote(message)
    elif message.content == '!inspire':
        get_image(message)
    elif message.content.startswith('!money'):
        args = message.content.split(' ')[1:]
        if args[0] == 'set':
            money[message.author.discriminator] = int(args[1])
        elif args[0] == 'get':
            amt = money[message.author.discriminator]
            await message.channel.send(f'${amt}')
        elif args[0] == 'add':
            amt = money[message.author.discriminator]
            amt += int(args[1])
            money[message.author.discriminator] = amt
            await message.channel.send(f'Now at ${amt}')
        elif args[0] == 'remove':
            amt = money[message.author.discriminator]
            amt -= int(args[1])
            money[message.author.discriminator] = amt
            await message.channel.send(f'Now at ${amt}')

client.run(token)
