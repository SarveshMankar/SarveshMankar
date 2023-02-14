import random
import json
import markdown
from bs4 import BeautifulSoup
import requests

category = 'happiness'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': 'AJS1FBub++2RH370GuqBmg==s2AgRz6ufja8i9xl'})

if response.status_code == requests.codes.ok:
    #print(response.text)
    quote=response.text
else:
    print("Error:", response.status_code, response.text)

with open("README.md", mode="r", encoding="utf8") as f:
    readme_text = f.read()

# finding tag
readme_text
opening_tag = "<h2 quote"
closing_tag = "</h2 quote"

start_index = readme_text.index(opening_tag)
end_index = readme_text.index(closing_tag)

quotemarkdown = "<h2 quote align='center'>"+quote["text"]+"</h2 quote>"

content = readme_text[start_index+len(opening_tag):end_index]
new_content = readme_text[:start_index]+quotemarkdown+readme_text[end_index+len(closing_tag)+1:]

# writing into readme file
readme_file = open("README.md", mode="w", encoding="utf8",)
readme_file.write(new_content)

