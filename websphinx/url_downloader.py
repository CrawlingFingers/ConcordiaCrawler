import urllib2
import os

lines = [line.strip() for line in open('url_list.txt', 'r')]
lines = set(lines)

for file_path in lines:

  try:
    print file_path
    response = urllib2.urlopen(file_path)
    html = response.read()

    save_path = file_path.replace('http://www.mcgill.ca/', '') + ".html"
    dir_path = save_path.replace('\/[A-Za-z0-9\.]*$', '')

    print "dir path: " + dir_path


    if not os.path.exists(os.path.dirname(save_path)):
      os.makedirs(os.path.dirname(save_path))

    with open(save_path, 'w') as f:
      f.write(html)

  except:
    None
