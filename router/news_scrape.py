from fastapi import APIRouter
from bs4 import BeautifulSoup
import requests
from ..Search_Details.loggings import logger

router = APIRouter(
    tags=['News']
)

@router.get('/News')
def news_scrape():
    
    logger.info("getting the news page")
    url = requests.get('http://www.inshorts.com/en/read/technology').text
    soup = BeautifulSoup(url,'lxml')
    
    logger.info("base of news page")
    newses=soup.find_all('div', class_='news-card z-depth-1')
    only=soup.find('div',class_='news-card-author-time news-card-author-time-in-content')
    
    logger.debug("fetching the news")
    for news in newses:
        hl=news.find('a', class_='clickable').text
        time=news.find('span',class_='time').text
        date=news.find('span',class_='date').text
        summary=news.find('div', class_='news-card-content news-right-box').text
        more_info=only.a['href']
        return [f'''
                {time} on {date}\n
                Headline:{hl}\n
                Summary:{summary}\n
                More Info{more_info}\n\n
                ''']        

