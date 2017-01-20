from subprocess import PIPE,Popen
import shutil
import os
import time


def main():
    directory = '/Users/student/Desktop/GRD_SRTM4.1'
    os.chdir(directory)
    each_file = os.listdir(directory)[868]
    Popen('/opt/local/bin/gmt grdsample ' + each_file + ' -T -G/Users/student/desktop/GRD_SRTM4.1_new/' + each_file, shell=True)


if __name__ == '__main__':
    main()