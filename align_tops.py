import os
import sys
from shutil import copyfile
from subprocess import Popen, PIPE
import subprocess
from make_dem import file_finder

directory = "/Users/student/Desktop/Task-3-7-2017"
os.chdir(directory)

with open('sentinel_input.txt', 'r') as f:
    content = f.readlines()
    content = [x.replace('\n', '') for x in content]


data_folder = content[0].split('= ')[1]
orbit_folder = content[1].split('= ')[1]
work_folder = content[2].split('= ')[1]
master_image = content[3].split('= ')[1]
slave_image = content[4].split('= ')[1]
master_orbit = content[5].split('= ')[1]
slave_orbit = content[6].split('= ')[1]
topo_range = content[7].split('= ')[1]
swath_number = content[8].split('= ')[1]

topo_path = work_folder + '/topo'
orig_path = work_folder + '/orig'

os.mkdir(topo_path)
os.mkdir(orig_path)

long1, long2, lat1, lat2 = topo_range.split('/')

os.chdir('/shareddata/GRD_SRTM4.1')

file_finder(float(long1), float(long2), float(lat1), float(lat2), topo_path)



