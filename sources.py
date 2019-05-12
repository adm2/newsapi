import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=business&'
       'apiKey=11a7d4ea5ca44a99838403e265a62c16')
response = requests.get(url)
print (response.json())
