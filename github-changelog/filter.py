# /// script
# dependencies = [
#   "defusedxml~=0.7"
# ]
# ///

import sys
import re
from pprint import pprint
from defusedxml.ElementTree import parse, tostring
from xml.etree.ElementTree import Comment

ignored_titles_re = re.compile('secret scanning|copilot|GitHub Models|enterprise', flags=re.IGNORECASE)

dom = parse(sys.stdin)
channel = dom.find('channel')

for item in channel.findall('item'):
    title = item.find('title')
    title_text = ''.join(title.itertext())
    if ignored_titles_re.search(title_text):
        channel.remove(item)
        print(tostring(Comment(f' Removed "{title_text}" '), encoding='unicode'))

print(tostring(dom.getroot(), encoding='unicode'))
