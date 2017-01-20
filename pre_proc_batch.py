import os
import subprocess
from subprocess import Popen, PIPE
import sys
from shutil import copyfile


def pre_proc(directory):

    os.chdir(directory + '/raw')
    copyfile('/shareddata/batch.config', directory + '/raw/batch.config')

    file_sizes = []
    files = []
    all_files = [x for x in os.listdir('.') if 'IMG' in x]

    for each_file in all_files:
        files.append(each_file)
        file_sizes.append(os.path.getsize(each_file))

    print file_sizes
    print files

    max_index = file_sizes.index(max(file_sizes))
    max_file = files[max_index]
    print max_file

    p = Popen('ls IMG* > temp.in', shell=True)
    p.communicate()

    with open(directory + '/raw/temp.in', 'r') as f:
        data = f.readlines()
        data = [x.strip('\n') for x in data]
        data[0], data[max_index] = data[max_index], data[0]
    with open(directory + '/raw/data.in', 'w') as m:
        for each in data:
            m.write(each + '\n')

    os.remove(directory + '/raw/temp.in')

    #P = Popen('source /shareddata/bashrc\n/usr/local/GMT5SAR/bin/pre_proc_batch.csh ALOS data.in batch.config', shell=True)
    #P.communicate()
