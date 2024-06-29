# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter  # type: ignore
import sqlite3


class Project1Pipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("quotes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("DROP TABLE IF EXISTS quotes_tb")
        self.curr.execute('''CREATE TABLE quotes_tb(
                          Quote TEXT,
                          Author TEXT,
                          Tags TEXT
                          )''')

    def store_db(self, items):
        self.curr.execute('''INSERT INTO quotes_tb VALUES (?, ?, ?)''', (
            items["quote"][0],
            items["author"][0],
            items["tags"][0]
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

# ---------------------------------------------------------------------------
# Extracted Data --> Temporary Containers (items) --> Pipeline --> Database
