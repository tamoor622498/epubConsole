
import ebooklib
from ebooklib import epub
from PIL import Image
import ascii_magic
import imageToAscii
import climage
import io
from pprint import pprint
import json
import xmltodict
import html2text
from rich.console import Console
from rich.markdown import Markdown


# my_art = ascii_magic.from_image_file('my_file.jpg')
# ascii_magic.to_terminal(my_art)

# #i = Image.open("my_file.jpg")

# #print(imageToAscii.do(i, 50))


# book = epub.read_epub('COMC.epub')
# images = list(book.get_items_of_type(ebooklib.ITEM_IMAGE))

# pic = images[1]

# b = pic.get_content()
# t = Image.open(io.BytesIO(b))

# t.thumbnail((50, 50), Image.ANTIALIAS)
# t.save("test.jpg", "JPEG")

# w, h = t.size

# #t = b.decode("ISO-8859-1").encode("utf-8")

# #x = imageToAscii.do(t, w//8)
# t = Image.open("test.jpg")

# x = imageToAscii.do(t, 200)

# print(x)

# f = open('img.txt','w')
# f.write(x)
# f.close()

# # d = (b.decode("ISO-8859-1").encode("utf-8"))

# binary_file = open("my_file.jpg", "wb")
# binary_file.write(b)
# binary_file.close()

# print('width:  ', w)
# print('height: ', h)
# print(pic.get_name())

#print(d)

#file = io.StringIO(d)

#print(climage.convert(d))

#print(images[0].get_name())


book = epub.read_epub('PHM.epub')

items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

t = items[6].get_content().decode("utf-8")#.replace('&#13;','')
# d = xmltodict.parse(t)
# j = json.dumps(d, indent=2)
print(t)
#m = html2text.html2text(t)

#print(m)

# console = Console()

# console.print(Markdown(m))

# for item in items:
#     t = item.get_content().decode("utf-8")
#     print(html2text.html2text(t))
#     print("\n\n\n\n")

#print(items[2].get_content())

# for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
#     t = epub.EpubCoverHtml(doc)
#     print(t)
