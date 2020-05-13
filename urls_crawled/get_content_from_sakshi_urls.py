import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import json
test_dict = {}
def get_content_sakshi(url, count):
    url = url.strip("\n")
    if not url[-1].isdigit():
        return False

    """
    response = urllib.request.urlopen(url)
    webContent = response.read()

    soup = BeautifulSoup(webContent, "html.parser")
    #print(soup.find(id='page-title').text)
    main_content = soup.find(id='main-content').text
    """
    test_dict[count] = {}
    test_dict[count]['url'] = url
    test_dict[count]['file'] = str(count)+"_"+url.split('/')[-1]+".txt"
    #f = open("./sakshi_content/"+str(count)+"_"+url.split('/')[-1]+".txt", 'w')
    #f.write(main_content)
    #f.close()
    return True

fd = open("sakshi_urls.txt", "r")
i = 1
for line in fd:
    print(i)
    i = i+1;
    print(line.strip("\n"))
    get_content_sakshi(line, i)
fd.close()

f = open("./sakshi_url_dict.txt","w")
f.write(json.dumps(test_dict))
f.close()

