import requests
import pprint
url = ('https://newsapi.org/v2/top-headlines?'
       'country=en&'
       'sources=bbc-news&'
	   'apiKey=11a7d4ea5ca44a99838403e265a62c16')
response = requests.get(url)
pprint.pprint (response.json())