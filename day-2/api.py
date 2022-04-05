import requests  # Import requests library

# Get InspiroBot image
inspirobot_res = requests.get('https://inspirobot.me/api?generate=true')
inspirobot_url = inspirobot_res.text
print(inspirobot_url)


# Get random quote
quote_res = requests.get('https://quoste-garden.herokuapp.com/api/v3/quotes/random')
quote_json = quote_res.json()
quote = quote_json['data'][0]

quote_text = quote['quoteText']
quote_author = quote['quoteAuthor']
quote_genre = quote['quoteGenre']

print(quote_text)
print(quote_author)
print(quote_genre)
