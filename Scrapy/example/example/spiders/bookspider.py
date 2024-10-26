import scrapy
from fake_useragent import UserAgent
from example.items import BookItem

class BookspiderSpider(scrapy.Spider):    
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]
    
    def parse(self, response):
        books = response.css('article')
        for book in books:
            # Each Book Page
            this_book = book.css("h3 a::attr(href)").get()
            if this_book is not None:
                if 'catalogue/' in this_book:
                    book_url = 'https://books.toscrape.com/' + this_book
                else:
                    book_url = 'https://books.toscrape.com/catalogue/' + this_book

            yield response.follow(book_url,callback=self.parse_book)

        
        # Next Books Page
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
                
            yield response.follow(next_page_url,callback=self.parse)
        
    def parse_book(self,response):
        table_rows = response.css('table tr')
        
        book_item = BookItem() 
        book_item['url'] = response.url,
        book_item['title'] = response.css('h1::text').get(),
        book_item['product_type'] = table_rows[1].css('td::text').get(),
        book_item['price'] = table_rows[2].css('td::text').get(),
        book_item['availability'] = table_rows[5].css('td::text').get(),
        book_item['number_of_reviews'] = table_rows[6].css('td::text').get(),
        book_item['stars'] = response.css('p.star-rating::attr(class)').get(),
        book_item['description'] = response.xpath("//div[@class='product_description']/following-sibling::p/text()").get()
        
        yield book_item


        
        
        
        