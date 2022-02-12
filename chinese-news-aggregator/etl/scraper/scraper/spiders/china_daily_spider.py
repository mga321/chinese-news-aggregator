import scrapy
import datetime
from scraper.items import ScraperItem


class ChinaDailySpider(scrapy.Spider):
    name = 'china_daily'
    start_urls = ['https://www.chinadaily.com.cn/world/china-us']
    allowed_domains = ['chinadaily.com.cn']

    def parse(self, response):
        """Define the primary, secondary, and tertiary sections as well as the functionality here."""
        item = ScraperItem()

        todays_date_string = datetime.datetime.today().strftime('%Y-%m-%d')  # Create a variable with today's date in str format
        articles = response.css('div.mb10.tw3_01_2')  # Create a subset of data containing all articles from the response

        for article in articles:  # For each article in articles response subset
            if article.css('b::text').get()[:10] == todays_date_string:  # If the date of the article is today's date
                item['date'] = todays_date_string  # Store the date in a ScraperItem () instance
                item['article_page_link'] = article.css('a').attrib['href']  # Store the date and link in a ScraperItem () instance
            else:
                break
             
            yield item
        
        

            #     item['date'] = articles.css('b::text').get()[:10]
            #     item['link'] = articles.css('a').attrib['href']
            # else:
            #     break
            
            # yield item
