import scrapy
import datetime
# from scraper.items import ScraperItem
# from scrapy.exporters import JsonItemExporter

todays_date_string = datetime.datetime.today().strftime('%Y-%m-%d')

class ChinaDailySpider(scrapy.Spider):
    name = 'scrapy_test'
    start_urls = ['https://www.chinadaily.com.cn/world/china-us']
    allowed_domains = ['chinadaily.com.cn']


    def parse(self, response):
        """Define the primary, secondary, and tertiary sections as well as the functionality here."""

        # todays_date_string = datetime.datetime.today().strftime('%Y-%m-%d')  # Create a variable with today's date in str format
        articles = response.css('div.mb10.tw3_01_2')  # Create a subset of data containing all articles from the response

        for article in articles:  # For each article in articles response subset
            if article.css('b::text').get()[:10] == todays_date_string:  # If the date of the article is today's date

                yield response.follow(article.css('a').attrib['href'], callback=self.parse_article_content)
    

    def parse_article_content(self, response):
        all_content = response.css('div.lft_art')

        yield {
            'date': todays_date_string,
            # 'article_link': 
            'title': all_content.css('h1::text').get(),
            'author': all_content.css('span.info_l::text').get().split('|')[0],
            'content': all_content.css('p::text').getall()            
        }