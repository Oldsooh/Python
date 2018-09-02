import re

data_path = r"regression/test_files/whoadat.txt"

with open(data_path,'r') as f:
    for line in f:
        print(re.split(r'\s\s+|\t', line.rstrip()))

print('Complete')