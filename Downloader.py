import mechanize
from time import sleep
from base64 import b64encode
import os

os.chdir('/Users/student/Desktop/SRTM3')

url = 'https://e4ftl01.cr.usgs.gov/SRTM/SRTMGL1.003/2000.02.11/N00E006.SRTMGL1.hgt.zip'
username = 'mattwei'
password = '2016#Asf'

b64login = b64encode('%s:%s' % (username, password))

br = mechanize.Browser()

br.addheaders.append( 
  ('Authorization', 'Basic %s' % b64login )
)

#br.retrieve('https://e4ftl01.cr.usgs.gov/SRTM/SRTMGL1.003/2000.02.11/N00E006.SRTMGL1.hgt.zip','N00E006.SRTMGL1.hgt.zip')

# Open your site
br.open('https://e4ftl01.cr.usgs.gov/SRTM/SRTMGL1.003/2000.02.11/')
f=open("source.html","w")
f.write(br.response().read())

filetypes=["hgt.zip"]
myfiles=[]
newfiles = []

for l in br.links():
    for t in filetypes:
        if t in str(l):
            myfiles.append(l)

for l in myfiles:
    if 'xml' not in l.text:
        newfiles.append(l.text)

for l in newfiles:
    br.retrieve('https://e4ftl01.cr.usgs.gov/SRTM/SRTMGL1.003/2000.02.11/' + l, l)
    print 'Downloading {}'.format(l)
