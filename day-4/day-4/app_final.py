import discord, os
from todo_final import *

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot ready at {client.user}')
    
@client.event
async def on_message(message):
    if message.content.startswith('!todo'):
        await todo_command(message)

load_todos()
client.run(os.environ.get('TOKEN'))