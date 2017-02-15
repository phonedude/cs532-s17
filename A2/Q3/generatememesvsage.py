import sys
import urllib2
import json
from datetime import *

current_datetime = datetime.now()

if len(sys.argv) != 3:
    print "Usage: Python generatememesvsage.py <input_file> <output_file>"
    print "e.g: Python generatememesvsage.py uniquelinkswithmemes.txt memesvsage.txt"
else:
    fh_input = open(sys.argv[1], 'r')
    fh_output = open(sys.argv[2], 'w')
    fh_output.write('ageX')
    fh_output.write('\t')
    fh_output.write('memesY')
    for line in fh_input:
        try:
            cr_link =  "http://cd.cs.odu.edu/cd?url=" + line
            me_link = "http://memgator.cs.odu.edu/timemap/json/" + line
            cr_response = urllib2.urlopen(cr_link)
            me_response = urllib2.urlopen(me_link)
            cr_data = json.load(cr_response)
            me_data = json.load(me_response)
            memes = len(me_data['mementos']['list'])
            memes = str(memes)
            creation_date = cr_data['Estimated Creation Date']
            creation_date = str(creation_date)
            fh_output.write('\n')
            if creation_date:
                creation_date_clean = creation_date[0:10]
                year_C = creation_date_clean.split('-')[0]
                month_C = creation_date_clean.split('-')[1]
                day_C = creation_date_clean.split('-')[2]
                month_C = month_C.lstrip("0")
                day_C = day_C.lstrip("0")
                year_C = int(year_C)
                month_C = int(month_C)
                day_C = int(day_C)
                date1 = date(year_C, month_C, day_C)
                today = date(current_datetime.year, current_datetime.month, current_datetime.day)
                old_in_days = (today - date1).days
                old_in_days = str(old_in_days)
                fh_output.write(old_in_days)
            else:
                fh_output.write('0')
            fh_output.write('\t')
            fh_output.write(memes)
            fh_output.write("\n")
        except:
            print "This link generated an error:"
            print line
    fh_input.close()
    fh_output.close()
