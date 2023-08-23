import scrapy

class codeForcesSpider(scrapy.Spider):
    name = "CodeForces"
    start_urls = [
        "https://codeforces.com/problemset"
    ]

    def parse(self, response):
        relevantPart = response.css("table.problems tbody tr").extract()

        for eachRow in relevantPart:
            name = relevantPart.css('.problems div:nth-child(1) a').extract()
            link = "https://codeforces.com/problemset"+eachRow.css('.problems div:nth-child(1) a').xpath("@href").extract()
            yield {
                "Name: ": name,
                "Link: ": link
            }