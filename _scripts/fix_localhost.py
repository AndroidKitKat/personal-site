#!/usr/bin/env python3

import xml.etree.ElementTree as ET

def load_and_fix(feed_file):
    with open(feed_file, 'r+') as feed:
        new_feed = feed.read().replace('http://localhost:4002', 'https://www.michaeleisemann.com')
        # print(new_feed)
        feed.write(new_feed)
#         tree = ET.parse(feed)
#         root = tree.getroot()

#         for elem in root.getiterator():
#             try:
#                 elem.text = elem.text.replace('localhost:4002', 'www.michaeleisemann.com')
#             except AttributeError:
#                 pass

#             tree.write('/home/akk/www/personal-site/_site/feed.xml')

load_and_fix('/home/akk/www/personal-site/_site/feed.xml')
