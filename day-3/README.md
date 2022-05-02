# Day 3

- [ ] [Connect API to discord bot](#connecting-api-to-discord-bot)
- [ ] [Simple Currency System](#simple-currency-system)

## Connecting API to discord bot

To connect the apis that we used last week to our discord bot, we need to import `requests` like we did in our `api.py`

```py
import requests
```

Then we can create two functions:

```py
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
```

and

```py
async def inspire(message):
    res = requests.get('https://inspirobot.me/api?generate=true')
    
    if res.ok:
        await message.channel.send(res.text)
    else:
        await message.channel.send(f':warning: Error: {res.status_code}')
```

To use these functions in our bot, we need to add this code after our if statements in `on_message`

```py
elif message.content == '!inspire':
    await inspire(message)
elif message.content == '!quote':
    await quote(message)
```

This will add the `!inspire` and `!quote` commands

## Simple Currency System

We'll add a simple currency system that has a few simple commands

First, we want to add a `!money` command similarly to how we've done the other commands, with the following code

```py
elif message.content.startswith('!money'):
```

inside of this else, we want to convert the arguements that the sender gives into a list


```py
elif message.content.startswith('!money'):
    args = message.content.split(' ')[1:]
```

Now, lets add support for a subcommand:

```py
elif message.content.startswith('!money'):
    args = message.content.split(' ')[1:]

    if args[0] == 'set':
        print('set money')
    elif args[0] == 'get':
        print('get money')
    elif args[0] == 'add':
        print('add money')
```

If you test this, you should see it print a message to the console when you run `!money set`, `!money get`, or `!money add`

Now let's add a dictionary to store the money

At the top, under `client = discord.Client()`, add the following line

```py
money = {}
```

and then under `async def on_message(message):` add this line:

```py
global money
```

The sub command code will now be changed to this:


```py
elif message.content.startswith('!money'):
    args = message.content.split(' ')[1:]

    key = message.author.discriminator
    
    if key not in money:  # If the key is not in the dictionary
        money[key] = 0    # Give it a default value

    if args[0] == 'set':
        money[key] = int(args[1])
    elif args[0] == 'get':
        await message.channel.send(f'Current Money: ${money[key]}')
    elif args[0] == 'add':
        money[key] += int(args[1])
        await message.channel.send(f'Current Money: ${money[key]}')
```

