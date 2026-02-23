# find_windows.py 
# search a distance time series and find the
# closest value to a supplied target distance, then print the
# time value corresponding to that distance

import numpy
import os

infile = open('dist.xvg', 'r')
lines = infile.readlines()

min_dist = 10000.0
time_of_min = 0.0
for line in lines:
    if not (line.startswith('#') or (line.startswith('@'))):
        tmp = line.split()
        time = float(tmp[0])
        distance = float(tmp[1])
        if (distance < min_dist):
            min_dist = distance
            time_of_min = time

print({min_dist:.3f}) {time_of_min:.1f})

count = 0
for d in numpy.arange(3.0, -0.1, -0.1):
    diff = 100000
    keeptime = 0
    keepdist = 0 
    for line in lines:
        if not (line.startswith('#') or (line.startswith('@'))):
            tmp = line.split()
            time = float(tmp[0])
            distance = float(tmp[1])

            if time > time_of_min:
                continue  

            tmpdiff = abs(d - distance)
            if (tmpdiff < diff):
                diff = tmpdiff
                keeptime = time
                keepdist = distance

    if keeptime > 0 or keepdist >= 0:
        cmd = "echo 0 | gmx trjconv -quiet -s pull.tpr -f pull.xtc -dump %f -o window%d.gro" % (keeptime, count)
        os.system(cmd)
        print("target value: %.1f best value: %.3f at time: %.1f" % (d, keepdist, keeptime))
        count += 1
    else:
        print(f" target value {d:.1f}")

exit()
