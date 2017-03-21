import os
import sys
from shutil import copyfile
from subprocess import Popen, PIPE
import subprocess

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
topo_range = content[6].split('= ')[1]
swath_number = content[7].split('= ')[1]

os.mkdir(work_folder + '/topo')
os.mkdir(work_folder + '/orig')

