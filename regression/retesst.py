import re

data = 'Tue Mar 06 05:52:33 1979::vsymca@iqbqva.gov::289518753-6-6'

dayOfWeekReg = r'^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'

match = re.match(dayOfWeekReg, data)

if match is not None:
    print(match.group())
    print(match.group(1))
    print(match.groups())
else:
    print('Not match')

print('All things done')