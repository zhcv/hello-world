import requests
import re
import time

local = time.strftime('%Y.%m.%d')
print local


url = 'http://cn.bing.com/'
con = requests.get(url)
content = con.text

reg = r"(az/hprichbg/rb/.*?.jpg)"
a = re.findall(reg, content, re.S)[0]
print a

picUrl = url + a
read = requests.get(picUrl)

with open('%s.jpg' % local, 'wb') as f:
    f.write(read.content)
