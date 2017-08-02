import time 
import webbrowser

i = 0
timebreak = 3

print ("This programme started on "+time.ctime())
while i < timebreak:
    time.sleep(10)
    webbrowser.open('https://docs.python.org/2/library/webbrowser.html', new=2)
    timebreak = timebreak + 1
