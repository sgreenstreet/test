'''
This code will read in the MPC report file for 2003 RB and return 
every 8th entry from the LCOGT node at McDonald Observatory (V37) 
in addition to rounding the magnitude values to 0.1 mag.
'''

import sys

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
    #			print line,
			    print "%s%.1f %s"%(part1, mag_num_round, part3),
    return

MPC_file = open('2003_RB.dat')
summarize_MPC_report(MPC_file)
MPC_file.close()
