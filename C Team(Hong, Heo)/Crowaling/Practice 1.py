import requests
import bs4
import urllib

def spider(max_pages):
    for page in range(1, max_pages + 1):
        query = urllib.parse.urlencode({'query':u'대선후보'})
        url = 'http://news.naver.com/main/search/search.nhn?query=' + '%B4%EB%BC%B1%C8%C4%BA%B8'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = bs4.BeautifulSoup(plain_text, 'html.parser')
        content = soup.find(id='search_div')
        for result in content.select('ul > li > div'):
            print('############# Title')
            print(result.a.text)
            print('############# Content')
            print(result.p.text)

spider(1)
