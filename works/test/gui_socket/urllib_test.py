from urllib import urlopen
import re

webpage = urlopen('http://www.python.org')
print webpage

text = webpage.read()
print text
m = re.search('<a href="([^"]+)" .*?>about</a>', text, re.IGNORECASE)
print m.group(1)

