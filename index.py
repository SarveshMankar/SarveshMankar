import random
import json
import markdown
from bs4 import BeautifulSoup
import requests
import os

API_KEY = os.environ.get('api_key')

category = ['inspirational','attitude','dreams','experience','intelligence','leadership','success']
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category[random.randint(0,6)])
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

if response.status_code == requests.codes.ok:
    quote=response.text
    quotes = json.loads(quote)
    q=quotes[0]['quote']
    mq=q.split('.')[0]
else:
    print("Error:", response.status_code, response.text)

with open("README.md", mode="r", encoding="utf8") as f:
    readme_text = f.read()

# finding tag
readme_text
opening_tag = "<h3 quote"
closing_tag = "</h3 quote"

start_index = readme_text.index(opening_tag)
end_index = readme_text.index(closing_tag)

quotemarkdown = "<h3 quote align='center'>"+mq+"."+"</h3 quote>"

content = readme_text[start_index+len(opening_tag):end_index]
new_content = readme_text[:start_index]+quotemarkdown+readme_text[end_index+len(closing_tag)+1:]

# writing into readme file
readme_file = open("README.md", mode="w", encoding="utf8",)
readme_file.write(new_content)

