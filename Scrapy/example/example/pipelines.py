# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ExamplePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        # Product Type --> switch to lowercase
        product_type = adapter.get('product_type')
        adapter['product_type'] = str(product_type).lower()
        
        # Price --> cast to float
        price = adapter.get('price')[0]
        adapter['price'] = float(price.replace('£',''))
        
        # Availability --> extract number of books available
        availability = adapter.get('availability')[0].split('(')
        if len(availability) < 2:
            adapter['availability'] = 0
        else:
            availability = availability[1].split(' ')[0]
            adapter['availability'] = int(availability)
        
        return item
    