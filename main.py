import requests
import bs4
from fake_useragent import UserAgent
from pprint import pprint

def get_need_article(link, words):
    """
    Функция возвращает список статей с ключевыми словами в описании
    :param link: ссылка на ресурс
    :param words: Ключевые слова для поиска
    :return: список статей
    """
    ua = UserAgent()
    response = requests.get(link, headers={'User-Agent': ua.chrome})
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all(class_='tm-articles-list__item')
    write_articles = []

    for article in articles:
        preview_inf = article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
        if preview_inf is None:
            preview_inf = article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-1')
        for keyword in words:
            if keyword in preview_inf.text:
                date = article.find(class_='tm-article-snippet__datetime-published')
                heading = article.find(class_='tm-article-snippet__title-link')
                link = article.find(class_='tm-article-snippet__title-link').attrs['href']
                write_article = f'{date.text} - {heading.text} - https://habr.com{link}'
                if write_article not in write_articles:
                    write_articles.append(write_article)
    pprint(write_articles)
    return



def get_article_full_text(link, words):
    """
    Функция вовзращает список статей с ключевыми словами в полном тексте статьи
    :param link: Ссылка на ресурс
    :param words: Ключевые слова для поиска
    :return: Список статей
    """
    ua = UserAgent()
    response = requests.get(link, headers={'User-Agent': ua.chrome})
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all(class_='tm-articles-list__item')
    write_articles = []
    for article in articles:
        link = article.find(class_='tm-article-snippet__title-link').attrs['href']
        article_link = f'https://habr.com{link}'
        res = requests.get(article_link, headers={'User-Agent': ua.chrome})
        text_article = res.text
        sp = bs4.BeautifulSoup(text_article, features='html.parser')
        article_text = sp.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
        if article_text is None:
            article_text = sp.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-1')
        for keyword in words:
            if keyword in article_text.text:
                date = article.find(class_='tm-article-snippet__datetime-published')
                heading = article.find(class_='tm-article-snippet__title-link')
                link = article.find(class_='tm-article-snippet__title-link').attrs['href']
                write_article = f'{date.text} - {heading.text} - https://habr.com{link}'
                if write_article not in write_articles:
                    write_articles.append(write_article)
    pprint(write_articles)
    return

if __name__ == '__main__':
    url = 'https://habr.com/ru/all/'
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    get_article_full_text(url, KEYWORDS)
    get_need_article(url, KEYWORDS)