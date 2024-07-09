import urllib.request
import urllib.parse

url = 'https://alx-intranet.hbtn.io/status'
values = {'type' : '<class 'bytes'>',
          'content' : 'OK',
          'utf8 content' : 'OK'}
data = urllib.parse.urlencode(values)
data - data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
  the_page - response.read()


