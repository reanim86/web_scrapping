import requests
import bs4
from fake_useragent import UserAgent

ua = UserAgent()
url = 'https://habr.com/ru/all/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get(url, headers={'User-Agent': ua.chrome})
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all(class_='tm-articles-list__item')

for article in articles:
    preview_inf = article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
    print(type(preview_inf.text))
    # if 'дизайн' in preview_inf.text:
    #     title = article.find(class_='tm-article-snippet__title-link').find('span')
    #     print(title.text)
