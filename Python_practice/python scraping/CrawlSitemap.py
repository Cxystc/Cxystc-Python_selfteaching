import Download
import re
def CrawlSitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)<//loc>',sitemap)
    for link in links :
        download(link)
CrawlSitemap('Sitemap: http://www.csdn.net/article/sitemap.txt')

