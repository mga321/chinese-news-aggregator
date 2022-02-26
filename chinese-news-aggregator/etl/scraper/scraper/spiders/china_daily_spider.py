import scrapy
import datetime


# Get the current date in string format
todays_date_string = datetime.datetime.today().strftime('%Y-%m-%d')


class ChinaDailySpider(scrapy.Spider):
    name = 'china_daily'
    start_urls = ['https://www.chinadaily.com.cn/world/china-us']
    allowed_domains = ['chinadaily.com.cn']


    def parse(self, response):
        """This method parses through the list of articles on the main page of the "China-US" section where all
        articles in this category are listed. It finds all articles with the current date and returns a response object
        by following the url of each article. It then passes the response object for each article url into the parse_article_content method."""

        articles = response.css('div.mb10.tw3_01_2')  # Create a subset of data containing all articles from the response

        for article in articles:  # For each article in articles response object
            if article.css('b::text').get()[:10] == todays_date_string:  # Check if the date of the article is today's date

                yield response.follow(article.css('a').attrib['href'], callback=self.parse_article_content)
    

    def parse_article_content(self, response):
        """This function parses the response object yielded by the original parse method and yields the required data in a dictionary."""
        
        current_url = response.request.url  # Store the response object's url attribute in a variable
        article_content = response.css('div.lft_art')  # Create a subset of the data contianing all of the relevant article data

        yield {
            'date': todays_date_string,
            'article_link': current_url,
            'title': article_content.css('h1::text').get(),
            'author': article_content.css('span.info_l::text').get(),
            'location': article_content.css('span.info_l::text').get(),
            'body': article_content.css('p').getall()
        }