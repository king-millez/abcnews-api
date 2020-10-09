import re
from bs4 import BeautifulSoup
from requests import get

ID = 'id'
TITLE = 'title'
TEASER_TITLE = 'teaser_title'
AUTHORS = 'authors'
PUBLISHED_TIME = 'published_time'
MODIFIED_TIME = 'modified_time'
CATEGORY = 'category'
KEY_POINTS = 'key_points'
TEXT = 'text'
URL = 'url'

def read_article(url):
    if not re.match(r'https?://(?:www\.)?abc\.net\.au/news/(?:[^/]+/){1,2}(?P<id>\d+)', url):
        return('Invalid URL...')

    _article_url = url
    _article_id = url[-8:]
    _article_key_points = ''
    _article_text = ''

    page = get(url).text.replace('&#x27;', '\'').replace('中', '').replace('文', '').replace('新', '').replace('冠', '').replace('疫', '').replace('情', '').replace('特', '').replace('别', '').replace('报', '').replace('道', '')
    soup = BeautifulSoup(page, 'html.parser')
    _article_title = soup.find('title').text[:-11]
    _article_teaser = soup.find('meta', {'property': 'og:title'})['content']
    _article_published_time = soup.find('meta', {'property': 'article:published_time'})['content']
    _article_modified_time = soup.find('meta', {'property': 'article:modified_time'})['content']
    try:
        _article_category = soup.find('a', {'class': '_1v60e _2f8qj FQVx7 _2tPjN _1QHxY'}).text
    except:
        _article_category = 'N/A'
    
    try:
        _article_authors = []
        for author in soup.findAll('a', {'class': '_2f8qj FQVx7 _2tPjN _1QHxY z7Xgw'}):
            _article_authors.append(author.text)

    except:
        _article_authors = ['N/A']

    _article_dict = {URL: _article_url, ID: _article_id, TITLE: _article_title, TEASER_TITLE: _article_teaser, AUTHORS: _article_authors, PUBLISHED_TIME: _article_published_time, MODIFIED_TIME: _article_modified_time, CATEGORY: _article_category}
    return(_article_dict)