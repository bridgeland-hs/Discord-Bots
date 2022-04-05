# Day 1 - Setup and Basics

View the code we did together [here](app.py)

## Overview

- [x] [Setup Repl.it](#setup-replit)
- [x] [Environment Variables](#environment-variables)
  - [x] Setting up Discord Bot Token
- [x] [Installing a package using Repl.it](#installing-a-package-with-replit)
- [x] [Connecting to Discord](#connecting-to-discord)
  - [x] Creating a client instance
  - [x] Running the client using our bot token
- [x] [Events](#events)
  - [x] `@client.event` decorator
  - [x] `on_ready()`
  - [x] `on_message(message)`

## Setup Repl.it

To setup Repl.it, all you need to do is create a new Repl with Python as the language, from there you can follow along with what we do.

## Environment Variables

An environment variable is crucial to hide secret data such as your bot token.

You can create an environemnt variable in Repl.it by going to to the "Secrets" tab on the left (looks like a padlock)

Create a secret called `TOKEN` and give it the value of your bot token.

This environment secret can be used in your code by using the following code:

```py
import os

token = os.environ.get('TOKEN')
```

When you add this code, you'll get a variable called `token` that contains the data saved in the `TOKEN` secret

## Installing a Package With Repl.it

A package in Python and most other languages is a collection of code that somebody has published on the internet for other people to access and add to their code.

We'll be using a few packages throughout our unit, but for now, the only one that we need to install is called `discord.py`.

You can install a package with Repl.it by going to the left side and clicking on the "Packages" tab (looks like a blank cube)

From there, you can search for the `discord.py` package and install it (Make sure it's `discord.py` exactly and no alternative spellings)

## Connecting to Discord

First, we must import the discord library, which can be done by adding `discord` to the import statement that we [used earlier](#environment-variables)

```py
import os, discord
#        ^^^^^^^^^

token = os.environ.get('TOKEN')
```

Now, we can create an instance of the client class and assigning it to a variable, like so:

```py
import os, discord

token = os.environ.get('TOKEN')

client = discord.Client()
# ^^^^^^^^^^^^^^^^^^^^^^^
```

This will create a client object that we can use to do everything associated with our discord bot

The final line that we add will actually connect the bot to discord:

```py
import os, discord

token = os.environ.get('TOKEN')

client = discord.Client()

client.run(token)
#^^^^^^^^^^^^^^^^
```

## Events

An event is something that our bot detect happening.  We can create functions called "Event Handlers" to handle these events and do certain actions when they occur.

To create an event handler, we need to use something called a decorator.  Decorators can do a lot of complex things, but we don't need to go into too much detail for this.

The decorator that we use with discord.py is `@client.event` and we put it on the line before we create the event handler

There are two events that we're going to look at today, [`on_ready`](#on_ready) and [`on_message`](#on_message).

### `on_ready`

The `on_ready` event runs when the bot successfully connects to Discord

We can create this event handler like so:

```py
import os, discord

token = os.environ.get('TOKEN')

client = discord.Client()

@client.event            # <----
async def on_ready():    # <----
    print('Bot ready!')  # <----

client.run(token)
```

> Notice the use of `async` -- this is a very important thing to have, but we'll talk about `async` and its counterpart, `await` another time.

Lets have the bot print its information into the console when it connects to discord using a formatted string:

```py
import os, discord

token = os.environ.get('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot ready at {client.user}!')
    #     ^          ^^^^^^^^^^^^^^^^^

client.run(token)
```

This will print something like `Discord-Bot#0001` to the console when the bot is started.


### `on_message`

The `on_message` event is called whenever a message is sent by a user in any channel that the bot has read permissions in.

We will use this to handle all simple commands

It is important to note that the `on_message` event takes in a `message` parameter that is an object representing the message sent, including properties like `author` and `content`.


```py
import os, discord

token = os.environ.get('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot ready at {client.user}')

@client.event                   # <----
async def on_message(message):  # <----
    print(message.content)      # <----

client.run(token)
```

Any time that we use this method, we want to have this if-statement to prevent anything bad from happening:

```py
if message.author.bot:
    return
```

```py
import os, discord

token = os.environ.get('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot ready at {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:  # <----
        return              # <----

    print(message.content)

client.run(token)
```

There are two ways to respond to a message, shown below:

```py
import os, discord

token = os.environ.get('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot ready at {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    await message.channel.send('Hello :wave:') # Send a message in the channel
    await message.reply('Ping :ping_pong:')    # Directly reply to the message

    print(message.content)

client.run(token)
```

## That's pretty much everything we covered today!
