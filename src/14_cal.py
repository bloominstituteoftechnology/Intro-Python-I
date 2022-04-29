

import sys
import calendar
from datetime import datetime
print(sys.argv)
l = len(sys.argv)

if l == 1:
  month=datetime.now().month
  year=datetime.now().year
if l == 2:
  month=int(sys.argv[1])
  year=datetime.now().year
if l == 3:
  month=int(sys.argv[1])
  year=int(sys.argv[2])
else:
  print('error, please check formatting ')
  
cal = calendar.TextCalendar()
cal.prmonth(year, month)
