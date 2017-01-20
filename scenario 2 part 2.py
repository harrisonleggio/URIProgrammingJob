import os
import sys
from shutil import copyfile
from subprocess import Popen, PIPE
import fileinput

def main(argv):
    directory = argv[1]
    super_file = argv[2]
    super_file_name = super_file.split('/')[-1]
    new_directory = directory.replace('/raw', '')

    print directory
    print super_file
    print super_file_name
    print new_directory

    intf = [x for x in os.listdir(directory) if 'intf.in' in x][0]
    print intf

    with open(directory + '/' + intf, 'r') as f:
        contents = f.readlines()

    contents = [x.strip('\n') for x in contents]
    contents = [x + ':' + super_file_name for x in contents]

    with open(new_directory + '/align.in', 'w') as z:
        for each in contents:
            z.write(each + '\n')

    os.chdir(directory.replace('/raw', ''))

    command = 'align_batch.csh ALOS align.in'
    p1 = Popen('source /shareddata/bashrc\n' + command, shell=True)
    p1.communicate()

    copyfile('/shareddata/batch.config', directory + '/batch.config')

    for line in fileinput.input(directory + '/batch.config', inplace = 1):
        print line.replace("master_image = ", "master_image = " + super_file_name).rstrip()

    os.chdir(new_directory)

    command2 = 'intf_batch.csh ALOS ' + directory  + '/intf.in ' + directory + '/batch.config'
    print command2

    p2 = Popen('source /shareddata/bashrc\n' + command2, shell=True)
    p2.communicate()


if __name__ == '__main__':
    main(sys.argv)