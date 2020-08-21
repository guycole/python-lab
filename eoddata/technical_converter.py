#! /usr/bin/python
#
# Title:techie3a.py
# Description:
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import sys
import time

def load_names():
    print 'load names'
    names = {}
    infile_name = '/home/gsc/github/mythic-crux-aws/archiver/master_names.txt'

    with open(infile_name, "r") as infile:
        input_buffer = infile.readlines()

    for element in input_buffer:
        tokens = element.split('|')
        tuple2 = (tokens[0].strip(), tokens[1].strip(), tokens[2].strip())
#       ('4991461', 'RSH21', 'WCE')
        names[tokens[0].strip()] = tuple2

    return names


def system_call(command):
    print command

    for attempt in range(128):
        print "attempt:%d" % attempt 

        retstat = os.system(command)
        if retstat == 0:
            print "retstatus happy" 
            return 0
        else:
            print "sleep for next attempt" 
            time.sleep(1)

    return retstat 


def fix_file(candidate):
    infile_file_name = "/mnt/raid0/gsc/tech/techie%s.txt" % (candidate[0])

    if not os.path.isfile(infile_file_name):
        print("missing raw sql file:%s" % infile_file_name)
        return 0

    with open(infile_file_name, "r") as infile:
        input_buffer = infile.readlines()

    first_flag = 1
    output_datum = []
    for element in input_buffer:
        if first_flag > 0:
            first_flag = 0
            continue

        tokens = element.split('\t')

        if len(tokens) > 35:
            print(element)
            print(len(tokens))
            print("bad file:%s" % infile_file_name)

        tuple2 = (tokens[2].strip(), tokens[3].strip(), float(tokens[4].strip()), float(tokens[5].strip()), int(tokens[6].strip()), float(tokens[7].strip()), float(tokens[8].strip()), float(tokens[9].strip()), float(tokens[10].strip()), int(tokens[11].strip()), float(tokens[12].strip()), float(tokens[13].strip()), float(tokens[14].strip()), float(tokens[15].strip()), int(tokens[16].strip()), float(tokens[17].strip()), float(tokens[18].strip()), float(tokens[19].strip()), float(tokens[20].strip()), int(tokens[21].strip()), int(tokens[22].strip()), int(tokens[23].strip()), int(tokens[24].strip()), int(tokens[25].strip()), int(tokens[26].strip()), float(tokens[27].strip()), float(tokens[28].strip()), float(tokens[29].strip()), float(tokens[30].strip()), float(tokens[31].strip()), int(tokens[32].strip()))
        output_datum.append(tuple2)

    if len(output_datum) < 1:
        print("skipping empty candidate %s" % candidate[0])
        return 0

    outfile_base = '/mnt/raid0/gsc/technicals'
    market = candidate[2].lower()

    txt_file_name = "%s/%s-%s.txt" % (market, market, candidate[0])
    full_file_name = "%s/%s" % (outfile_base, txt_file_name)
    print("creating:%d:%s" % (len(output_datum), full_file_name))

    with open(full_file_name, "w") as outfile:
        outfile.write("name_id | tar_file_name | previous | change | volume_change | week_high | week_low | week_change | avg_week_change | avg_week_volume | month_high | month_low | month_change | avg_month_change | avg_month_volume | year_high | year_low | year_change | avg_year_change | avg_year_volume | ma5 | ma20 | ma50 | ma100 | ma200 | rsi14 | sto9 | wpr14 | mtm14 | roc14 | ptc |\n") 

        for element in output_datum:
            output_formatted = "%s | %s | %f | %f | %d | %f | %f | %f | %f | %d | %f | %f | %f | %f | %d | %f | %f | %f | %f | %d | %d |  %d | %d | %d | %d | %f | %f | %f | %f | %f | %d |\n" % (element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9], element[10], element[11], element[12], element[13], element[14], element[15], element[16], element[17], element[18], element[19], element[20], element[21], element[22], element[23], element[24], element[25], element[26], element[27], element[28], element[29], element[30])
            outfile.write(output_formatted)

    return len(output_datum)


def zip_file(candidate):
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
        retstat = system_call(command) 
        if retstat != 0:
            sys.exit("mv retry exceeded bad retstat %d" % retstat)

print 'start'

if __name__ == '__main__':
    print 'main'
    name_dictionary = load_names()

#    for ndx in range(1425520, 4991462):
#    for ndx in range(1, 1663821):

    lower_bound = 130465
    upper_bound = 1663821
    for ndx in range(lower_bound, upper_bound):
        print("current ndx:%d of %d (%d)" % (ndx, upper_bound, (upper_bound - ndx)))
        if fix_file(name_dictionary[str(ndx)]) > 0:
            zip_file(name_dictionary[str(ndx)])

print 'stop'
