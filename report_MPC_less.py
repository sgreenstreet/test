'''
This code is to be used for 80-column MPC report files that have 
more than 10 entries. It will read in the MPC report file for any 
object and from any observatory code (both read in from the 
command line) and will return only 10 lines to report to the MPC. 
In addition, it will round the magnitude values to one decimal 
place.
To run, use the following command: 
python report_MPC_less.py ".dat file" "obs code"
'''

#allow reading arguments from the command line
import sys

#create new lists
f_less = []
report_line = []

'''
This function reduces the number of lines in a MPC report file (f) 
for any observatory code (code) to 10 entries and rounds the 
magnitude reported to one decimal place.
'''
def summarize_MPC_report(f, code):
    num_line = 0
    #create a new list of strings (f_less) from the input file only for obs code wanted
    for line in f:
        if code in line:
            f_less.append(line)
    #for each string in list f_less
    for line in f_less:
        num_line += 1
        #reduce the number of output entries to 10
        if num_line % int(len(f_less)/10.) == 0:
            #split the 80-column string into 3 parts to round the magnitude to one decimal place
            part1 = line[0:65]
            mag = line[65:70]
            part3 = line[70:]
            mag_num = float(mag)
            #the magnitude will likely never need to have more than one decimal place
            mag_num_round = round(mag_num, 1)
            #create a new list (report_line) to put the full 80-column string back together with rounded magnitude
            report_line.append([part1, mag_num_round, part3.rstrip()])          
    return report_line
    
#open file, call summarize_MPC_report function, close file
MPC_file = open(sys.argv[1],'r')

summarize_MPC_report(MPC_file,sys.argv[2])

MPC_file.close()

#print reduced number of entries (10) with one-decimal-place-rounded magnitude as a formatted 80-column string to standard output to be sent to the MPC
for i in range(len(report_line)):
    print "%s%.1f %s" % (report_line[i][0], report_line[i][1], report_line[i][2])

