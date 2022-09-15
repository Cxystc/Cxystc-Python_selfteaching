class Throttle:
        """
节流阀
"""
    def __init__ (self,delay)：
        self.delay = delay
        self.domain = {}
    def wait (self,url):
        domain = urlparse.urlparse(url),netloc
        last_accessed = self.domian.get(domain)
        if self.delay > 0 and last_accessed in not None:
            sleep.secs =self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0 :
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.datetime.now()