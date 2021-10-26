from typing import List
import wikipedia, requests
from bs4 import BeautifulSoup

def get_img(url: str) -> str:
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')

    td = soup.find('td', {'class': "infobox-full-data"})

    image_url = td.find('a').find('img').get('src')
    img_url = f'https:{image_url}'
    return img_url
    
    
def wiki(keyword : str) -> dict:
    
    results = []

    # print(wikipedia.summary(search, sentences=2))
    page = wikipedia.page(keyword , auto_suggest=False)
    print(page)
    page_cont = page.content
    page_url = page.url
    try:
        img_url: str = get_img(page_url)
    except:
        img_url = None

    output = {}
    output['info'] = page_cont
    output['url'] = page_url
    output['img_url'] = img_url
    

    
    results.append(output)
    # print(page_image)
    return {'result' : results}
    