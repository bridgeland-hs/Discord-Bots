import discord

todos = []

async def todo_command(message):
    
    args = message.content.split(' ')[1:]
    
    author = message.author.mention
    
    if args[0] == 'list':
        await list_todos(message)
    
    elif args[0] == 'add':
        await add_todo(message, author, ' '.join(args[1:]))
        
    elif args[0] == 'complete':
        await complete_todo(message, int(args[1]))
        
    elif args[0] == 'delete':
        await delete_todo(message, int(args[1]))
        
async def list_todos(message):
    global todos
    
    embed = {
        'title': 'To-Do List',
        'description': 'Current To-Do Items',
        'fields': [],
    }
    
    index = 0
    for todo in todos:
        checked = ':white_check_mark:' if todo['completed'] else ''
        embed['fields'].append({
            'name': f'{index + 1}. {checked} {todo["name"]}',
            'value': f'Added By {todo["author"]}',
        })
        index += 1
        
    await message.channel.send(embed=discord.Embed.from_dict(embed))
    
    
async def add_todo(message, author, name):
    global todos
    
    todos.append({
        'name': name,
        'author': author,
        'completed': False,
    })
    
    await message.reply('To-Do Added!')
    
async def complete_todo(message, id):
    global todos
    
    todo = todos[id - 1]
    todo['completed'] = not todo['completed']
    
    await message.reply(f'To-Do item {id} toggled')
    
async def delete_todo(message, id):
    global todos
    
    todos.pop(id - 1)
    
    await message.reply('To-Do Removed')