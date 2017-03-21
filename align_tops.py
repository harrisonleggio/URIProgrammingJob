import os
import sys
from shutil import copyfile
from subprocess import Popen, PIPE
import subprocess
from make_dem import file_finder
import re

directory = "/Users/student/Desktop/Task-3-7-2017"
os.chdir(directory)

with open('sentinel_input.txt', 'r') as f:
    content = f.readlines()
    content = [x.replace('\n', '') for x in content]


data_folder = content[0].split('= ')[1]
orbit_folder = content[1].split('= ')[1]
work_folder = content[2].split('= ')[1]
master_folder = content[3].split('= ')[1]
slave_folder = content[4].split('= ')[1]
master_orbit = content[5].split('= ')[1]
slave_orbit = content[6].split('= ')[1]
topo_range = content[7].split('= ')[1]
swath_number = content[8].split('= ')[1]

topo_path = work_folder + '/topo'
orig_path = work_folder + '/orig'

os.mkdir(topo_path)
os.mkdir(orig_path)

long1, long2, lat1, lat2 = topo_range.split('/')

#file_finder(float(long1), float(long2), float(lat1), float(lat2), topo_path)

os.chdir(orig_path)



command1 = 'ln -s {}/{}.SAFE/measurement/*iw{}*vv* .'.format(data_folder, master_folder, swath_number)
command2 = 'ln -s {}/{}.SAFE/annotation/*iw{}*vv* .'.format(data_folder, master_folder, swath_number)
command3 = 'ln -s {}/{}.SAFE/measurement/*iw{}*vv* .'.format(data_folder, slave_folder, swath_number)
command4 = 'ln -s {}/{}.SAFE/annotation/*iw{}*vv* .'.format(data_folder, slave_folder, swath_number)
command5 = 'ln -s {}/dem.grd .'.format(topo_path)
command6 = 'ln -s {}/{} .'.format(orbit_folder, master_orbit)
command7 = 'ln -s {}/{} .'.format(orbit_folder, slave_orbit)



p1 = Popen(command1, shell=True)
p1.wait()
p2 = Popen(command2, shell=True)
p2.wait()
p3 = Popen(command3, shell=True)
p3.wait()
p4 = Popen(command4, shell=True)
p4.wait()
p5 = Popen(command5, shell=True)
p5.wait()
p6 = Popen(command6, shell=True)
p6.wait()
p7 = Popen(command7, shell=True)
p7.wait()

pat1 = '_(\d{6})_'
master_pattern = re.findall(pat1, master_folder)[0]

master_image = [x for x in os.listdir(orig_path) if master_pattern in x][0]
master_image = master_image.strip('.tiff')

slave_pattern = re.findall(pat1, slave_folder)[0]
slave_image = [x for x in os.listdir(orig_path) if slave_pattern in x][0]
slave_image = slave_image.strip('.tiff')

print master_image, slave_image

command8 = '/usr/local/GMT5SAR/bin/align_tops.csh {} {} {} {} {}/dem.grd'.format(master_image, master_orbit, slave_image, slave_orbit, orig_path)
p8 = Popen(command8, shell=True)
p8.wait()

os.chdir(work_folder)

swath_folder = 'F{}'.format(swath_number)
swath_raw = swath_folder + '/raw'
swath_topo = swath_folder + '/topo'

os.mkdir(swath_folder)
os.mkdir(swath_raw)
os.mkdir(swath_topo)

command9 = 'cp {}/config.s1a.txt {}/{}/.'.format(data_folder, work_folder, swath_folder)
command10 = 'ln -s {}/orig/*{}* {}/{}/raw/.'.format(work_folder, swath_folder, work_folder, swath_folder)
command11 = 'ln -s {}/topo/dem.grd {}/{}/topo/.'.format(work_folder, work_folder, swath_folder)

p9 = Popen(command9, shell=True)
p10 = Popen(command10, shell=True)
p11 = Popen(command11, shell=True)

os.chdir(work_folder + '/' + swath_folder)








