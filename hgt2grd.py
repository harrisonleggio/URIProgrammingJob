from subprocess import Popen, PIPE
import sys
import os
import re

os.chdir('/Users/student/Desktop/SRTM3')

all_files = [x for x in os.listdir() if 'hgt' in x]

for each_file in all_files:
    name = each_file.split('.')[0]
    sub = '(\d+)[WE](\d+)'
    matches = re.findall(sub, name)
    lat = matches[0][0]
    lon = matches[0][1]
    lat = int(lat)
    lon = int(lon)
    if 'S' in name:
        lat = -lat
    if 'W' in name:
        lon = -lon
    lat2 = lat + 1
    lon2 = lon + 1

    coords = [lon, lon2, lat, lat2]
    print coords
