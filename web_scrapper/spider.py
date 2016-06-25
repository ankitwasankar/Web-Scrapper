import urllib2
import urlparse

import BeautifulSoup
from django.conf import settings

# defining global variables
url = ""
depth = 999
domain = False
host = ""
visited = []
fetched = []
format_list = []


def crawl(url_param, depth_param, domain_param, format_list_param):
    """
    initialize spider and start crawling
    url - site url to crawl
    depth - depth to which the links to fetch
    domain - boolean value - whether to fetch link outside domain or not
    """
    global url
    global depth
    global domain
    global host
    global visited
    global fetched
    global format_list
    # initialize spider code here
    url = correct_url(url_param)
    depth = int(depth_param)
    domain = bool(domain_param)
    host = get_host(url)
    visited.append(url)
    format_list = format_list_param
    # start crawler code here
    flag = start_fetching()
    return flag


def correct_url(url):
    """
    It will correct URL to pattern like - http://www.mytechblog.in/
    """
    return url


def get_host(url):
    """
    Param URL will be in corrected form - http://www.mytechblog.in/
    Returns the host name from url like - mytechblog.in
    """
    return url


def start_fetching():
    """
    Using global variables, it will start fetching links one by one
    and store only those which ends with given filetype
    """
    global url
    global depth
    global domain
    global host
    global visited
    global fetched
    global format_list
    # start the fetching
    for url in visited:
        print "Downloading = " + str(url)
        # try fetching the url now
        try:
            request = urllib2.Request(
                url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib2.urlopen(request)
        except Exception as e:
            pass
        # Parsing the HTML content of URL
        try:
            soup = BeautifulSoup.BeautifulSoup(response)
        except Exception as e:
            pass
        # find all the urls that is in anchor tag
        try:
            for a in soup.findAll('a'):
                if 'href' in str(a):
                    fetched_link = a['href']
                    corrected_link = urlparse.urljoin(url, fetched_link)
                    if corrected_link not in visited:
                        visited.append(corrected_link)
                        print "visited = " + str(corrected_link)
                        # If it has required filetype add it to fetched
                        if corrected_link.endswith(tuple(format_list)):
                            fetched.append(corrected_link)
                            print "Fetched = " + str(corrected_link)
        except Exception as e:
            pass
    # Simply returning true without analysis
    return True
