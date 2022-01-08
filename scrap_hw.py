import requests
import bs4
from bs4 import BeautifulSoup
from pprint import pp, pprint

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'If-None-Match': 'W/"34944-ayAqoXXLWyp1TZjkezR2mGMcYmo"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
KEYWORDS = {'Системное администрирование', 'Изучение языков', 'Звук', 'python'}




if __name__ == '__main__':
    
    response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
    text = response.text
    
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article', class_='tm-articles-list__item')

    
    
    for article in articles:
        
        tags = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
        tags = set(tag.find('span').text for tag in tags)
        time = article.find('time')
        date = time ['datetime']
        
        title = article.find('a', class_='tm-article-snippet__title-link')
        clear_title = title.find('span').text
        
        href = title['href']
        link = 'https://habr.com'+href
        
        response_2 = requests.get(link, headers=HEADERS)
        text = response_2.text
        soup = bs4.BeautifulSoup(text, features='html.parser')
           
        if KEYWORDS  & tags:
            print(date, clear_title, link)
            
            for key in KEYWORDS:
                article_inner = soup.find(string=key)
                
                if article_inner in KEYWORDS:
                    print(f'Поиск по статье {link}\n')
                    print('---------')
            
            
        
        
            
    