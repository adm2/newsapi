import re #оставлено чтобы помнить про некорректный  пользовательский ввод
import pprint
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='11a7d4ea5ca44a99838403e265a62c16') # с безопасностью всё плохо...

def input_language():
	input_language = int(input('Выберете язык \n 1 - Русский \n 2 - Английский \n'))
	if input_language == 1:
		language = 'ru'
	elif input_language == 2:
		language = 'en'
	return language

def input_page():
	input_page = int(input('Укажите номер страницы: '))
	return input_page

def input_country():
# разорбать эту каку
   input_country = 	input('Укажите страну для поиска новостей (ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za): ')
   return input_country

def input_sort_by():
	input_sort_by = int(input('Выберете сортировку \n 1 - статьи, более тесно связанные с ключевыми словами \n 2 - Статьи из популярных источников и издателей на первом месте \n 3 - Новые статьи на первом месте \n'))
	if input_sort_by == 1:
		sort_by = 'relevancy'
	elif input_sort_by == 2:
		sort_by = 'popularity'
	elif input_sort_by == 3:
		sort_by = 'publishedAt'
	return sort_by

# Получить последние публикации по списку категорий.
def category():
	select = int(input('Выберете категорию \n 1 - Бизнес \n 2 - Развлечения \n 3 - Основные \n 4 - Наука \n 5 - Спорт \n 6 - Технологии \n'))
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
                                              language=input_language(),
                                              page=input_page(),
                                              country=input_country(),
                                              )
	pprint.pprint (top_headlines)

# Получить последние публикации по списку ключевых слов.
def description():
    keyword = str(input('Введите ключевое слово на english: '))
    all_articles = newsapi.get_everything(q=keyword,
                                          language=input_language(),
                                          sort_by=input_sort_by(),
                                          page=input_page(),
                                          )                                       
    pprint.pprint (all_articles)

# Поиск публикаций по запросу.
def searh_public():
	pass

user_input = int(input('Выберете пункт в меню \n 1 - Последние публикации по списку категорий \n 2 - Последние публикации по списку ключевых слов \n 3 - Поиск публикаций по запросу \n'))

if user_input == 1: # Последние публикации по списку категорий
    category()
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

# я хоть в правильном направлении иду? А то столько всякой фиганды тут понаписано, что походу повернул не туда...





#language = str(input('Введите язык: '))
#top_headlines = newsapi.get_top_headlines(language=language)
#print (top_headlines)