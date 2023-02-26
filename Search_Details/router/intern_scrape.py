from fastapi import APIRouter
from ..loggings import logger
from bs4 import BeautifulSoup
import requests

router = APIRouter(
    tags=['Internships']
)

@router.get('/Internships')
def intern_scrape():
    logger.info("getting the intern page")
    url = requests.get('https://internshala.com/internships/work-from-home-internships/').text
    soup = BeautifulSoup(url,'lxml')
    
    logger.info("base of intern page")
    containers = soup.find_all('div', class_= 'container-fluid individual_internship visibilityTrackerItem')
    
    logger.info("fetching the intern page")
    for index,container in enumerate(containers):
        company_name = container.find('h4', class_ ='heading_6 company_name').text.replace(' ','')
        position = container.find('h3',class_ ='heading_4_5 profile').text
        location = container.find('a', class_ ='location_link view_detail_button').text
        published = container.find('div', class_ ='status-container').text
        more_info=container.div.h3.a['href']
        if 'Few' in published:
            return {f'''
                    Company name:{company_name}\n
                    Position:{position}\n
                    Location:{location}\n
                    published on:{published}\n
                    More info:{more_info}\n\n
                    '''}