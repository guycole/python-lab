#! /usr/bin/python
#
# Title:price_converter.py
# Description: convert raw session files
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import subprocess
import sys
import time

def load_names(infile_name):
    names = {}

    with open(infile_name, "r") as infile:
        input_buffer = infile.readlines()

        for element in input_buffer:
            tokens = element.split('|')
            tuple2 = (tokens[0].strip(), tokens[1].strip(), tokens[2].strip())
        #       ('4991461', 'RSH21', 'WCE')
            names[tokens[0].strip()] = tuple2

    print "names loaded length:%d" % len(names)

    return names

def fix_file(candidate, raw_data_directory, temp_directory):
    name_id = candidate[0]
    market = candidate[2].lower()

    infile_name = "%s/session%s.txt" % (raw_data_directory, name_id)
    print "fix_file:%s" % infile_name

    if not os.path.isfile(infile_name):
        sys.exit("ERROR: fix_file missing file:%s" % infile_name)

    test_directory = "%s/%s" % (temp_directory, market)
    if not os.path.exists(test_directory):
        print "fix_file create directory:%s" % test_directory
        os.mkdir(test_directory)

    txt_file_name = "%s/%s-%s.txt" % (market, market, name_id)
    full_file_name = "%s/%s" % (temp_directory, txt_file_name)

    with open(infile_name, "r") as infile:
        input_buffer = infile.readlines()

    first_flag = 1
    output_datum = []
    for element in input_buffer:
        # skip header row
        if first_flag > 0:
            first_flag = 0
            continue

        tokens = element.split('\t')
        if len(tokens) != 11:
            sys.exit("ERROR: fix_file bad token count:%s:%s" % (infile_name, element))

        row_tuple = (tokens[3].strip(), tokens[4].strip(), int(tokens[5].strip()), int(tokens[6].strip()), int(tokens[7].strip()), int(tokens[8].strip()), int(tokens[9].strip()), int(tokens[10].strip()))
        output_datum.append(row_tuple)

    print("creating:%d:%s" % (len(output_datum), full_file_name))

    with open(full_file_name, "w") as outfile:
        outfile.write("name_id | date | open_price | high_price | low_price | close_price | volume | open_interest |\n")

        for element in output_datum:
            output_formatted = "%s | %s | %s | %s | %s | %s | %s | %s |\n" % (element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7])
            outfile.write(output_formatted)

def shell_call(command):
    for attempt in range(128):
        print "attempt:%d" % attempt

        retstat = subprocess.call(command)
        if retstat == 0:
            print "retstatus happy"
            return retstat
        else:
            print "sleep for next attempt"
            time.sleep(1)

    return retstat

def zip_file(candidate, archive_directory, temp_directory):
    os.chdir(temp_directory)

    name_id = candidate[0]
    market = candidate[2].lower()

    txt_file_name = "%s/%s-%s.txt" % (market, market, name_id)
    zip_file_name = "%s/%s-%s.zip" % (market, market, name_id)

    if not os.path.isfile(txt_file_name):
        sys.exit("ERROR: zip_file missing file:%s" % txt_file_name)

    test_directory = "%s/%s" % (archive_directory, market)
    if not os.path.exists(test_directory):
        print "zip_file create directory:%s" % test_directory
        os.mkdir(test_directory)

    command = ["/usr/bin/zip", "-q", zip_file_name, txt_file_name]
    retstat = shell_call(command)
    if retstat != 0:
        sys.exit("zip retry exceeded bad retstat %d" % retstat)

    fresh_file_stat = os.stat(zip_file_name)
    fresh_file_size = fresh_file_stat.st_size

    reference_file_name = "%s/%s" % (archive_directory, zip_file_name)
    if os.path.isfile(reference_file_name):
        reference_file_stat = os.stat(reference_file_name)
        reference_file_size = reference_file_stat.st_size
    else:
        print "missing reference file"
        reference_file_size = 0

    if fresh_file_size == reference_file_size:
        os.unlink(zip_file_name)
    else:
        print "file size match failure"
        command = ["/bin/mv", zip_file_name, reference_file_name]
        retstat = shell_call(command)
        if retstat != 0:
            sys.exit("mv retry exceeded bad retstat %d" % retstat)

print 'start'

if __name__ == '__main__':
    print 'main'

    archive_directory = '/mnt/raid0/gsc/bigload/prices'
    archive_directory = '/Users/gsc/IdeaProjects/python-lab/eoddata/archive'

    data_directory = '/mnt/raid0/gsc/archiver'
    data_directory = '/Users/gsc/IdeaProjects/python-lab/eoddata/raw_test_files'

    temp_directory = '/mnt/raid0/gsc/prices'
    temp_directory = '/tmp'

    name_file = '/home/gsc/github/mythic-crux-aws/archiver/master_names.txt'
    name_file = '/Users/gsc/IdeaProjects/python-lab/eoddata/master_names.txt'

    name_dictionary = load_names(name_file)
    if len(name_dictionary) != 4991462:
        sys.exit('short name dictionary read')

    lower_bound = 1
    upper_bound = 4991462
    upper_bound = 499
    for ndx in range(lower_bound, upper_bound):
        print("current ndx:%d of %d (%d)" % (ndx, upper_bound, (upper_bound - ndx)))
        fix_file(name_dictionary[str(ndx)], data_directory, temp_directory)
        zip_file(name_dictionary[str(ndx)], archive_directory, temp_directory)

print 'stop'