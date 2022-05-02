import discord
import json

todos = []  # Empty storage for our todos variable


# The `: discord.Message` gives us a type for better type hints, not required
async def todo_command(message: discord.Message):
    global todos  # Make sure that the interpreter knows we're talking about the global variable
    # Convert the args from a string into a list
    args = message.content.split(' ')[1:]

    if len(args) < 1:  # If there's no args, then give help message
        await message.reply('Usage: !todo <add|list|complete|delete> [args]')
        return

    if args[0] == 'add':  # !todo add <item>
        value = ' '.join(args[1:])  # Item Name
        author = message.author.mention  # Author
        await add_todo(value, author, message)  # Run the method

    elif args[0] == 'list':  # !todo list
        await get_todos(message)

    elif args[0] == 'complete':  # !todo complete <id>
        await complete_todo(int(args[1]) - 1, message)

    elif args[0] == 'delete':  # !todo delete <id>
        await delete_todo(int(args[1]) - 1, message)

    else:  # Otherwise, give a help messagep
        await message.reply('Usage: !todo <add|list|complete|delete> [args]')

    save_todos() # Save the file after every operation


async def add_todo(title: str, author: str, message: discord.Message):
    global todos  # Make sure that the interpreter knows we're talking about the global variable

    todos.append({  # Add a new todo item
        "author": author,
        "title": title,
        "done": False,
    })

    await message.reply('To-Do Added!') # Reply to sender


async def get_todos(message: discord.Message):
    global todos  # Make sure that the interpreter knows we're talking about the global variable

    embed = { # Embed base
        'title': 'Current Todos',
        'color': 0x00ff00,
        'fields': [],
    }

    index = 1
    for todo in todos: # Add all todos to the fields properties
        embed['fields'].append({
            'name': f"{index}. {':white_check_mark: ' if todo['done'] else ''}{todo['title']}",
            'value': f'Added by {todo["author"]}',
        })
        index += 1

    await message.channel.send(embed=discord.Embed.from_dict(embed))


async def complete_todo(item: int, message: discord.Message):
    global todos  # Make sure that the interpreter knows we're talking about the global variable

    todos[item]['done'] = not todos[item]['done'] # Toggle the `done` entry in the dict

    marked = 'marked' if todos[item]['done'] else 'unmarked' # Better formatted message
    await message.reply(f'To-Do {marked} as complete!')


async def delete_todo(item: int, message: discord.Message):
    global todos  # Make sure that the interpreter knows we're talking about the global variable

    todo = todos.pop(item) # Remove the certain item (perhaps use the name in the reply)

    await message.reply('To-Do deleted!')


# If we have time

def save_todos():
    global todos  # Make sure that the interpreter knows we're talking about the global variable

    out = json.dumps(todos) # Convert dict to str

    with open('todos.json', 'w') as file: # Write str to file
        file.write(out)


def load_todos():
    global todos  # Make sure that the interpreter knows we're talking about the global variable

    try:
        with open('todos.json', 'r') as file: # Load the contents of the file into `todo`
            todos = json.loads(file.read())
    except: # If the file doesn't exist
        print('No Todos file found!')
        todos = []
