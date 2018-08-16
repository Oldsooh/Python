import json

numbers = [1, 2, 3, 4, 5]

file_name = 'standard library/test_files/numbers.json'

with open(file_name, 'w') as file_object:
    json.dump(numbers, file_object)

print('Data was saved')


exist_numbers = []

with open(file_name, 'r') as file_object:
    exist_numbers = json.load(file_object)

print('The data loaded are:')
print(exist_numbers)
