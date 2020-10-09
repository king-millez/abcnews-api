from abcnews_api import article

urls = ['https://www.abc.net.au/news/2020-10-09/coles-experience-nationwide-closure-over-it-outage/12749358', 'https://www.abc.net.au/news/2020-10-09/coronavirus-australia-live-news-covid19-latest-altona-high-risk/12746074', 'https://www.abc.net.au/news/2020-10-09/budget-signals-return-to-politics-as-usual/12748090']
for url in urls:
    print(article.read_article(url))