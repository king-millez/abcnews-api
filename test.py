from abcnews_api import search, article

articletoget = search.find_articles('Marise Payne says the search for the two remaining victims has been hampered by poor weather conditions today')[0]
print('Found article: ' + str(articletoget))
print(str(article.read_article(articletoget[0])))