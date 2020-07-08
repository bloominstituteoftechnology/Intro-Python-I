import sys
import calendar

from datetime import datetime

today = datetime.today()
month = today.month
year = today.year
cal = calendar.TextCalendar(firstweekday=6)

if len(sys.argv) == 1:
  calendar.prmonth(today.year, today.month)
elif len(sys.argv) == 2:
  calendar.prmonth(today.year, int(sys.argv[1]))
elif len(sys.argv) == 3:
  calendar.prmonth(int(sys.argv[2]), int(sys.argv[1]))
else:
  print("useage: filename month year")
  sys.exit(1)