import json


class IG_spider(scrapy.Spider):

    file_input = '../external_files/input.json' # TODO Change this part
    with open(file_input) as data_file:
        data = json.load(data_file)

    def sortList():
        pass
