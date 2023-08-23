import scrapy
from ..items import ScrapecpItem
from scrapy.http import FormRequest

class hackerrankspider(scrapy.Spider):
    name = "HackerRank"
    start_urls = [
        "https://www.hackerrank.com/auth/login"
    ]


    def parse(self,response):
        token = response.css('form.form div.ui-tooltip-wrapper input::attr(value)').extract_first()
        
        return FormRequest.form_response(response, formdata={
            'Token_Value' : token,
            'username' : 'adwaith.mnambiar2021@vitstudent.ac.in',
            'password' : 'mic123'
        },callback = self.scrape)

    def scrape(self,response):
        items = ScrapecpItem()

        questionSet = response.css(".challenges-list .challenge").extract()

        for section in questionSet:
            Name = respone.css(".challenge-name h4::text").extract()
            Link = "https://www.hackerrank.com"+response.css("a.challenge-card-link::attr(href)").extract()
            items['Name'] = Name
            items['Link'] = Lame

            yield items