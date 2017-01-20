from subprocess import PIPE,Popen
import shutil
import os
import re

def main():
    directory = "/Users/student/Desktop/unzipped_files"
    #directory = "/Users/student/Desktop/test"
    os.chdir(directory)
    grd_commands(directory)


def grd_commands(directory):
    for filename in os.listdir(directory)[1:]:
        print filename
        new_filename = ''
        first_letter = ''
        second_letter = ''
        bash_command = '/opt/local/bin/gmt grdinfo ' + filename + ' -I-'
        #print bash_command
        coordinates = Popen(bash_command, stdout=PIPE, shell=True)
        coordinates = coordinates.communicate()
        latlong = re.findall(r'^\D*?([-+]?\d+)\D*?[-+]?\d+\D*?([-+]?\d+)', str(coordinates))[0]
        #print latlong
        if '-' in latlong[1]:
            first_letter = 'S'
        else:
            first_letter = 'N'
        if '-' in latlong[0]:
            second_letter = 'W'
        else:
            second_letter = 'E'

        new_filename = first_letter + str(latlong[1]) + second_letter + str(latlong[0]) + '.grd'
        new_filename = new_filename.replace('-', '')
        print new_filename
        Popen('/opt/local/bin/gmt grdconvert ' + str(filename) + ' ' + new_filename, shell=True)


if __name__ == '__main__':
    main()