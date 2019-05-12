input_sort_by = int(input('Выберете сортировку \n 1 - статьи, более тесно связанные с ключевыми словами \n 2 - Статьи из популярных источников и издателей на первом месте \n 3 (по умолчанию) - Новые статьи на первом месте \n'))
if input_sort_by not in (1,2,3):
  if input_sort_by == 1:
    sort_by = 'relevancy'
  elif input_sort_by == 2:
    sort_by = 'popularity'
  elif input_sort_by == 3:
    sort_by = 'publishedAt'
else:
  sort_by = 1
print(sort_by)