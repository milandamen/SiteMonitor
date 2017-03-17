#!/usr/bin/python3

import app
from app import config
from app import monitor

config = config.Config()
monitor = monitor.Monitor(config.savedir)

for site in config.sites:
    monitor.addSite(site)
    
#monitor.wait()

#import urllib.request
#import calendar
#import time

##URL = 'https://aidoru-online.org'
#URL = 'http://darvit.nl'
#MIN_INTERVAL = 60       # Minimum probe interval in seconds

#def tryURL(url):
    #try:
        #with urllib.request.urlopen(url) as response:
            #page = response.read()
            #print('Success')
            #return True
    #except urllib.error.URLError as e:
        #print('Failed')
        #return False

#def getTime():
    #return calendar.timegm(time.gmtime()) # Return seconds since epoch in UTC

#while True:
    #startTime = getTime()
    #print(startTime)
    #result = tryURL(URL)
    #endTime = getTime()
    #print(endTime)
    #if endTime - startTime < MIN_INTERVAL:
        #time.sleep(MIN_INTERVAL - (endTime - startTime))