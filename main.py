from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='11a7d4ea5ca44a99838403e265a62c16')

# /v2/top-headlines
#top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                          sources='bbc-news,the-verge',
#                                          category='business',
#                                          language='en',
#                                          country='us')

# /v2/everything
#all_articles = newsapi.get_everything(q='bitcoin',
#                                      sources='bbc-news,the-verge',
#                                      domains='bbc.co.uk,techcrunch.com',
#                                      from_param='2017-12-01',
#                                      to='2017-12-12',
#                                      language='en',
#                                      sort_by='relevancy',
#                                      page=2)

# /v2/sources
# Поиск по категориям
def category():
	pass



# Поиск по ключевым словам
def description():
	pass

# Поиск по запросу
def searh_public():
	pass

sources = newsapi.get_sources()

language = str(input('Введите язык: '))
top_headlines = newsapi.get_top_headlines(language=language)
print (top_headlines)