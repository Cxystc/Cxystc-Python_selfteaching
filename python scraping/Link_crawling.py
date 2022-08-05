import re 
def get_links (html):
    webpage_regex = re.compile ('<a[^>] + href = ["\'],re.IGNORECASE)
    return webpage_regex.find_all(html)

import roboturlparse 
def crawler_link(seed_url,regex_forlink):
    crawler_queue = [seed_url]
    seen_list = set(crawler_queue)
    while crawler_queue:
        url = crawler_link.pop()
        download(url) = html
        if  re.can_fetch(user_agent,url):
            for link in get_links(html):
                if re.match (regex_forlink,link):
                    if link not in seen_list:
                        link = urlparse.urljoin(seed_url,link)
                        crawler_queue.append(link)
                        seen_list.add(link)
                        
