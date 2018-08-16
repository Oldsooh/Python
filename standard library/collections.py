from collections import OrderedDict

user_names = OrderedDict()

user_names['richard'] = 'Richard Huang'
user_names['zoe'] = 'Zoe Tian'

for name, full_name in user_names.items():
    print(name + "'s full name is " + full_name) 