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
api = []

api_link_prefix = 'https://mapi.yummly.com/mapi/v19/content/search?solr.seo_boost=new&'
api_link_postfix = '&ignore-taste-pref%3F=true&start=0&maxResult=1000&fetchUserCollections=false&allowedContent=single_recipe&allowedContent=suggested_search&allowedContent=related_search&allowedContent=article&allowedContent=video&allowedContent=generic_cta&guided-search=true&solr.view_type=search_internal'
for recipe in YUMMLY:
    print(f'extracting link: {recipe}')
    
    html = requests.get(recipe, headers=headers, timeout=30)
    response = Selector(text=html.text)
    for link in response.xpath('//*[@class="all-yum-link primary-teal font-bold desktop"]/@href').extract():
        q = str(link).replace('/recipes?', '').replace(' ', '%20')
        api.append(f'{api_link_prefix}{q}{api_link_postfix}')
        
        
with open('yummly_api_calls.json', 'w') as fp:
    json.dump(api, fp, indent=6)
    
# for link in api:
#     html = requests.get(link, headers=headers, timeout=30)
#     recipes = json.loads(html.text)
#     for item in recipes.get('feed', []):
#         url = "https://www.yummly.com/" + str(item.get("tracking-id")).replace(' ', '%20')
#         urls.append(url)
    
# with open('yummly_all_links.json', 'w') as fp:
#     json.dump(urls, fp, indent=6)   

data = {}

for link in api:
    html = requests.get(link, headers=headers, timeout=30)
    recipes = json.loads(html.text)
    for item in recipes.get('feed', []):
        content = item.get("content")
        data['name'] = content.get('details').get('name')
        data['totalTime'] = content.get('details').get('totalTime')
        data['rating'] = content.get('details').get('rating')
        data['category'] = content.get('tags').get('course')[0].get('display-name') if 'course' in content.get('tags').keys() else None
        data['cuisine'] = content.get('tags').get('cuisine')[0].get('display-name') if 'cuisine' in content.get('tags').keys() else None
        data['tags'] = [{key: [x.get('display-name') for x in value]} for key, value in content.get('tags').items()]
        data['IngredientsWithAmount'] = [ingredient.get('wholeLine') for ingredient in content.get('ingredientLines')]
        data['Ingredients'] = [ingredient.get('ingredient') for ingredient in content.get('ingredientLines')] 
        
        
        
        

# for recipe in YUMMLY:
#     print(f'extracting link: {recipe}')
    
#     html = requests.get(recipe, headers=headers, timeout=30)
#     response = Selector(text=html.text)
#     for link in response.xpath('//*[@class="all-yum-link primary-teal font-bold desktop"]/@href').extract():
#         search_urls.append('https://yummly.com' + str(link).replace(' ', '%20'))
#         print(link)
        
# with open('yummly_searches.json', 'w') as fp:
#     json.dump(search_urls, fp, indent=6)
    
# for search in search_urls:
#     html = requests.get(search, headers=headers, timeout=30)
#     response = Selector(text=html.text)
#     for url in response.xpath('//*[@class="link-overlay"]/@href').extract():
#         urls.append('https://yummly.com' + str(url).replace(' ', '%20'))
#         print(url)
    
# with open('yummly_links.json', 'w') as fp:
#     json.dump(urls, fp, indent=6)