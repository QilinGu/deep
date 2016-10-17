import scrapy
import json

class IG_spider(scrapy.Spider):
    name = "IG"

    start_urls = [
            'https://www.instagram.com/francisco.rs/',
            'https://www.instagram.com/_jantie._/',
            'https://www.instagram.com/gaston_contreras4/',
            'https://www.instagram.com/j_shikari/'
            'https://www.instagram.com/yasminnstifler/'
            'https://www.instagram.com/thenotrealnickrobinson/'
            'https://www.instagram.com/mari_armada16/'
            'https://www.instagram.com/carolina___19/'
            'https://www.instagram.com/nemanja_sindja/'
            'https://www.instagram.com/leoo.taborda3/',
            'https://www.instagram.com/giulignr/',
            'https://www.instagram.com/pariparker/',
            'https://www.instagram.com/bencomomel/',
            'https://www.instagram.com/jeison_lebron/',
            'https://www.instagram.com/danirivera0918/',
            'https://www.instagram.com/sharapova4884/',
            'https://www.instagram.com/sshawnmendess.cf/',
            'https://www.instagram.com/mrreckless23foreva/',
            'https://www.instagram.com/karo_by_cuteforyou_blog/',
            'https://www.instagram.com/idk.s.x_/',
            'https://www.instagram.com/helsagabriela_/',
            'https://www.instagram.com/ebnnasserdine/'
        ]


    def parse(self, response):
        # Extracts the JSON which makes up the whole instagram profile
        extractedJSON = response.css("script").extract()[6]
        proccessedJSON = parseJSON(extractedJSON)

        filename = "output.JSON" # TODO Change this part
        with open(filename, 'a') as f:
            f.write(proccessedJSON)


# Helper Function to parse JSON (Should probably clean this up later on)
def parseJSON(json):
    if json.find('"is_private": true') > 0:
        return ''
    else: return json+'\n'
    # TODO finish adding functionality
