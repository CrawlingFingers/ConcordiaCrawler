import re
import os

def createurllist():
    infile = 'websphinx.txt'
    outfile = 'url_list.txt'
    pattern = "retrieving \[(.*)\]"
    urllist = []

    with open(infile, 'r') as f:
        lines = f.readlines()

    for line in lines:
        match = re.search(pattern, line)
        if match:
            urls = match.group(1) + '\n'
            print urls
            urllist.append(urls)

    with open(outfile, 'w') as g:
        g.seek(0)
        g.writelines(urllist)

def download_urls():
    infile = 'url_list.txt'

    with open(infile, 'r') as f:
        lines = f.readlines()

    for line in lines:
        os.system('wget -x -O ece %s' %line)
