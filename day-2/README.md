# Embeds and APIs

We used two python files today, [`app.py`](./app.py) and [`api.py`](./api.py)

## Overview

- [x] [What is an embed?](#what-is-an-embed)
    - [x] [Parts of an embed](#parts-of-an-embed)
- [x] [Making an embed](#making-an-embed)
    - [x] Python Dictionary
    - [x] `discord.Embed.from_dict`
    - [x] Send it to a channel
- [x] What is an API?
    - [x] Web Service APIs
    - [x] REST APIs
    - [x] Examples
- [x] How do I use an API
    - [x] `requests` library
- [ ] ~~How do I use an API with my Discord Bot?~~
    - Not done in day 2 - moved to day 3

## What is an Embed?

An Embed is a fancier way of displaying data that only bots and webhooks can use

### Parts of an Embed

An embed can have the following values (and some others not listed):

```ts
{
    title: string,
    description: string,
    url: string,
    color: number, // 0xRRGGBB
    footer: {
        text: string,
        icon_url: string,
    },
    image: {
        url: string,
        height: number,
        width: number,
    },
    thumbnail: {
        url: string,
        height: number,
        width: number,
    },
    video: {
        url: string,
        height: number,
        width: number,
    },
    author: {
        name: string,
        url: string,
        icon_url: string,
    },
    fields: [
        {
            name: string,
            value: string,
            inline: boolean,
        }
    ]
}
```

## Making an Embed

To make an embed, we need to create a dictionary in Python

```py
embed_dictionary = {
    'title': 'Embed Title',
    'description': 'This is the description for an embed\nIt supports **markdown** to __format__ your *messages*\nAnd it supports emojis :smile:'
}
```

To convert this dictionary into an embed, we need to use the `Embed.from_dict` method:

```py
embed = discord.Embed.from_dict(embed_dictionary)
```

Now that we have an embed, we send it similarly to any other messge

```py
await message.content.send(embed=embed)
```

## What is an API?

An API is a service that allows two applications on the same or different computers to share data.

We're going to be using a **Web Service** type called **REST** as it's one of the most common types of public APIs for data.

There's a couple of different ways to use a REST API depending on how they're setup, the most common methods are called `GET` and `POST`.

### `GET`

The `GET` method tells the server that we're trying to get some sort of data, it's very simple and the only data that it sends to the server is in the URL

This is what your web browser sends when it tries to get a web page.

### `POST`

The `POST` method tells the server that we're trying to send some sort of data.  it has a `body` that contains the data that we're trying to send

### JSON

JSON is a way to share data between different applications on 

### Examples

The two example APIs that we'll be using are

- [InspiroBot](https://inspirobot.me/api?generate=true) - Returns the URL in plaintext
<<<<<<< HEAD
- [Quote Garden](https://quote-garden.herokuapp.com/api/v3/quotes/random) - Returns quote data as JSON


=======
  - When you go to this url, it returns a plaintext url
- [Quote Garden](https://quote-garden.herokuapp.com/api/v3/quotes/random) - Returns quote data as JSON
  - When you go to this url, it returns JSON data

## Using an API

In Python, to use an API, we'll use the `requests` package

Install it like you did with the `discord.py` package with the packages tab on the left

and then you can import it using

```py
import requests
```

To make a GET request to an API, use the following code

```py
import requests

url = 'YOUR API URL'

res = requests.get(url)

# If the API returns plaintext, use
data = res.text

# If the API returns JSON, use
data = res.json()
```
>>>>>>> 85764a1778c2287e67ff25e53a6497400da0dcb3
