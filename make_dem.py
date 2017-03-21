import subprocess
from subprocess import Popen, PIPE
import os
import re
import shutil
import itertools
import time
import string
import sys

def file_finder(long1, long2, lat1, lat2, directory_final):
    """
    The code below determines the longitude and latitude bounds
    After finding the bounds, we store them in a list for easy accessibility
    """

    os.chdir('/shareddata/GRD_SRTM4.1')

    lat1lower = lat1 - (lat1 % 5)
    lat1upper = lat1lower + 5
    latlower = lat1lower

    lat2lower = lat2 - (lat2 % 5)
    if (lat2 % 5 == 0):
        lat2upper = lat2
    else:
        lat2upper = lat2lower + 5
    latupper = lat2upper

    long1lower = long1 - (long1 % 5)
    long1upper = long1lower + 5
    longlower = long1lower

    long2lower = long2 - (long2 % 5)
    if (long2 % 5 == 0):
        long2upper = long2
    else:
        long2upper = long2lower + 5
    longupper = long2upper


    # coords to save: lat1lower, lat2upper, long1lower, long2upper
    bounds = [long1lower, long2upper, lat1lower, lat2upper]

    """
    The two lists below are used to store all of the possible longitude and latitude coordinates so that
    we know which .grd files we are going to include in the filelist that we build later

    We initialize the lists with the first unchanged values of lat1lower and long1lower
    """

    lats = [lat1lower]
    longs = [long1lower]
    """
    The code below first finds the delta values for the longitude and latitude, and then divides it by 5
    so that we know how many points we will need, which lets us know how many files we will have in our filelist
    """
    lat_delta = lat2upper - lat1lower
    long_delta = long2upper - long1lower

    lat_add = lat_delta / 5
    long_add = long_delta / 5

    """
    We loop up to the values lat_add and long_add, add 5 to them during every iteration of the loop, and then add
    them to the lists that we previously created. After these sections of code execute, we have all the longitude
    and latitude coordinates and can construct our filelist
    """
    i = 1
    while i < lat_add:
        lat1lower += 5
        lats.append(lat1lower)
        i += 1

    j = 1
    while j < long_add:
        long1lower += 5
        longs.append(long1lower)
        j += 1
    """
    We sort each list of coordinates so that our files are written into the filelist in the proper order
    """
    lats = (sorted(lats))
    longs = (sorted(longs))

    lats = [int(x) for x in lats]
    longs = [int(x) for x in longs]


    """
    The following lines of code match each value in the latitude coordinates with each value in the longitude
    coordinates.

    For example: lats = [0,5,10] longs = [20,25]
    Output = [[0,20],[0,25],[5,20],[5,25],[10,20],[10,25]]
    """
    files = list(itertools.product(lats,longs))
    files = [list(element) for element in files]

    file_list = []
    """
    At this point we look to see what the values of the coordinates are, specifically to see if they're positive or
    negative. This information allows us to properly name the files in the filelist.
    """
    for each_file in files:
        first_letter = ''
        second_letter = ''
        new_filename = ''

        if each_file[0] < 0:
            first_letter = 'S'
        else:
            first_letter = 'N'
        if each_file[1] < 0:
            second_letter = 'W'
        else:
            second_letter = 'E'
        """
        Here, we construct the file name using our variables in the proper order, and strip out any negative signs.
        Finally, we add the filename to the list of files.
        """
        new_filename = first_letter + str(each_file[0]) + second_letter + str(each_file[1]) + '.grd'
        new_filename = new_filename.replace('-', '')
        file_list.append(new_filename)

    """
    Here, we loop through the list of files and write each filename into a file called "filelist". This is done with a
    new line character after each filename so that the file is written in the format of 1 filename per line.
    """
    temp_file = open('filelist', 'w')
    for x in file_list:
        temp_file.write(x + '\n')
    temp_file.flush()
    time.sleep(5)
    """
    Here, we make our 2 shell commands, grdblend and grdcut. If filelist only contains 1 file, grdblend will prompt you
    and will immediately skip to grdcut.
    """
    p = Popen('/opt/local/bin/gmt grdblend filelist -R' + str(longlower) + '/' + str(longupper) + '/' + str(latlower) + '/' + str(latupper) + ' -I3s -N0 -G' + directory_final + '/' + 'all.grd', shell=True)
    p.wait()
    Popen('/opt/local/bin/gmt grdcut ' + directory_final + '/' + 'all.grd' + ' -G' + directory_final + '/' + 'dem.grd -R' + str(long1) + '/' + str(long2) + '/' + str(lat1) + '/'+ str(lat2), shell=True)

    os.remove('filelist')
