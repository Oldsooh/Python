import re

data = 'Tue Mar 06 05:52:33 1979::vsymca@iqbqva.gov::289518753-6-6'

pattern = r'.+:(\d+-\d+-\d+)'

match = re.match(pattern, data)

if match is not None:
    print(match.groups())
else:
    print('Not match')

print('All things done')