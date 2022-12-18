import json
import requests
from parsel import Selector

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36 '
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
    'https://www.yummly.com/cuisines/hawaiian',
    'https://www.yummly.com/cuisines/thai',
    'https://www.yummly.com/cuisines/indian',
    'https://www.yummly.com/cuisines/spanish',
    'https://www.yummly.com/cuisines/korean',
    'https://www.yummly.com/cuisines/moroccan',
    'https://www.yummly.com/cuisines/british',
    'https://www.yummly.com/cuisines/irish',
    'https://www.yummly.com/cuisines/russian',
    'https://www.yummly.com/cuisines/brazilian',
    'https://www.yummly.com/cuisines/german',
    'https://www.yummly.com/cuisines/ethiopian',
    'https://www.yummly.com/cuisines/soul-food',
    'https://www.yummly.com/cuisines/cuban',
    'https://www.yummly.com/cuisines/swedish',
    'https://www.yummly.com/cuisines/hungarian',
    'https://www.yummly.com/cuisines/portuguese',
    ]


search_urls = []
urls = []
api = []

"""
Extracting links TODO: infinite scrolling
"""
# for recipe in YUMMLY:
#     print(f'extracting link: {recipe}')
    
#     html = requests.get(recipe, headers=headers, timeout=30)
#     response = Selector(text=html.text)
#     for link in response.xpath('//*[@class="all-yum-link primary-teal font-bold desktop"]/@href').extract():
#         search_urls.append('https://yummly.com' + str(link).replace(' ', '%20'))
#         print(link)
    
# for search in search_urls:
#     html = requests.get(search, headers=headers, timeout=30)
#     response = Selector(text=html.text)
#     for url in response.xpath('//*[@class="link-overlay"]/@href').extract():
#         urls.append('https://yummly.com' + str(url).replace(' ', '%20'))
#         print(url)
    
# with open('yummly_links.json', 'w') as fp:
#     json.dump(urls, fp, indent=6)
    
"""
Extracting links infinite scrolling included using api calls
"""
print('extracting links')
api_link_prefix = 'https://mapi.yummly.com/mapi/v19/content/search?solr.seo_boost=new&'
api_link_postfix = '&ignore-taste-pref%3F=true&start=0&maxResult=1000&fetchUserCollections=false&allowedContent=single_recipe&allowedContent=suggested_search&allowedContent=related_search&allowedContent=article&allowedContent=video&allowedContent=generic_cta&guided-search=true&solr.view_type=search_internal'

for recipe in YUMMLY:
    print(f'extracting link: {recipe}')
    
    html = requests.get(recipe, headers=headers, timeout=30)
    response = Selector(text=html.text)
    for link in response.xpath('//*[@class="all-yum-link primary-teal font-bold desktop"]/@href').extract():
        q = str(link).replace('/recipes?', '').replace(' ', '%20')
        api.append(f'{api_link_prefix}{q}{api_link_postfix}')

api.append(f'{api_link_prefix}q=italian{api_link_postfix}')
api.append(f'{api_link_prefix}q=mexican{api_link_postfix}')
api.append(f'{api_link_prefix}q=southern+%26+soul+food{api_link_postfix}')
api.append(f'{api_link_prefix}q=indian{api_link_postfix}')
api.append(f'{api_link_prefix}q=chinese{api_link_postfix}')
api.append(f'{api_link_prefix}q=french{api_link_postfix}')
api.append(f'{api_link_prefix}q=thai{api_link_postfix}')
api.append(f'{api_link_prefix}q=japanese{api_link_postfix}')
api.append(f'{api_link_prefix}q=greek{api_link_postfix}')
api.append(f'{api_link_prefix}q=spanish{api_link_postfix}')
api.append(f'{api_link_prefix}q=korean{api_link_postfix}')
api.append(f'{api_link_prefix}q=vietnamese{api_link_postfix}')
api.append(f'{api_link_prefix}q=moroccan{api_link_postfix}')
api.append(f'{api_link_prefix}q=british{api_link_postfix}')
api.append(f'{api_link_prefix}q=filipino{api_link_postfix}')
api.append(f'{api_link_prefix}q=irish{api_link_postfix}')
api.append(f'{api_link_prefix}q=jamaican{api_link_postfix}')
api.append(f'{api_link_prefix}q=russian{api_link_postfix}')
api.append(f'{api_link_prefix}q=brazilian{api_link_postfix}')
api.append(f'{api_link_prefix}q=german{api_link_postfix}')
api.append(f'{api_link_prefix}q=turkish{api_link_postfix}')
api.append(f'{api_link_prefix}q=swedish{api_link_postfix}')
api.append(f'{api_link_prefix}q=portuguese{api_link_postfix}')

with open('./yummly_api_links.json', 'w') as fp:
    json.dump(api, fp, indent=6)
# for link in api:
#     html = requests.get(link, headers=headers, timeout=30)
#     recipes = json.loads(html.text)
#     for item in recipes.get('feed', []):
#         url = "https://www.yummly.com/" + str(item.get("tracking-id")).replace(' ', '%20')
#         urls.append(url)
    
# with open('./yummly_all_links.json', 'w') as fp:
#     json.dump(urls, fp, indent=6)
