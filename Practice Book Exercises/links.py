import urllib.request

# Problem 65: Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked
# from that webpage.
def links(url):
    print('\nLinks in', url, ':')
    response = str(urllib.request.urlopen(url).read())
    links = []
    more_links = 1
    while more_links > 0:
        more_links = response.find('"http://')  # start of link
        if not more_links > 0:
            more_links = response.find('"https://')  # start of link
        if more_links > 0:
            response = response[more_links + 1:]
            more_links = response.find('"')         # end of link
            links.append(response[:more_links])
            response = response[more_links:]
        more_links = response.find('"http://')
        if not more_links > 0:
            more_links = response.find('"https://')  # start of link
    print(links)