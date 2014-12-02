import urllib2

lines = [line.strip() for line in open('url_list.txt', 'r')]
lines = set(lines)

for file_path in lines:
  print file_path
  response = urllib2.urlopen(file_path)
  html = response.read()