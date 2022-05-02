import os
import discord
import requests
from todo import todo_command

token = os.environ.get('TOKEN')

client = discord.Client()

async def quote(message):
    res = requests.get('https://quote-garden.herokuapp.com/api/v3/quotes/random')
    
    if not res.ok:
        await message.channel.send(f':warning: Error {res.status_code}')
        return
    
    quote_json = res.json()
    quote = quote_json['data'][0]

    quote_text = quote['quoteText']
    quote_author = quote['quoteAuthor']
    quote_genre = quote['quoteGenre']
    
    embed = {
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
                'name': 'Text',
                'value': f'```{quote_text}```',
            },
        ]
    }
    
    await message.channel.send(embed=discord.Embed.from_dict(embed))

async def inspire(message):
    res = requests.get('https://inspirobot.me/api?generate=true')
    
    if res.ok:
        await message.channel.send(res.text)
    else:
        await message.channel.send(f':warning: Error: {res.status_code}')

money = {
    
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
    elif message.content == '!inspire':
        await inspire(message)
    elif message.content == '!quote':
        await quote(message)
    elif message.content.startswith('!money'):
        args = message.content.split(' ')[1:]
        # !money <set|get|add> [args...]
        # !money set 5 -> [!money, set, 5] -> [set, 5]
        
        key = message.author.discriminator
        
        if key not in money:
            money[key] = 0
        
        if args[0] == 'set':
            # !money set <amount>
            money[key] = int(args[1])
            await message.channel.send('set money')
            
        elif args[0] == 'get':
            # !money get
            amount = money[key]
            await message.channel.send('Your money: $' + str(amount))
            
        elif args[0] == 'add':
            await message.channel.send('add money')
            
    elif message.content.startswith('!todo'):
        await todo_command(message)
        

client.run(token)
