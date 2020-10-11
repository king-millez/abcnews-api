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
    try:
        _article_published_time = soup.find('meta', {'property': 'article:published_time'})['content']
    except:
        _article_published_time = soup.find('meta', {'name': 'DCTERMS.issued'})['content']
    
    try:
        _article_modified_time = soup.find('meta', {'property': 'article:modified_time'})['content']
    except:
        _article_modified_time = soup.find('meta', {'name': 'DCTERMS.modified'})['content']
    
    try:
        _article_category = soup.find('a', {'class': '_1v60e _2f8qj FQVx7 _2tPjN _1QHxY'}).text
    except:
        _article_category = 'none'
    
    try:
        _article_authors = []
        author_span = soup.find_all('span', {'class': '_21SmZ _3_Aqg _1hGzz _1-RZJ P8HGV', 'data-component': 'Text'})[len(soup.find_all('span', {'class': '_21SmZ _3_Aqg _1hGzz _1-RZJ P8HGV', 'data-component': 'Text'})) - 1]
        for tag in author_span.find_all('a', {'class', '_2f8qj FQVx7 _2tPjN _1QHxY z7Xgw'}):
            if(tag['href'][:28] != 'https://www.abc.net.au/news/'):
                _article_authors = [author_span.text.split(' ')[1] + ' ' + author_span.text.split(' ')[2]]
            else:
                _article_authors.append(tag.text)

    except:
        _article_authors = []

    _article_dict = {URL: _article_url, ID: _article_id, TITLE: _article_title, TEASER_TITLE: _article_teaser, AUTHORS: _article_authors, PUBLISHED_TIME: _article_published_time, MODIFIED_TIME: _article_modified_time, CATEGORY: _article_category}
    return(_article_dict)