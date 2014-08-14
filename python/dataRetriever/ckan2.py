#!/usr/bin/env python
import json
import pprint
import sys
import urllib, urllib2, requests, zipfile, StringIO

all_file_url = []
all_zip_file_url = []
for startRow in range(1,1000,1000):
    print startRow

# Use the json module to dump a dictionary to a string for posting.
    data_string = urllib.quote(json.dumps({'id': 'data-explorer'}))


# Make the HTTP request.
    urlString = r'''http://catalog.data.gov/api/3/action/package_list?start=%s&rows=10''' % (startRow)
    response = urllib2.urlopen(urlString, data_string)  
    assert response.code == 200

    # Use the json module to load CKAN's response into a dictionary.
    response_dict = json.loads(response.read())

    # Check the contents of the response.
    assert response_dict['success'] is True
    #pprint.pprint(response_dict)

    result = response_dict['result']

# Count of Rows fetched out of 1000
    print len(response_dict['result']['results'])
# Dataset count
    print response_dict['result']['count']

    file_url = []
    for result in response_dict['result']['results']:
        #   print result['resources'][0]['url']
    
        try:  
            # print result['resources'][0]['url']
            file_url.append(result['resources'][0]['url'])
     
        except IOError as e:
                    print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
                    print "Could not convert data to an integer."
        except IndexError:
                    print "Index Error"
        except:
                    print "Unexpected error:", sys.exc_info()[0]
        
    #print file_url
    print len(file_url)

# Get zipped fies
    zip_file_url = []
    for url in file_url:
        if 'zip' in url:
            if 'http' in url:
                zip_file_url.append(url)
            
    print len(zip_file_url)      

# Download zipped files as csv
    for url in zip_file_url:   
        print url    
        
        try:  
             r = requests.get(url)
             z = zipfile.ZipFile(StringIO.StringIO(r.content))
             z.extractall()
        
        except IOError as e:
                    print "zip I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
                    print "zip Could not convert data to an integer."
        except IndexError:
                    print "zip Index Error"
        except:
                    print "zip Unexpected error:", sys.exc_info()[0]

# Capture all urls     
all_file_url.append(file_url)
all_zip_file_url.append(zip_file_url)
print all_zip_file_url