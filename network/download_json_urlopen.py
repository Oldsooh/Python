from __future__ import (absolute_import, division, print_function, unicode_literals)

try:
    # For Python 2.x
    from urllib2 import urlopen
except ImportError:
    # For Python 3.x
    from urllib.request import urlopen

import json

json_file_name = 'network/test_files/btc_close_2017.json'
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

response = urlopen(json_url)
req = response.read()

with open(json_file_name, 'wb') as f:
    f.write(req)

file_urllib = json.loads(req)
print(file_urllib)