# abcnews-api

Python utility to easily and efficiently interact with the Australian Broadcasting Corporation's news website

## article

Import:

```from abcnews_api import article```

Read an article:

```article.read_article('ARTICLE URL')```

## search

Import:

```from abcnews_api import search```

Search for a term:

```search.find_articles('TERM')```

# Todo

- Add article body scraping

- Add support for articles written before the website overhaul

- Add support for the Beta JS search page