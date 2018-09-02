import os
import re

regression = r'([\w.]+(?:[\w.]+)*)\s\s+(\d+)\s+(\w+)\s\s+(\d+)\s\s+([\d,]+ K)'

with os.popen('tasklist /nh', 'r') as f:
    for line in f:
        matches = re.findall(regression, line.rstrip())
        if matches:
            print(matches)
        else:
            print(line.rstrip())

print('All things done')