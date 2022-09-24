import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup as bs
import lxml
from html.parser import HTMLParser
import json
import xmltodict

book = epub.read_epub('Axiom.epub')
print(book.get_metadata('DC', 'title'))
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
t = items[8].get_content().decode("utf-8")


bs_content = bs(t, features="xml")

con = bs_content.find("body").contents

for child in con:
    if (child != '\n'):
        for sub in child.contents:
            if(sub != '\n'):
                print(sub.getText())
                print("================================================================================")
                print(sub.find("img"))
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("--------------------------------------------------------------------------------")



# for child in body.findChildren():
#     print(child.findChildren())
#     print("-----------------------------------------------------------------------------------------------------------------")

#print(vals)

# for child in children:
#     print(child)
#     # d = xmltodict.parse(str(child))
#     # j = json.dumps(d, indent=2)
#     # print(j)
#     print("-----------------------------------------------------------------------------------------------------------------")


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


