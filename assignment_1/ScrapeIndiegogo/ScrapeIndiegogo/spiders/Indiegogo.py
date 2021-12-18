import scrapy
from scrapy.crawler import CrawlerProcess


class IndiegogoSpider(scrapy.Spider):
    name = "Indiegogo"

    def start_requests(self):
        urls = [
            'https://www.indiegogo.com/explore/home',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kvargs):
        res = response.xpath('//div[@class="discoverableCard"]').extract()
        self.log("the link is: {}".format(res))
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


def main():
    process = CrawlerProcess({'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36'
                                            '(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
)
    process.crawl(IndiegogoSpider)
    process.start()


if __name__ == "__main__":
    main()
