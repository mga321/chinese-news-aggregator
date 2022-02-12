import scrapy
import datetime


class ChinaDailySpider(scrapy.Spider):
    name = 'china_daily'
    start_urls = ['https://www.chinadaily.com.cn/world/china-us']
    allowed_domains = ['chinadaily.com.cn']

    def parse(self, response):
        """Tertiary section is the list of all other articles below the primary and secondary sections."""
        
        todays_date_string = datetime.datetime.today().strftime('%Y-%m-%d')  # Create a variable with today's date in str format
        articles = response.css('div.mb10.tw3_01_2')  # Create a subset of data containing all articles from the response

        for article in articles:  # For each article in articles response subset
            if article.css('b::text').get()[:10] == todays_date_string:
                yield {
                    'date': articles.css('b::text').get()[:10],
                    'link': articles.css('a').attrib['href']
                }
