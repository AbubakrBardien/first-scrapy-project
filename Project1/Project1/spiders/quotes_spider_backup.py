import scrapy  # type: ignore
from ..items import Project1Item


class QuoteSpider(scrapy.Spider):
    name = "quotes_backup"  # Don't change variable name
    start_urls = ["https://quotes.toscrape.com/"]  # Don't change variable name

    # Don't change the funtion signiture (funcName, paramNum, paramNames)
    # def parse(self, response):  # 'response' contains the entire webpage source code
    # # retrieves the title of the webpage
    # title = response.css("title::text").extract()

    # # We use 'yield' instead of 'return' because it works with a scrapy generator behind the scenes
    # yield {"titleText": title}

    # --------------------------------------

    # all_quotes = response.css("div.quote .text::text").extract()
    # all_authors = response.css("div.quote .author::text").extract()

    # yield {
    #     "quotes": all_quotes,
    #     "authors": all_authors
    # }

    # --------------------------------------

    # all_div_quotes = response.css("div.quote")[0]
    # quotes = all_div_quotes.css(".text::text").extract()
    # authors = all_div_quotes.css(".author::text").extract()
    # tags = all_div_quotes.css(".tag::text").extract()
    # yield {
    #     "quotes": quotes,
    #     "authors": authors,
    #     "tags": tags
    # }

    # --------------------------------------

    # all_div_quotes = response.css("div.quote")

    # for quote_ in all_div_quotes:
    #     quote = quote_.css(".text::text").extract()
    #     author = quote_.css(".author::text").extract()
    #     tags = quote_.css(".tag::text").extract()
    #     yield {
    #         "quote": quote,
    #         "author": author,
    #         "tags": tags
    #     }

    # -----------------------------------------------------------

    def parse(self, response):
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

        nextPage = response.css("li.next a::attr(href)").extract_first()

        # Basically allows scrapy to loop through the webpages (a method similar to recursion)
        if nextPage is not None:
            yield response.follow(nextPage, callback=self.parse)

    # ---------------------------------------------------------------------------
    # In the terminal (assuming you're in the virtual environmant), navigate the the project folder.
    # Example: "~/Desktop/Web Scraping Projects/Scrapy/Project1"

    # Then run 'scrapy crawl <name>' in the terminal, where '<name>' represents the
    # value of the name variable in the class above.

    # --------------------------------------

    # Run 'scrapy shell "<URL>"' to do a kind of 'temporary web scraping' through
    # the use of the scrapy shell.

    # --------------------------------------
    # Assuming you're the items.py file to create temporary containers, you can
    # then export the data to different file formats. To do that, run 1 of these
    # terminal commands, depending in the file format you want.

    # 'scrapy crawl quotes -o items.json'
    # 'scrapy crawl quotes -o items.csv'
    # 'scrapy crawl quotes -o items.xml'
