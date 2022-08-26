links=[]

i=0

class WikiScrapeSpider(scrapy.Spider):
    name = 'wiki_scrape'
    #allowed_domains = ['www.wikipedia.org']
    start_urls = [links[i], links[i]]
    def parse(self, response):
        datas = response.xpath('//p').extract()
        for item in datas:
            all_items = {
                'datas' : BeautifulSoup(item).text
            }
            yield all_items

process = CrawlerProcess(settings={
    "FEEDS": {
        "scrapped_data.txt": {"format": "json"},
    },
})
process.crawl(WikiScrapeSpider)
process.start()
    

    
    