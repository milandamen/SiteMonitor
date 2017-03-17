import urllib.request

class Site:
    def __init__(self, config):
        self.url = config["url"]
        if "interval" in config:
            self.interval = config["interval"]
        else:
            self.interval = 60
    
    def refresh(self):
        try:
            with urllib.request.urlopen(self.url) as response:
                print('Success')
                return True
        except urllib.error.URLError as e:
            print('Failed')
            return False
        