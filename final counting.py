import webbrowser
import time
url = "https://www.youtube.com/watch?v=iik25wqIuFo"
i = 5
while i>= 0:
    print(i)
    if i == 0:
        webbrowser.open(url,new=1)
    i -= 1
    time.sleep(1)