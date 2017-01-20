import os
import subprocess
from subprocess import Popen, PIPE
import sys
from itertools import combinations


def generate_pairs(table_file, threshold):
    num_args = len(sys.argv)
    #print num_args

    if num_args < 2:
        print "Input: table.gmt file path [baseline_threshold to choose]"
        sys.exit()
    elif num_args < 3:
        base = 700
    else:
        base = sys.argv[2]

    directory = os.getcwd() + '/'
    #print directory

    with open(directory + table_file, 'r') as table:
        contents = table.readlines()

    contents = [x.strip('\n') for x in contents]

    days = []
    baseline = []
    orbit_number = []

    for image in contents:
        days.append(image.split(' ')[0])
        baseline.append(image.split(' ')[1])
        orbit_number.append(image.split(' ')[6])

    days = [int(x) for x in days]
    baseline = [float(x) for x in baseline]

    baseline_pairs = [(i, j) for i, j in combinations(baseline, 2) if abs(j - i) <= float(base)]

    if len(baseline_pairs) == 0:
        print "There are no pairs"
        sys.exit()

    # print baseline_pairs

    temp_days = []

    for each in baseline_pairs:
        pos1 = baseline.index(each[0])
        pos2 = baseline.index(each[1])
        temp_day = days[pos1], days[pos2]
        temp_days.append(temp_day)

    #print temp_days

    # print len(baseline_pairs)
    # print len(temp_days)

    pairs = []

    for each in temp_days:
        x = each[0]
        y = each[1]


        if (float(y) - float(x)) > 200:
            remainder = (float(y) - float(x)) % 365
            #print remainder
            if remainder < 60 or remainder > 305:
                pair = x, y
                pairs.append(pair)

        """if x > 365 and y < 365:
            delta = x / 365
            new_x = x - (delta * 365)
            if abs(new_x - y) <= 60:
                pair = x, y
                pairs.append(pair)
        if x < 365 and y > 365:
            delta = y / 365
            new_y = y - (delta * 365)
            if abs(x - new_y) <= 60:
                pair = x, y
                pairs.append(pair)
        if x > 365 and y > 365:
            delta1 = x / 365
            new_x = x - (delta1 * 365)
            delta2 = y / 365
            new_y = y - (delta2 * 365)
            if abs(new_x - new_y) <= 60:
                pair = x, y
                pairs.append(pair)
        if x < 365 and y < 365:
            if abs(x - y) <= 60:
                pair = x, y
                pairs.append(pair)"""

    # print pairs

    final_pairs = []

    for each in pairs:
        pos1 = days.index(each[0])
        pos2 = days.index(each[1])
        final_pair = orbit_number[pos1], orbit_number[pos2]
        final_pairs.append(final_pair)

    #print final_pairs

    intf = open(directory + 'intf.in', 'w')
    all_files = os.listdir(directory)
    all_files = [x for x in all_files if 'PRM' not in x]
    all_files = [x for x in all_files if 'raw' not in x]
    all_files = [x for x in all_files if 'LED' not in x]
    all_files = [x for x in all_files if '__A' in x]
    #print all_files

    for each in final_pairs:
        first = [x for x in all_files if each[0] in x][0]
        second = [x for x in all_files if each[1] in x][0]

        intf.write(str(first) + ':' + str(second) + '\n')

    intf.flush()


