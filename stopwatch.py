#! python 3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "clickC the stopwatch. Press Ctrl-C to quit.')
input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1

# start tracking lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()

except KeyboardInterrupt:
    print('\nDone.')
