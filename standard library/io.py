# with open('standard library/test_files/pi_digits.txt') as file_object:
#     for line in file_object:
#         print(line.rstrip())

from word_count import count_words

file_name = r'standard library/test_files/write_result.txt'
# with open(file_name, 'w') as file_object:
#     file_object.write('Test string\n')
#     file_object.write('The sceond line\n')


words_count = count_words(file_name)

print('The total words count: ' + str(words_count))