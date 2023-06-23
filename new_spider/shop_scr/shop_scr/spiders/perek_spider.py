import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PerekSpider(CrawlSpider):
    name = 'perek'
    start_urls = ['https://www.perekrestok.ru/cat']
    rules = (
        Rule(LinkExtractor(allow=('cat/mc/113/', 'cat/mc/148/', 'cat/mc/100/', 'cat/mc/187/', 'cat/mc/242/',
        'cat/mc/132/', 'cat/mc/79/'), 
        deny = ('/cat/mc/965/','/cat/mc/25/','/cat/mc/708/',
        '/cat/mc/205/', '/cat/mc/54/','/cat/mc/782/', '/cat/mc/793/', '/cat/mc/229/', '/cat/mc/217/',
        '/cat/mc/224/', '/cat/mc/168/', '/cat/mc/74/', '/cat/mc/64/', '/cat/mc/157/',
        '/cat/mc/108/', '/cat/mc/66/', '/cat/mc/84/', '/cat/mc/236/', '/cat/mc/162/',
        '/cat/mc/35/', '/cat/mc/1/', '/cat/mc/248/')), follow=True),
        Rule(LinkExtractor(allow=('cat/c/114', 'cat/c/122', 'cat/c/123', 'cat/c/121', 'cat/c/659', 
        'cat/c/150', 'cat/c/153', 'cat/c/105', 'cat/c/104', 'cat/c/107', 'cat/c/106', 'cat/c/101', 'cat/c/186', 'cat/c/176',
        'cat/c/243', 'cat/c/142', 'cat/c/82/', 'cat/c/83/')), follow=True),
        Rule(LinkExtractor(allow=('114/p/', '122/p/', '123/p/', '121/p/', '659/p/', '150/p/', '153/p/', '105/p/',
        '104/p/', '107/p/', '106/p/', '101/p/', '186/p/', '176/p/', '243/p/', '142/p/', '/82/p/', '/83/p/')), 
        callback='parse_items', follow=True),
    )

    def parse_items(self, response):
        
        perek_list = ['Гречка Мистраль, 900г', 'Рис Мистраль Кубань белый круглозёрный, 900г', 'Морковь отечественная',
        'Картофель ранний', 'Макароны Makfa улитки, 450г', 'Масло подсолнечное Золотая Семечка рафинированное, 1л',
        'Маргарин сливочный Хозяюшка Нижегородский 60%, 200г', 'Молоко ультрапастеризованное Домик в деревне 3.5%, 950мл',
        'Мука Makfa пшеничная высшего сорта, 1кг', 'Лопаточная часть говяжья Перекрёсток без кости',
        'Огурцы гладкие среднеплодные', 'Томаты Махитос красные', 'Форель радужная потрошеная с головой',
        'Сахар белый песок, 1кг', 'Соль поваренная пищевая крупная, 1кг',
        'Сыр полутвёрдый Брест-Литовск Классический 45%, 200г', 'Печенье Юбилейное Традиционное витаминизированное, 268г',
        'Батон Нарезной нарезка Маркет Перекрёсток, 400г', 'Чай Майский Корона Российской Империи чёрный в пакетиках, 25х2г',
        'Яблоки Гренни смит Маркет Перекрёсток', 'Яйцо куриное Окское столовое С1, 10шт']
        
        if response.css('h1.sc-fubCzh.ibFUIH.product__title::text').get() in perek_list:
            yield{
                'name':response.css('h1.sc-fubCzh.ibFUIH.product__title::text').get(),
                'price':response.css('div.price-new::text').get().split()[0]
                }


        
