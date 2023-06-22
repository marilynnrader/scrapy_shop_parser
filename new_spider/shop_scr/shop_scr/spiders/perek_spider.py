import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#https://www.perekrestok.ru/cat/mc/148/ovosi-frukty-griby
#https://www.perekrestok.ru/cat/c/710/popkorn
#product-card__link-text

class PerekSpider(CrawlSpider):
    name = 'perek'
    start_urls = ['https://www.perekrestok.ru/cat']
    rules = (
        Rule(LinkExtractor(allow=('cat/mc/')), follow=True),
        Rule(LinkExtractor(allow=('cat/c/774')), follow=True),
        Rule(LinkExtractor(allow=('774/p/')), callback='parse_items', follow=True),
    )

    def parse_items(self, response):
        perek_list2 = ['Чипсы кукурузные Carambas бекон, 150г', 'Чипсы кукурузные Carambas Original, 150г']
        if response.css('h1.sc-fubCzh.ibFUIH.product__title::text').get() in perek_list2:
            yield{
                'name':response.css('h1.sc-fubCzh.ibFUIH.product__title::text').get(),
                'price':response.css('div.price-new::text').get().split()[0]
                }


        
