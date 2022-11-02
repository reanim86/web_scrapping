import requests
import bs4
from fake_useragent import UserAgent
from pprint import pprint

ua = UserAgent()
url = 'https://habr.com/ru/all/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get(url, headers={'User-Agent': ua.chrome})
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')

# articles = soup.find(class_='tm-articles-list')
articles = soup.find(id='697146').find(class_='tm-article-snippet__title tm-article-snippet__title_h2').attrs[]


# for article in articles:
#     preview_inf = article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
#     pprint(article.attr())





    # print(type(preview_inf.text))    article-formatted-body article-formatted-body article-formatted-body_version-1
    # title = article.find(class_='tm-article-snippet__title-link').find('span')
    # print(preview_inf.text)
