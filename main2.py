import re
import pprint
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='11a7d4ea5ca44a99838403e265a62c16')

# Получить последние публикации по списку категорий.
def category(select, lang):
	if lang == 1:
		language = 'ru'
	elif lang == 2:
		language = 'en'

	if select == 1:
		category = 'business'
	elif select == 2:
		category = 'entertainment'
	elif select == 3:
		category = 'general'
	elif select == 4:
		category = 'science'
	elif select == 5:
		category = 'sports'
	elif select == 6:
		category = 'technology'
	top_headlines = newsapi.get_top_headlines(category=category,
											  language=language,
											  )
	pprint.pprint (top_headlines)

# Получить последние публикации по списку ключевых слов.
def description():
    keyword = str(input('Введите ключевые слова на english: ').split)
    all_articles = newsapi.get_everything(q=keyword,
                                          language='en',
                                          )                                       
    pprint.pprint (all_articles)

# Поиск публикаций по запросу.
def searh_public():
	pass

user_input = int(input('Выберете пункт в меню \n 1 - Последние публикации по списку категорий \n 2 - Последние публикации по списку ключевых слов \n 3 - Поиск публикаций по запросу \n'))

if user_input == 1: # Последние публикации по списку категорий
    input_category = int(input('Выберете категорию \n 1 - Бизнес \n 2 - Развлечения \n 3 - Основные \n 4 - Наука \n 5 - Спорт \n 6 - Технологии \n'))
    input_language = int(input('Выберете язык \n 1 - Русский \n 2 - Английский \n'))
    category(input_category, input_language)
elif user_input == 2: # Последние публикации по списку ключевых слов
	description()
elif user_input == 3: # Поиск публикаций по запросу
	all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
	print (all_articles)

elif user_input == 4:
	sources = newsapi.get_sources()
	pprint.pprint (sources)


#language = str(input('Введите язык: '))
#top_headlines = newsapi.get_top_headlines(language=language)
#print (top_headlines)