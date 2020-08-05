import sys
import calendar
from datetime import datetime

"""
Class work
"""

l = len(sys.argv)

if l == 1:
    # User didn't specify any input
    month = datetime.now().month
    year = datetime.now().year
elif l == 2:
    # User didn'y specify year
    month = int(sys.argv[1])
    year = datetime.now().year
elif l == 3:
    # User specified both month and year
    month = int(sys.argv[1])
    year = int(sys.argv[2])
else:
    # User provided faulty input
    print("usage: 14_cal_alternative.py [month] [year]")
    sys.exit(1)

cal = calendar.TextCalendar()

cal.prmonth(year, month)
