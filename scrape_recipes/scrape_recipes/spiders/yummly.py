import json
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

def read_urls():
    data = []
    with open('yummly/yummly_all_links.json', 'r') as fp:
        data = json.load(fp)
    return data

class YummlySpider(scrapy.Spider):
    name = 'yummly'
    allowed_domains = ['yummly.com']
    start_urls = read_urls()
    
    custom_settings = {
        'LOG_LEVEL' : 'INFO',
        'JOBDIR' : 'jobs/yummly-1'
    }
    
    # rules = (
    #     # Rule(LinkExtractor(allow=r'recipes/'), callback='parse', follow=True),
    #     Rule(LinkExtractor(allow=r'recipe/'), callback='parse_recipe', follow=True),
    # )

    # def parse(self, response):
    #     for url in response.xpath('//*[@class="link-overlay"]/@href').extract():
    #         url=response.urljoin(url)
    #         yield Request(url, callback=self.parse_recipe, meta={'href':url})

    def parse(self, response):
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
