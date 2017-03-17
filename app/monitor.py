import app.clientthread as clientthread

class Monitor:
    
    def __init__(self, savedir):
        self.sites = []
        self.threads = []
        self.savedir = savedir
    
    # Add a site to the monitor
    # param:
    #   site {Site}
    def addSite(self, site):
        if not site in self.sites:
            self.sites.append(site)
            print("Added site: " + site.url)
            
            thread = clientthread.ClientThread(site, self.savedir)
            self.threads.append(thread)
            thread.start()

    def wait(self):
        for thread in self.threads:
            thread.join()