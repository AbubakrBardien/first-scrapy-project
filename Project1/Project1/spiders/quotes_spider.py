import scrapy  # type: ignore
from scrapy.http import FormRequest  # type: ignore
from ..items import Project1Item


class QuoteSpider(scrapy.Spider):
    name = "quotes"  # Don't change variable name

    # Don't change variable name
    start_urls = ["https://quotes.toscrape.com/login"]

    def parse(self, response):
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response, formdata={
            "csrf_token": token,
            "username": "AbubakrBardien",
            "password": "12345"
        }, callback=self.startScraping)

    def startScraping(self, response):
        items = Project1Item()

        all_div_quotes = response.css("div.quote")

        for quote_ in all_div_quotes:
            quote = quote_.css(".text::text").extract()
            author = quote_.css(".author::text").extract()
            tags = quote_.css(".tag::text").extract()

            items["quote"] = quote
            items["author"] = author
            items["tags"] = tags

            yield items

        nextPage = response.css("li.next a::attr(href)").get()

        # Basically allows scrapy to loop through the webpages (a method similar to recursion)
        if nextPage is not None:
            yield response.follow(nextPage, callback=self.startScraping)
