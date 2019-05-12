import pprint
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='11a7d4ea5ca44a99838403e265a62c16')

keyword = input('Введите ключевые слова: ')
print(keyword)
print(type(keyword))

all_articles = newsapi.get_everything(q=keyword,
                                      language='ru',
                                      sort_by='relevancy',
                                      page=2)

# /v2/sources
#sources = newsapi.get_sources()

pprint.pprint (all_articles)
