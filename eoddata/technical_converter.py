#! /usr/bin/python
#
# Title:technical_converter.py
# Description:
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
    #
    # read the files in raw_data_directory and format/convert them w/results in temp_directory
    #

    name_id = candidate[0]
    market = candidate[2].lower()

    infile_name = "%s/techie%s.txt" % (raw_data_directory, name_id)
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
        if len(tokens) != 33:
            sys.exit("ERROR: fix_file bad token count:%s:%s" % (infile_name, element))

        raw_tuple = (tokens[2].strip(), tokens[3].strip(), float(tokens[4].strip()), float(tokens[5].strip()), int(tokens[6].strip()), float(tokens[7].strip()), float(tokens[8].strip()), float(tokens[9].strip()), float(tokens[10].strip()), int(tokens[11].strip()), float(tokens[12].strip()), float(tokens[13].strip()), float(tokens[14].strip()), float(tokens[15].strip()), int(tokens[16].strip()), float(tokens[17].strip()), float(tokens[18].strip()), float(tokens[19].strip()), float(tokens[20].strip()), int(tokens[21].strip()), int(tokens[22].strip()), int(tokens[23].strip()), int(tokens[24].strip()), int(tokens[25].strip()), int(tokens[26].strip()), float(tokens[27].strip()), float(tokens[28].strip()), float(tokens[29].strip()), float(tokens[30].strip()), float(tokens[31].strip()), int(tokens[32].strip()))
        output_datum.append(raw_tuple)

    if len(output_datum) < 1:
        print("skipping empty candidate %s" % name_id)
        return 0

    print("creating:%d:%s" % (len(output_datum), full_file_name))

    with open(full_file_name, "w") as outfile:
        outfile.write("name_id | tar_file_name | previous | change | volume_change | week_high | week_low | week_change | avg_week_change | avg_week_volume | month_high | month_low | month_change | avg_month_change | avg_month_volume | year_high | year_low | year_change | avg_year_change | avg_year_volume | ma5 | ma20 | ma50 | ma100 | ma200 | rsi14 | sto9 | wpr14 | mtm14 | roc14 | ptc |\n")

        for element in output_datum:
            output_formatted = "%s | %s | %f | %f | %d | %f | %f | %f | %f | %d | %f | %f | %f | %f | %d | %f | %f | %f | %f | %d | %d |  %d | %d | %d | %d | %f | %f | %f | %f | %f | %d |\n" % (element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9], element[10], element[11], element[12], element[13], element[14], element[15], element[16], element[17], element[18], element[19], element[20], element[21], element[22], element[23], element[24], element[25], element[26], element[27], element[28], element[29], element[30])
            outfile.write(output_formatted)

    return len(output_datum)


def shell_call(command):
    print command

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


def zip_file2(candidate):
    outfile_base = '/mnt/raid0/gsc/technicals'
    os.chdir(outfile_base)

    market = candidate[2].lower()

    txt_file_name = "%s/%s-%s.txt" % (market, market, candidate[0])
    zip_file_name = "%s/%s-%s.zip" % (market, market, candidate[0])

    if not os.path.isfile(txt_file_name):
        sys.exit("ERROR: missing text file:%s" % txt_file_name)

    command = "/usr/bin/zip -q %s %s" % (zip_file_name, txt_file_name)
    retstat = system_call(command)
    if retstat != 0:
        sys.exit("zip retry exceeded bad retstat %d" % retstat)

    fresh_file_stat = os.stat(zip_file_name)
    fresh_file_size = fresh_file_stat.st_size

    sync_base = '/mnt/raid0/gsc/bigload/technicals'
    reference_file_name = "%s/%s" % (sync_base, zip_file_name)
    if os.path.isfile(reference_file_name):
        reference_file_stat = os.stat(reference_file_name)
        reference_file_size = reference_file_stat.st_size
    else:
        print("missing reference file %s" % reference_file_name)
        reference_file_size = 0

    if fresh_file_size == reference_file_size:
        os.unlink(zip_file_name)
    else:
        print("file size match failure")

        if not os.path.isfile(zip_file_name):
            print "ERROR: missing zip file:%s" % zip_file_name

        command = "/bin/mv %s %s" % (zip_file_name, reference_file_name)
#        retstat = system_call(command)
#        if retstat != 0:
#            sys.exit("mv retry exceeded bad retstat %d" % retstat)

print 'start'

if __name__ == '__main__':
    print 'main'

    # for sync to s3
    archive_directory = '/mnt/raid0/gsc/bigload/prices'
    archive_directory = '/Users/gsc/IdeaProjects/python-lab/eoddata/archive'

    # files from mysql
    data_directory = '/mnt/raid0/gsc/archiver'
    data_directory = '/Users/gsc/IdeaProjects/python-lab/eoddata/raw_test_files'

    # temporary files
    temp_directory = '/mnt/raid0/gsc/tech'
    temp_directory = '/tmp'

    # id, symbol, market
    name_file = '/home/gsc/github/mythic-crux-aws/archiver/master_names.txt'
    name_file = '/Users/gsc/IdeaProjects/python-lab/eoddata/master_names.txt'

    name_dictionary = load_names(name_file)
    if len(name_dictionary) != 4991462:
        sys.exit('short name dictionary read')

    lower_bound = 1
    upper_bound = 1663820
#    lower_bound = 1663820
#    upper_bound = 3327640
#    lower_bound = 3327640
#    upper_bound = 4991462
    for ndx in range(lower_bound, upper_bound):
        print("current ndx:%d of %d (%d)" % (ndx, upper_bound, (upper_bound - ndx)))
        row_count = fix_file(name_dictionary[str(ndx)], data_directory, temp_directory)
        if row_count > 0:
            zip_file(name_dictionary[str(ndx)], archive_directory, temp_directory)

print 'stop'
