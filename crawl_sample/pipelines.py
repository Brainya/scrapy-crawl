# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlSamplePipeline(object):
    def open_spider(self, spider):
        # スクレイピングを始めるときに呼び出される
        pass

    def close_spider(self, spider):
        # スクレイピングが完了したときに呼び出される
        pass
    
    def process_item(self, item, spider):
        # dbに書き込んだりする
        return item
