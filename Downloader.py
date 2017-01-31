import mechanize
from time import sleep
import os

os.chdir('/Users/student/Desktop/SRTM3')

br = mechanize.Browser()


# Open your site
br.open('https://e4ftl01.cr.usgs.gov/SRTM/SRTMGL1.003/2000.02.11/')

f=open("source.html","w")
f.write(br.response().read())

filetypes=["hgt.zip"]
myfiles=[]
for l in br.links():
    for t in filetypes:
        if t in str(l):
            myfiles.append(l)


def downloadlink(l):
    f=open(l.text,"w")
    br.click_link(l)
    f.write(br.response().read())
    print l.text," has been downloaded"
    #br.back()

for l in myfiles:
    sleep(1)
    downloadlink(l)
