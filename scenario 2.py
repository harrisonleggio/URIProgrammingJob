import os
import sys
from shutil import copyfile
from subprocess import Popen, PIPE
import subprocess
import time
from threading import Thread
from pre_proc_batch import pre_proc
from generate_pairs import generate_pairs
from generate_dem import make_dem


def main(argv):

    directory = argv[1]
    threshold = argv[2]
    os.chdir(directory)
    pre_proc(directory)

    #table_file = [x for x in os.listdir(directory + '/raw') if 'table.gmt' in x][0]
    #generate_pairs(table_file, threshold)
    image_file = [x for x in os.listdir(directory + '/raw/') if 'IMG' in x][0]

    print image_file
    print directory

    #make_dem(image_file, directory)


if __name__ == '__main__':
    main(sys.argv)