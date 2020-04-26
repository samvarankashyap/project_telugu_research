from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque
from requests import get  # to make GET request
import hashlib


def download_file_from_url(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)
    print("DOWNLOADED URL "+url+" TO "+file_name)



url = "https://www.eenadu.net"
# a queue of urls to be crawled next
new_urls = deque([url])
# a set of urls that we have already processed 
processed_urls = set()
# a set of domains inside the target website
local_urls = set()
# a set of domains outside the target website
foreign_urls = set()
# a set of broken urls
broken_urls = set()
# process urls one by one until we exhaust the queue
#test = []
some = 0
while len(new_urls):
    # move url from the queue to processed url set
    url = new_urls.popleft()
    processed_urls.add(url)
    # print the current url
    #if not ("ruchulu" in url) or ("api" in url) or ("whatsapp" in url) or ("t.me" in url) or ("facebook" in url) or ("twitter" in url):
        #print("not processing")
    #    continue
    if url.startswith("//"):
        url = "https:"+url
    print("PROCESSING URL %s" % url)
    # check if the url exists
    fdr = open("collected_urls.txt", "r")
    lines_in_file = fdr.readlines()
    fdr.close()
    if not (url+"\n" in lines_in_file):
        fd = open("collected_urls.txt", "a")
        fd.write("\n")
        fd.write(url)
        fd.close()
    some = some + 1
    print(some)
    #test.append(url)
    #print(len(test))
    try:
        print("DOWNLOADING HTML FILE")
        response = requests.get(url)
        if not (url+"\n" in lines_in_file):
            download_file_from_url(url, "./html_files/"+hashlib.md5(url.encode('utf-8')).hexdigest()+".html")

    except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema):
        # add broken urls to it’s own set, then continue
        print("Broken url %s" % url)
        broken_urls.add(url)
        continue

    # extract base url to resolve relative links
    parts = urlsplit(url)
    base = "{0.netloc}".format(parts)
    strip_base = base.replace("www.", "")
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url

    soup = BeautifulSoup(response.text, "lxml")
    for link in soup.find_all('a'):
        # extract link url from the anchor
        anchor = link.attrs["href"] if "href" in link.attrs else ''
        if anchor.startswith('/'):
#            local_link = base_url + anchor
            local_link =  anchor
            local_urls.add(local_link)
        elif strip_base in anchor:
            local_urls.add(anchor)
        elif not anchor.startswith('http'):
            local_link = path + anchor
            local_urls.add(local_link)
        else:
            foreign_urls.add(anchor)
        for i in local_urls:
            if not i in new_urls and not i in processed_urls:
                new_urls.append(i)

# if you want to include all the urls. which is highly unlikely
#        if not link in new_urls and not link in processed_urls:
#            new_urls.append(anchor)

print(len(url))
