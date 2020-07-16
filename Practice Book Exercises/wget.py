import urllib.request

# Problem 62: Write a program wget.py to download a given URL. The program should accept a URL as argument,
# download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as
# index.html.
def wget(url):
    filename = str(url).split('/')[-1]
    if filename == '':
        filename = 'index.html'
    print('Saving', url, 'as', filename, '.')
    response = urllib.request.urlopen(url)
    file = open(filename, 'w')
    file.write(str(response.read()))
    file.close()