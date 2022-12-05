import json
import requests
from parsel import Selector

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

YUMMLY = [
    'https://www.yummly.com/cuisines/asian',
    'https://www.yummly.com/cuisines/chinese',
    'https://www.yummly.com/cuisines/mediterranean',
    'https://www.yummly.com/cuisines/italian',
    'https://www.yummly.com/cuisines/american',
    'https://www.yummly.com/cuisines/mexican',
    'https://www.yummly.com/cuisines/greek',
    'https://www.yummly.com/cuisines/vietnamese',
    'https://www.yummly.com/cuisines/african',
    'https://www.yummly.com/cuisines/french',
    'https://www.yummly.com/cuisines/japanese',
    'https://www.yummly.com/cuisines/hawaiian'
    ]


search_urls = []
urls = []
for recipe in YUMMLY:
    print(f'extracting link: {recipe}')
    
    html = requests.get(recipe, headers=headers, timeout=30)
    response = Selector(text=html.text)
    for link in response.xpath('//*[@class="all-yum-link primary-teal font-bold desktop"]/@href').extract():
        search_urls.append('https://yummly.com' + str(link).replace(' ', '%20'))
        print(link)
        
with open('yumly_searches.json', 'w') as fp:
    json.dump(search_urls, fp, indent=6)
    
for search in search_urls:
    html = requests.get(search, headers=headers, timeout=30)
    response = Selector(text=html.text)
    for url in response.xpath('//*[@class="link-overlay"]/@href').extract():
        urls.append('https://yummly.com' + str(url).replace(' ', '%20'))
        print(url)
    
with open('yumly_links.json', 'w') as fp:
    json.dump(urls, fp, indent=6)