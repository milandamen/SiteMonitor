import hashlib
import urllib.request
import http.client

class Site:
    def __init__(self, config):
        self.url = config["url"]
        if "interval" in config:
            self.interval = config["interval"]
        else:
            self.interval = 60
        
        self.hash = hashlib.sha1(self.url.encode('utf-8')).hexdigest()
    
    def refresh(self):
        try:
            with urllib.request.urlopen(self.url) as response:
                print(self.url + ': Success')
                return True
        except (urllib.error.URLError, http.client.HTTPException) as e:
            print(self.url + ': Failed')
            return False
        