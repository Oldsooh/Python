import pygal

from die import Die

die = Die()

results = []
for roll in range(1000):
    result = die.roll()
    results.append(result)

print('The results of rolling D6 1000 times:')
print(results)

frequncies = []
for value in range(1, die.num_sides+1):
    frequncy = results.count(value)
    frequncies.append((value, frequncy))


print('The count of each sides:')
for frequncy in frequncies:
    print('The side ' + str(frequncy[0]) +
          ' has ' + str(frequncy[1]) + ' appeared times')

hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times'

x_labels = []
for side_number in range(1, die.num_sides):
    x_labels.append(str(side_number))

hist.x_labels = x_labels
hist._x_title = 'Result'
hist._y_title = 'Frequncy of Result'

sidesFrequncies = []
for frequncy in frequncies:
    sidesFrequncies.append(frequncy[1])

hist.add('D6', sidesFrequncies)

result_file_name = 'pygal/test_files/die_visual.svg'

print('Generating result...')
hist.render_to_file(result_file_name)

print('The result was saved to ' + result_file_name)
