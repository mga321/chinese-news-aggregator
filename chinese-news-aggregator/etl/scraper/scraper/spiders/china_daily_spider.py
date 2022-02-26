import scrapy
import datetime


todays_date_string = datetime.datetime.today().strftime('%Y-%m-%d')


class ChinaDailySpider(scrapy.Spider):
    name = 'china_daily'
    start_urls = ['https://www.chinadaily.com.cn/world/china-us']
    allowed_domains = ['chinadaily.com.cn']


    def parse(self, response):
        """Define the primary, secondary, and tertiary sections as well as the functionality here."""

        articles = response.css('div.mb10.tw3_01_2')  # Create a subset of data containing all articles from the response

        for article in articles:  # For each article in articles response subset
            if article.css('b::text').get()[:10] == todays_date_string:  # If the date of the article is today's date

                yield response.follow(article.css('a').attrib['href'], callback=self.parse_article_content)
    

    def parse_article_content(self, response):
        """Documentation here."""
        
        current_url = response.request.url
        article_content = response.css('div.lft_art')

        yield {
            'date': todays_date_string,
            'article_link': current_url,
            'title': article_content.css('h1::text').get(),
            'author': article_content.css('span.info_l::text').get(),
            'location': article_content.css('span.info_l::text').get(),
            'body': article_content.css('p').getall()
        }