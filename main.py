import requests
from time import sleep
from fake_headers import Headers
from bs4 import BeautifulSoup
from send_webhook import send_webhook


def get_article_url(soup):
    try:
        link = 'https://cointelegraph.com' + soup.find('article').find('a')['href']
        return link
    except:
        return None


def get_title(soup):
    try:
        title = soup.find('span', class_='post-card__title')
        return title.text
    except:
        return None


def get_author_and_url(soup):
    try:
        author = soup.find('a', class_='post-card__author-link')
        author_name = author.text
        return author_name
    except:
        return None


def get_description(soup):
    try:
        description = soup.find('p', class_='post-card__text').text
        return description
    except:
        return None


def main():
    headers = Headers(os='win', headers=True).generate()
    url = 'https://cointelegraph.com/'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    urls = []

    if res:
        if soup.find('ul', class_='posts-listing__list'):
            news_list = soup.find('ul', class_='posts-listing__list')
            if news_list.find_all('li', {'class': 'posts-listing__item'}):
                news_list = news_list.find_all('li', {'class': 'posts-listing__item'})

                for item in news_list:
                    url = get_article_url(item)
                    title = get_title(item)
                    author_name = get_author_and_url(item)
                    description = get_description(item)
                    if url and title and author_name and description:
                        if url not in urls:
                            urls.append(url)
                            send_webhook(url, description, title, author_name)
                            sleep(1)

        return False


if __name__ == '__main__':
    while not main():
        main()
        sleep(1)
