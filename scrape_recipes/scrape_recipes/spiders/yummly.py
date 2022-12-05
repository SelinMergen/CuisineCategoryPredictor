import json
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request


class YummlySpider(scrapy.Spider):
    name = 'yummly'
    allowed_domains = ['yummly.com']
    start_urls = [
        "https://yummly.com/recipes?q=Best%20Asian",
        "https://yummly.com/recipes?q=Easy%20Asian",
        "https://yummly.com/recipes?q=Healthy%20Asian",
        "https://yummly.com/recipes?q=Stir-Fry",
        "https://yummly.com/recipes?q=Chinese",
        "https://yummly.com/recipes?q=Thai",
        "https://yummly.com/recipes?q=Korean",
        "https://yummly.com/recipes?q=Asian%20Chicken",
        "https://yummly.com/recipes?q=Asian%20Noodle",
        "https://yummly.com/recipes?q=Asian%20Salad",
        "https://yummly.com/recipes?q=Asian%20Sauce",
        "https://yummly.com/recipes?q=Asian%20Pork",
        "https://yummly.com/recipes?q=Asian%20Salmon",
        "https://yummly.com/recipes?q=Asian",
        "https://yummly.com/recipes?q=Easy%20Chinese",
        "https://yummly.com/recipes?q=Healthy%20Chinese",
        "https://yummly.com/recipes?q=Chinese%20Chicken",
        "https://yummly.com/recipes?q=Chinese%20Beef",
        "https://yummly.com/recipes?q=Chinese%20Noodle",
        "https://yummly.com/recipes?q=Chinese%20Pork",
        "https://yummly.com/recipes?q=Fried%20Rice",
        "https://yummly.com/recipes?q=Chinese%20Green%20Bean",
        "https://yummly.com/recipes?q=Chinese%20Dumpling",
        "https://yummly.com/recipes?q=Chinese%20Soup",
        "https://yummly.com/recipes?q=Orange%20Chicken",
        "https://yummly.com/recipes?q=Broccoli%20&%20Beef",
        "https://yummly.com/recipes?q=Chinese",
        "https://yummly.com/recipes?q=Best%20Mediterranean",
        "https://yummly.com/recipes?q=Easy%20Mediterranean",
        "https://yummly.com/recipes?q=Healthy%20Mediterranean",
        "https://yummly.com/recipes?q=Shawarma",
        "https://yummly.com/recipes?q=Hummus",
        "https://yummly.com/recipes?q=Falafel",
        "https://yummly.com/recipes?q=Kofta",
        "https://yummly.com/recipes?q=Couscous",
        "https://yummly.com/recipes?q=Mediterranean%20Chicken",
        "https://yummly.com/recipes?q=Mediterranean%20Lamb",
        "https://yummly.com/recipes?q=Mediterranean%20Beef",
        "https://yummly.com/recipes?q=Mediterranean%20Fish",
        "https://yummly.com/recipes?q=Mediterranean%20Salmon",
        "https://yummly.com/recipes?q=Mediterranean%20Salad",
        "https://yummly.com/recipes?q=Mediterranean%20Side%20Dish",
        "https://yummly.com/recipes?q=Mediterranean%20Lunch",
        "https://yummly.com/recipes?q=Mediterranean",
        "https://yummly.com/recipes?q=Best%20Italian",
        "https://yummly.com/recipes?q=Easy%20Italian",
        "https://yummly.com/recipes?q=Healthy%20Italian",
        "https://yummly.com/recipes?q=Italian%20Pasta",
        "https://yummly.com/recipes?q=Italian%20Chicken",
        "https://yummly.com/recipes?q=Pizza",
        "https://yummly.com/recipes?q=Risotto",
        "https://yummly.com/recipes?q=Chicken%20Parmesan",
        "https://yummly.com/recipes?q=Lasagna",
        "https://yummly.com/recipes?q=Italian%20Meatballs",
        "https://yummly.com/recipes?q=Italian%20Dinner",
        "https://yummly.com/recipes?q=Italian%20Side%20Dish",
        "https://yummly.com/recipes?q=Italian%20Appetizer",
        "https://yummly.com/recipes?q=Italian%20Dessert",
        "https://yummly.com/recipes?q=Italian",
        "https://yummly.com/recipes?q=Best%20American",
        "https://yummly.com/recipes?q=Easy%20American",
        "https://yummly.com/recipes?q=Healthy%20American",
        "https://yummly.com/recipes?q=Hamburger",
        "https://yummly.com/recipes?q=Ground%20Beef",
        "https://yummly.com/recipes?q=Casserole",
        "https://yummly.com/recipes?q=Fried%20Chicken",
        "https://yummly.com/recipes?q=Cake",
        "https://yummly.com/recipes?q=Cookie",
        "https://yummly.com/recipes?q=Pie",
        "https://yummly.com/recipes?q=Chili",
        "https://yummly.com/recipes?q=Pancake",
        "https://yummly.com/recipes?q=Cheese",
        "https://yummly.com/recipes?q=American",
        "https://yummly.com/recipes?q=Best%20Mexican",
        "https://yummly.com/recipes?q=Easy%20Mexican",
        "https://yummly.com/recipes?q=Healthy%20Mexican",
        "https://yummly.com/recipes?q=Mexican%20Chicken",
        "https://yummly.com/recipes?q=Mexican%20Beef",
        "https://yummly.com/recipes?q=Enchilada",
        "https://yummly.com/recipes?q=Taco",
        "https://yummly.com/recipes?q=Burrito",
        "https://yummly.com/recipes?q=Fajitas",
        "https://yummly.com/recipes?q=Quesadilla",
        "https://yummly.com/recipes?q=Mexican%20Casserole",
        "https://yummly.com/recipes?q=Slow%20Cooker%20Mexican",
        "https://yummly.com/recipes?q=Mexican%20Dessert",
        "https://yummly.com/recipes?q=Mexican%20Side%20Dish",
        "https://yummly.com/recipes?q=Mexican%20Soup",
        "https://yummly.com/recipes?q=Mexican%20Rice",
        "https://yummly.com/recipes?q=Mexican",
        "https://yummly.com/recipes?q=Best%20Greek",
        "https://yummly.com/recipes?q=Easy%20Greek",
        "https://yummly.com/recipes?q=Healthy%20Greek",
        "https://yummly.com/recipes?q=Greek%20Salad",
        "https://yummly.com/recipes?q=Greek%20Gyro",
        "https://yummly.com/recipes?q=Tzatziki%20Sauce",
        "https://yummly.com/recipes?q=Hummus",
        "https://yummly.com/recipes?q=Souvlaki",
        "https://yummly.com/recipes?q=Halloumi",
        "https://yummly.com/recipes?q=Moussaka",
        "https://yummly.com/recipes?q=Greek%20Chicken",
        "https://yummly.com/recipes?q=Greek%20Pasta",
        "https://yummly.com/recipes?q=Greek%20Lamb",
        "https://yummly.com/recipes?q=Greek",
        "https://yummly.com/recipes?q=Easy%20Vietnamese",
        "https://yummly.com/recipes?q=Healthy%20Vietnamese",
        "https://yummly.com/recipes?q=Spring%20Roll",
        "https://yummly.com/recipes?q=Pho",
        "https://yummly.com/recipes?q=Vietnamese%20Rice%20Noodle",
        "https://yummly.com/recipes?q=Vietnamese%20Chicken",
        "https://yummly.com/recipes?q=Vietnamese%20Beef",
        "https://yummly.com/recipes?q=Vietnamese%20Pork",
        "https://yummly.com/recipes?q=Vietnamese%20Shrimp",
        "https://yummly.com/recipes?q=Vietnamese%20Soup",
        "https://yummly.com/recipes?q=Banh%20Mi",
        "https://yummly.com/recipes?q=Vietnamese",
        "https://yummly.com/recipes?q=best+african",
        "https://yummly.com/recipes?q=healthy+african",
        "https://yummly.com/recipes?q=west+african",
        "https://yummly.com/recipes?q=south+african",
        "https://yummly.com/recipes?q=north+african",
        "https://yummly.com/recipes?q=east+african",
        "https://yummly.com/recipes?q=ethiopian",
        "https://yummly.com/recipes?q=shawarma",
        "https://yummly.com/recipes?q=tajine",
        "https://yummly.com/recipes?q=couscous",
        "https://yummly.com/recipes?q=shakshouka",
        "https://yummly.com/recipes?q=fufu",
        "https://yummly.com/recipes?q=jollof+rice",
        "https://yummly.com/recipes?q=pastilla",
        "https://yummly.com/recipes?q=Best%20French",
        "https://yummly.com/recipes?q=Easy%20French",
        "https://yummly.com/recipes?q=Healthy%20French",
        "https://yummly.com/recipes?q=Ratatouille",
        "https://yummly.com/recipes?q=Beef%20Bourguinon",
        "https://yummly.com/recipes?q=Coq%20Au%20Vin",
        "https://yummly.com/recipes?q=Chateaubriand",
        "https://yummly.com/recipes?q=Chicken%20Provencal",
        "https://yummly.com/recipes?q=Croque%20Monsieur",
        "https://yummly.com/recipes?q=Croque%20Madame",
        "https://yummly.com/recipes?q=French%20Onion%20Soup",
        "https://yummly.com/recipes?q=Chicken%20Cordon%20Bleu",
        "https://yummly.com/recipes?q=Macaroon",
        "https://yummly.com/recipes?q=French%20Chicken",
        "https://yummly.com/recipes?q=Creme%20Brulee",
        "https://yummly.com/recipes?q=French",
        "https://yummly.com/recipes?q=Easy%20Japanese",
        "https://yummly.com/recipes?q=Healthy%20Japanese",
        "https://yummly.com/recipes?q=Sushi",
        "https://yummly.com/recipes?q=Japanese%20Chicken",
        "https://yummly.com/recipes?q=Japanese%20Beef",
        "https://yummly.com/recipes?q=Japanese%20Pork",
        "https://yummly.com/recipes?q=Japanese%20Curry",
        "https://yummly.com/recipes?q=Japanese%20Soup",
        "https://yummly.com/recipes?q=Japanese%20Lunch",
        "https://yummly.com/recipes?q=Japanese%20Dinner",
        "https://yummly.com/recipes?q=Japanese%20Breakfast",
        "https://yummly.com/recipes?q=Japanese%20Rice",
        "https://yummly.com/recipes?q=Okonomiyaki",
        "https://yummly.com/recipes?q=Japanese",
        "https://yummly.com/recipes?q=Best%20Hawaiian",
        "https://yummly.com/recipes?q=Easy%20Hawaiian",
        "https://yummly.com/recipes?q=Healthy%20Hawaiian",
        "https://yummly.com/recipes?q=Huli%20Huli%20Chicken",
        "https://yummly.com/recipes?q=Kalua%20Pig",
        "https://yummly.com/recipes?q=Poke",
        "https://yummly.com/recipes?q=Spam",
        "https://yummly.com/recipes?q=Hawaiian%20Bread",
        "https://yummly.com/recipes?q=Hawaiian%20Main%20Dish",
        "https://yummly.com/recipes?q=Hawaiian%20Appetizer",
        "https://yummly.com/recipes?q=Vegan%20Hawaiian",
        "https://yummly.com/recipes?q=Slow%20Cooker%20Hawaiian",
        "https://yummly.com/recipes?q=Instant%20Pot%20Hawaiian",
        "https://yummly.com/recipes?q=Hawaiian"
    ]
    
    custom_settings = {
        'LOG_LEVEL' : 'INFO',
        'JOBDIR' : 'jobs/yummly-1'
    }
    
    rules = (
        Rule(LinkExtractor(allow=r'recipes/'), callback='parse', follow=True),
        Rule(LinkExtractor(allow=r'recipe/'), callback='parse_recipe', follow=True),
    )

    def parse(self, response):
        for url in response.xpath('//*[@class="link-overlay"]/@href').extract():
            url=response.urljoin(url)
            yield Request(url, callback=self.parse_recipe, meta={'href':url})

    def parse_recipe(self, response):
        item = {}
        result = {}
        self.logger.info("Code: " + str(response.status) + " Parsing: " + response.url)
        try:
            item = response.css('div.structured-data-info script::text').getall()[0]
            item = json.loads(item)
        except:
            self.logger.warning("Unable to get recipe from: " + response.url)
            pass
        
        result['title'] = item['name'] if 'name' in item.keys() else response.xpath('//*[@class="recipe-title font-bold h2-text primary-dark"]/text()').extract()
        result['nutrition'] = item['nutrition'] if 'nutrition' in item.keys() else None
        result['rating'] = item['aggregateRating']['ratingValue'] if 'aggregateRating' in item.keys() else None
        result['ratingCount'] = item['aggregateRating']['reviewCount'] if 'aggregateRating' in item.keys() else None
        result['category'] = item['recipeCategory'] if 'recipeCategory' in item.keys() else None
        result['keywords'] = item['keywords'] if 'keywords' in item.keys() else None
        result['ingredients'] = item['recipeIngredient'] if 'recipeIngredient' in item.keys() else None
        result['link'] = response.url
        result['cuisine'] = item['recipeCuisine'] if 'recipeCuisine' in item.keys() else None
        result['totalTime'] = item['totalTime'] if 'totalTime' in item.keys() else None
        
        yield result
