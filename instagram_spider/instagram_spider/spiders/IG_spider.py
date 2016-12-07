import scrapy
import json

class IG_spider(scrapy.Spider):
    '''
    [1] - Instagram is set up really nicely for this
    [2] - These tags are universal across instagram so no need to make this
          less specific or do anything fancier here
    '''
    name = "IG"

    start_urls = []
    file_input = '../../../external_files/input.txt' # TODO Change this part
    f_read = open(file_input, 'r')
    for line in f_read:
        start_urls.append('https://www.instagram.com/'+line[:-1]+'/')


    def parse(self, response):
        # Extracts the JSON which makes up the whole instagram profile [1]
        extracted_string = response.css("script").extract()[6]

        if len(extracted_string) > 31 and extracted_string[31] == 'w': # Skips invalid pages
            stripped_json = extracted_string[52:-10] # Strips script tags and 'window._sharedData =' [2]
            proccessed_json = parseJSON(stripped_json)

            filename = "../../../external_files/output.json" # TODO Change this part
            with open(filename, 'a') as f:
                f.write(proccessed_json)


def parseJSON(input_json):
    '''
    Helper Function to parse JSON

    Input: Takes an input string of each users' profile that is valid JSON format
    Returns: Multiple dictionaries seperated by commas
             Note: This needs to be fixed! Very hacky

    TODO finish adding functionality
        - Need to clean up the return here.
    '''

    extracted_info = json.loads(input_json)

    # Fields we need from user
    user_info = extracted_info['entry_data']['ProfilePage'][0]['user']
    username = user_info['username'] # we probably don't need this
    user_id = user_info['id']
    followed_by = user_info['followed_by']['count']
    follows = user_info['follows']['count']
    mediaCount = user_info['media']['count']
    is_private = user_info['is_private']
    #has_next_page = user_info['media']['count']['page_info']['has_next_page']

    if mediaCount < 12 or is_private:
        return ''

    # Fields we need from image
    output_images = []
    image_nodes = user_info['media']['nodes']
    for image in image_nodes:
        if not image['is_video']:

            image_thumbnail_src = image['thumbnail_src']
            image_display_src = image['display_src']
            out_image = {'username': username,
                        'user_id': user_id,
                        'im_id': image['id'],
                        'im_code': image['code'],
                        'followed_by': followed_by,
                        'follows': follows,
                        'date': image['date'],
                        'likes': image['likes']['count'],
                        #'hashtag_count': image_hashtag_count,
                        'thumbnail_src': image_thumbnail_src[:image_thumbnail_src.index('.jpg')+4],
                        'display_src': image_display_src[:image_display_src.index('.jpg')+4]
                        }
            #image_caption = image['caption']
            #image_hashtag_count = image_caption.count('#')
            output_images.append(out_image)
    return formatJSON(str(output_images)[1:-1]+',')

def formatJSON(input_json):
    input_json = input_json.replace('u\'', '"')
    input_json = input_json.replace('\'', '"')
    input_json = input_json.replace('{', '\n{')
    return input_json
