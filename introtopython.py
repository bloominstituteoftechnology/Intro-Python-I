import webbrowser
import time

num = 0
print("This program started on " + time.ctime())
while num < 3:
    time.sleep(5)
    webbrowser.open("http://www.lambdaschool.com")
    num = num + 1