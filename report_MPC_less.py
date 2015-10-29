'''
This code is to be used for 80-column MPC report files that have 
more than 10 entries. It will read in the MPC report file for any 
object and from any observatory code (both read in from the 
command line) and will return only 10 lines to report to the MPC. 
In addition, it will round the magnitude values to one decimal 
place.
To run, use the following command: 
python report_MPC_less.py ".dat file" "obs code" "obs date wanted (2015 09 03)"
'''

import sys #allow reading arguments from the command line
from report_MPC_less_subs import *
    
#open file, call summarize_MPC_report function, close file
MPC_file = open(sys.argv[1],'r')

site_only_lines = pull_site_lines(MPC_file,sys.argv[2],sys.argv[3])

report_line = summarize_MPC_report(site_only_lines)

MPC_file.close()

#print reduced number of entries (10) with one-decimal-place-rounded magnitude as a formatted 80-column string to standard output to be sent to the MPC
for i in range(len(report_line)):
    print "%s%.1f %s" % (report_line[i][0], report_line[i][1], report_line[i][2])

