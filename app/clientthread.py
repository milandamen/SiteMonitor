import calendar
import hashlib
import threading
import time

class ClientThread(threading.Thread):
    
    def __init__(self, site, savedir):
        self.site = site
        self.savedir = savedir
        threading.Thread.__init__(self)
        
    def run(self):
        print("Started thread for " + self.site.url)
        
        while True:
            startTime = getTime()
            startStopwatch = time.time()
            res = self.site.refresh()
            endTime = getTime()
            endStopwatch = time.time()
            interval = int((endStopwatch - startStopwatch) * 1000) # Time diff in msec
            
            result = {}
            result["time"] = endTime
            result["success"] = res
            result["interval"] = interval
            
            # Save result
            self.save(result)
            
            if endTime - startTime < self.site.interval:
                time.sleep(self.site.interval - (endTime - startTime))
    
    def save(self, result):
        # Convert result to protocol
        time = str(result["time"])
        success = "+" if result["success"] else "-"       # result["success"] ? "+" : "-"
        interval = str(result["interval"]) + "i"
        
        resultStr = time + success + interval
        print("Result: " + resultStr)
        
        # Convert the site URL to a sha1 hash and use that as filename
        savePath = self.savedir + self.site.hash
        print("Saving to " + savePath)
        f = open(savePath, "a")
        f.write(resultStr)
        f.close()

def getTime():
        return calendar.timegm(time.gmtime()) # Return seconds since epoch in UTC