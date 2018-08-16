def change_list(list):
    """ Removes the first item from list"""
    if list:
        value = list[0]
        del list[0]
        print(value + ' has been removed from list')


def print_list(list):
    if list:
        for item in list:
            print(item + ',')
    else:
        print('The target list is emtpy')


list = ['Richard', 'Zoe', 'Joy']

print_list(list)
change_list(list)
change_list(list[:])
print_list(list)