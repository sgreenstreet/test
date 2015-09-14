'''
This code will read in the MPC report file for any object and return 
every 8th entry from the LCOGT node at McDonald Observatory (V37) 
in addition to rounding the magnitude values to one decimal place.
'''

import sys

report_line = []

def summarize_MPC_report(f):
    num_line = 0
    for line in f:
        if 'V37' in line:
            num_line += 1
            if num_line % 8 == 0:
                part1 = line[0:65]
                mag = line[65:70]
                part3 = line[70:]
                mag_num = float(mag)
                mag_num_round = round(mag_num, 1)
                report_line.append([part1, mag_num_round, part3.rstrip()])
    return report_line

MPC_file = open(sys.argv[1],'r')

summarize_MPC_report(MPC_file)

MPC_file.close()

for i in range(len(report_line)):
    print "%s%.1f %s" % (report_line[i][0], report_line[i][1], report_line[i][2])
