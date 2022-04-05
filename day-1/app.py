import os       # Import os (for environment variable)
import discord  # Import discord

token = os.environ.get('TOKEN')  # Get the token from the environment variables

client = discord.Client()  # Create instance of Client


@client.event
async def on_ready():                        # When the bot successfully connects to Discord
    print(f'Hello World! -- {client.user}')  # Print a message to the console


@client.event
async def on_message(message):  # When a message is sent in a channel
    if message.author.bot:      # Ignore if the message was sent by a bot
        return

    if message.content == '!hello':               # Message content is '!hello'
        await message.channel.send('Hello! 😃')   # Send message in the channel
    elif message.content == '!ping':              # Message content is '!ping'
        await message.reply('Pong! :ping_pong:')  # Reply to the message

client.run(token)
