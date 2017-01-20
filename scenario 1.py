import os
import sys
from shutil import copyfile
from subprocess import Popen, PIPE
import subprocess
import time
from threading import Thread

from generate_dem import make_dem

def main(argv):

    directory = argv[1]
    os.chdir(directory + '/raw')
    print directory + '/raw'
    all_files = os.listdir(directory + '/raw')
    print all_files
    target = [x for x in all_files if 'IMG' in x][0]
    target = 'raw/' + target
    print target
    print directory

    make_dem(directory + '/' + target, directory)

    new_directory = directory.replace('raw', '')

    print new_directory

    print directory + '/raw'

    target2 = [x for x in os.listdir(directory + '/raw') if 'IMG' in x][1]
    target = target.split('raw/')[1]
    print target2
    print target



    copyfile('/shareddata/config.alos.txt', directory + '/config.alos.txt')

    os.chdir(new_directory)

    time.sleep(10)


    command1 = 'p2p_ALOS.csh ' + target + ' ' + target2 + ' config.alos.txt'

    print command1

    p = Popen('source /shareddata/bashrc\n' + command1, shell=True, stdout=PIPE)
    p.communicate()


if __name__ == '__main__':
    main(sys.argv)