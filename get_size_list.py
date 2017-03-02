# -*- coding: utf-8 -*-

import sys
import csv

script_name = sys.argv[0]

try:
    infile = sys.argv[1]
    with open(infile, 'r') as fin:
        lines = fin.readlines()
except IndexError:
    print 'Usage: %s map-file out-file' % script_name
    quit()
except IOError:
    print '"%s" cannot be opened.' % infile
    quit()

try:
    outfile = sys.argv[2]
    with open(outfile, "r") as fref:
        csvReader = csv.reader(fref)
        ref_header = list(csvReader)[0]
except IndexError:
    print 'Usage: %s map-file out-file' % script_name
    quit()
except IOError:
    ref_header = []

header = []
size = []
with open(outfile, "ab") as fout:
    for line in lines:
        if line.find("Execution Region") >= 0:
            data = line.split()
            header.append(data[2])
            size.append(int(data[4].replace(',',''), 16))
    csvWriter = csv.writer(fout)
    if ref_header is None:
        csvWriter.writerow(header)
    elif ref_header != header:
        print 'warning: map layout change!!'
        print 'old: %s' % ref_header
        print 'current: %s' % header
        quit()
    csvWriter.writerow(size)

