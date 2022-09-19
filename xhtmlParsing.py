import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup as bs
import lxml
from html.parser import HTMLParser
import json
import xmltodict

book = epub.read_epub('Axiom.epub')
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
t = items[6].get_content().decode("utf-8")#.replace('&#13;','')


bs_content = bs(t, features="xml")

body = bs_content.find("body")

print(list(bs_content.children)[1])

# child = body.contents[1]

# for c in child.findChildren():
#     #if(c.findChildren()):
#     d = xmltodict.parse(str(c))
#     j = json.dumps(d, indent=2)
#     sub = d[list(d.keys())[0]]
#     for key in sub.keys():
#         if(key == "#text"):
#             print(sub[key])
#         #print(key)
#     print("--------------------------------------------------------------")


