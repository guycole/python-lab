#!/usr/bin/python
#
# Title:main.py
# Description: ECL code challenge solution
#
import json
import os
import sys


class Main:
    EXIT_HAPPY = 0
    EXIT_NO_FILE = 1
    EXIT_BAD_FILE = 2

    # raw id and scores
    scores = {}

    def parse_line(self, raw_line):
        """
        parse a line of format score: {json dictionary} and store result in scores dictionary
        :param raw_line: from data file
        :return: 0 if success w/results in scores dictionary else -1 for parse failure
        """
        buffer = raw_line.strip()
        if len(buffer) < 1:
            # empty line is OK
            return 0

        ndx0 = buffer.find(':')

        temp = buffer[:ndx0]
        score = int(temp)

        ndx1 = buffer.find('{')
        ndx2 = buffer.rfind('}')
        temp = buffer[ndx1:1+ndx2]

        try:
            parsed = json.loads(temp)
            id = parsed['id']
            if len(id) < 1:
                # empty key
                return -1

            self.scores[id] = score
        except KeyError:
            # missing key
            return -1

        return 0

    def read_file(self, full_file_name):
        """
        read data file, parse content and store results in scores dictionary
        :param full_file_name: fully qualified data file name
        :return: 0 = OK, 2 = file w/a badly formatted line
        """
        in_file = open(full_file_name, 'r')
        raw_buffer = in_file.readlines()
        in_file.close()

        retstat = self.EXIT_HAPPY

        line_counter = 0
        for raw_line in raw_buffer:
            line_counter = 1 + line_counter
            flag = self.parse_line(raw_line)
            if flag < 0:
                print("bad line:%d" % line_counter)
                retstat = self.EXIT_BAD_FILE

        return retstat

    def create_output(self, score_limit):
        """
        create dictionary sorted by scores
        :param score_limit: total output row count
        :return: results dictionary
        """
        results = []
        counter = 0
        for key, value in sorted(self.scores.items(), key=lambda item: (item[1], item[0]), reverse=True):
            if counter < score_limit:
                counter = 1 + counter
                temp = {}
                temp['id'] = key
                temp['score'] = value
                results.append(temp)

        return results

    def execute(self, full_file_name, score_limit):
        """
        read data file, sort by score and write json report
        :param full_file_name: fully qualified data file name
        :param score_limit: output row population
        :return: exit status 0 = good, 1 = file not found and 2 = bad file
        """
        if not os.path.isfile(full_file_name):
            return self.EXIT_NO_FILE

        retstat = self.read_file(full_file_name)
        if retstat == self.EXIT_HAPPY:
            results = self.create_output(score_limit)
            print(json.dumps(results))

        return retstat
#
# main driver
#
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage highest.py filename limit")
        sys.exit(0)

    file_name = sys.argv[1]
    limit = int(sys.argv[2])

    driver = Main()
    status = driver.execute(file_name, limit)
    sys.exit(status)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***