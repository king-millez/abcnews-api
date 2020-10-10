import requests
from bs4 import BeautifulSoup
import re

def find_articles(term):
    search_results = requests.get('http://search.abc.net.au/search/search.cgi?collection=abcnews_meta&form=advanced&query=' + term)
    if(search_results.status_code != 200):
        return('Error: Got HTTP status code ' + str(search_results.status_code))

    else:
        soup = BeautifulSoup(search_results.text, 'lxml') # The usual html.parser doesn't work here, there's so many errors in the HTML that we have to use lxml.
    
    try:
        total = int(soup.find('p', string=re.compile('Documents: ')).text.split('\n')[1].split(' ')[1]) # This finds the number of returned results
    except:
        return('The search query did not contain any words.')
    
    if(total == 0):
        return('No results were found...')

    elif(total > 0):
        total = total - int(str(total)[len(str(total)) - 1]) - 10
        req = 1
        _search_results = []
        for i in range(int(str(total / 10)[:-2]) + 2):
            pageres = requests.get('http://search.abc.net.au/search/search.cgi?collection=abcnews_meta&form=advanced&query=' + term + '&start_rank=' + str(req))
            if(pageres.status_code != 200):
                return('Error: Got HTTP status code ' + str(pageres.status_code) + ' on search ' + 'http://search.abc.net.au/search/search.cgi?collection=abcnews_meta&form=advanced&query=' + term + '&start_rank=' + str(req))
            
            else:
                soup = BeautifulSoup(pageres.text, 'lxml')
                div = soup.find('div', {'id': 'mainColumn'})
                _headings = div.find_all('h3')[1:]
                for heading in _headings:
                    url = heading.find('a')['href']
                    title = heading.find('a').text[:-1]
                    _search_results.append([url, title])
            req = req + 10
        return(_search_results)
    else:
        return('Something weird happened, here\'s the supposed results total: ' + str(total) + '\n\nPlease submit an issue at https://github.com/king-millez/abcnews-api/issues/new/choose with the search term you used...')