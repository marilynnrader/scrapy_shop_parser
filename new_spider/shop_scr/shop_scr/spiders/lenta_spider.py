import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class LavkaSpider(CrawlSpider):
    name = 'lavka'
    start_urls = ['https://lavka.yandex.ru/']
    rules = (
        #Rule(LinkExtractor(allow=('_i_zelen/pomidory', '_i_zelen/ogurcy'), deny='/213/good/'), follow = True),
        Rule(LinkExtractor(allow='/213/good/'), follow = True,
        callback='parse_items'),
    )

    def parse_items(self, response):
        
        lavka_list = ['Крупа гречневая «Мистраль» ядрица', 'Рис Кубань «Мистраль» круглозёрный', 'Морковь',
        'Картофель белый ранний', 'Макароны Перья Makfa', 'Масло подсолнечное «Благо» рафинированное',
        'Маргарин сливочный 60% «Добавкин»', 'Молоко 3,4-4,5% «Домик в деревне» пастеризованное отборное',
        'Мука пшеничная Makfa высший сорт', 'Лопатка говяжья','Огурцы средние гладкие', 'Помидоры розовые', 
        'Форель радужная потрошеная с головой','Сахар-песок «Русский»', 'Соль «Илецкая» помол №1',
        'Сыр «Брест-Литовск» классический 45%', 'Печенье Традиционное «Юбилейное»',
        'Батон нарезной «Черёмушки» нарезка', 'Чай чёрный Kenyan Sunrise Greenfield в пакетиках',
        'Яблоки сезонные', 'Яйцо куриное С1 «Из Лавки»']
        
        if response.css('h1.t5c3shz.t18stym3.hbhlhv.bdxkmhu.b1k6fkc9.n1wpn6v7.l14lhr1r::text').get() in lavka_list:
            yield{
                'name':response.css('h1.t5c3shz.t18stym3.hbhlhv.bdxkmhu.b1k6fkc9.n1wpn6v7.l14lhr1r::text').get(),
                'price':response.css('span.ttz1v1m.t18stym3.t38p0ru.b1ba12f6.bkuxkry.t1wnuyqt.l14lhr1r::text').get().split()[0]
                }