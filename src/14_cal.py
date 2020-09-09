import sys
import calendar
from datetime import datetime

#print (type(sys.argv[2]))
today = datetime.today()
cal = calendar.TextCalendar()
#print (sys.argv)
if (len(sys.argv)==1):
  print(cal.prmonth(today.year,today.month))
elif (len(sys.argv)==2):
  print(cal.prmonth(today.year,int(sys.argv[1])))
elif (len(sys.argv)==3):
  print(cal.prmonth(int(sys.argv[2]),int(sys.argv[1])))
else:
  print("Error! Usage: Python3 14_cal.py <month> <year>")