import urllib2
def Downlaod(url,retries_number=5):
    #urllib2只能用于python2
    #urllib3 urllib
    print('Download:',url)
    try:
        html = urllib.urlopen(url).read()
        print ('Download Successfully')

    except urllib2.URLRrror as e:
        print(e.reason)
        html=None
        if retries_number > 0 :
            if hasattr(e,'code') and 500 < e.code <= 600:
                print ('Retry now....')
                return Downlaod(url,retries_number-1)
        else:
            print(
                "The website is unaccessible"
            )
    return html