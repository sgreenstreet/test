'''
This holds functions used by report_MPC_less.py.
'''

def pull_site_lines(f, code, year_want, month_want, day_want):
    '''
    This function pulls out the lines in a MPC report file (f) 
    for a given observatory code (code) and returns the list.
    '''
    f_less = []
    date_want = year_want + ' ' + month_want + ' ' + day_want
    for line in f:
        if code in line:
            if date_want in line:
                f_less.append(line)
    return f_less

def summarize_MPC_report(f_less):
    '''
    This function reduces the number of lines in a MPC report file (f) 
    for any observatory code (code) to 10 entries and rounds the 
    magnitude reported to one decimal place.
    '''
    report_line = []
    num_line = 0
    for line in f_less:
        #split the 80-column string into 3 parts to round the magnitude to one decimal place
        part1 = line[0:65]
        mag = line[65:70]
        part3 = line[70:]
        mag_num = float(mag)
        #the magnitude will likely never need to have more than one decimal place
        mag_num_round = round(mag_num, 1)
        if len(f_less) >= 10: #if have more than 10 entries
            num_line += 1
            #determine which every nth line to report
            if num_line % int(len(f_less)/10.) == 0:
                #force the number of output entries to be 10
                if len(report_line) < 10:
                    #append to new list (report_line) to put the full 80-column string back together with rounded magnitude
                    report_line.append([part1, mag_num_round, part3.rstrip()])
        else: #if have less than 10 entries already
            report_line.append([part1, mag_num_round, part3.rstrip()])
    return report_line

