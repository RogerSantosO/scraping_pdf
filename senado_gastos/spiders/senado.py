import scrapy
from scrapy.loader import ItemLoader
from senado_gastos.items import SenadoGastosItem

class SenadoSpider(scrapy.Spider):
    name = 'senado'
    allowed_domains = ['www12.senado.leg.br']
    start_urls = ['https://www12.senado.leg.br/transparencia/sen/gastos-com-correspondencias']

    def parse(self, response):
        for link in response.xpath("//following::a[@class='internal-link'][contains(@href,'pdf')]"):
            loader = ItemLoader(item=SenadoGastosItem(), selector=link)
                        
            gasto_relative = link.xpath('.//@href').extract_first()
            gasto = response.urljoin(gasto_relative)
                
            loader.add_value('file_urls',gasto)
            yield loader.load_item()