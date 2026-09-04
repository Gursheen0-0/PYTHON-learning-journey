# for loops= execute a block of code fixed number of times
""" for x in reversed(range(1,6)):
    print(x)
print("this is countdown")
"""

import time

timer= int(input("How long you want the countdown to: "))
for x in (range(timer, 0, -1)):
    seconds = x%60
    minutes= int(x/60) % 60
    hours = int(x /3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("time's up")