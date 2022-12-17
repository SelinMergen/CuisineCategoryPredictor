"""
Scraping data faster using the data shared in api response
"""
import csv
import json

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36 '
}

with open('./yummly_all_links.json', 'r') as fp:
    api = json.load(fp)

api = list(dict.fromkeys(api))
print('extracting columns')
data = {}
with open('../../../datasets/yummly/recipes_from_api.csv', 'a', newline='') as csvfile:
    field_names = ['link', 'name', 'totalTime', 'rating', 'category', 'cuisine', 'tags', 'IngredientsWithAmount',
                   'Ingredients', 'NutritionValues']
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    for link in api:
        html = requests.get(link, headers=headers, timeout=30)
        if html.text:
            recipes = json.loads(html.text)
            for item in recipes.get('feed', []):
                content = item.get("content")
                data['link'] = f'https://www.yummly.com/{item.get("tracking-id")}'
                print(data['link'])
                data['name'] = content.get('details').get('name').strip()
                data['totalTime'] = content.get('details').get('totalTime').strip()
                data['rating'] = content.get('details').get('rating').strip()
                data['category'] = content.get('tags').get('course')[0].get(
                    'display-name').strip() if 'course' in content.get('tags').keys() and content.get('tags').get(
                    'course') else None
                data['cuisine'] = content.get('tags').get('cuisine')[0].get(
                    'display-name').strip() if 'cuisine' in content.get('tags').keys() else None
                data['tags'] = [{key: [x.get('display-name') for x in value]} for key, value in
                                content.get('tags').items()]
                data['IngredientsWithAmount'] = [
                    str(ingredient.get('wholeLine')).replace('unchecked', '').replace('▢', '')
                    for ingredient in content.get('ingredientLines')
                ]
                data['Ingredients'] = [''.join([i for i in ingredient.get('ingredient').strip() if not i.isdigit()])
                                       for ingredient in content.get('ingredientLines')]
                data['NutritionValues'] = {
                    str(x.get('attribute')): f'{x.get("value")}{x.get("unit").get("abbreviation")}' for x in
                    content.get('nutrition').get('nutritionEstimates')}
                writer.writerow(data)
        else:
            print("An error occured:", link)
