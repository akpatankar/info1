#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint
import re
import StringIO

# Use the json module to dump a dictionary to a string for posting.
data_string = urllib.quote(json.dumps({'id': 'data-explorer'}))

# Make the HTTP request.
response = urllib2.urlopen('http://catalog.data.gov/api/3/action/package_list',
        data_string)
assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())

# Check the contents of the response.
assert response_dict['success'] is True
#pprint.pprint(response_dict)

result = response_dict['result']
pprint.pprint(result)

#url1 = result[0]["url"]
#url2 = response_dict["url"]

response = urllib2.urlopen('http://catalog.data.gov/api/3/action/package_list?rows=25',
        data_string)
assert response.code == 200
response_dict2 = json.loads(response.read())
print response_dict2['result']['results'][24]['resources']
#print re.search("http", result).group()