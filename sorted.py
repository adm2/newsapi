import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2019-05-12&'
       'sortBy=popularity&'
       'apiKey=11a7d4ea5ca44a99838403e265a62c16')

response = requests.get(url)

print (r.json)