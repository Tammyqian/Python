import urllib
import json

url = 'https://api.github.com/repos/pandas-dev/pandas/issues/25049/comments'

response = urllib.urlopen(url).read()
print response
print len(response)
resp = json.loads(response)
print resp
print len(resp)
