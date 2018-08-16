
try:
    # result = 5 / 0
    result = 5 / 1
except ZeroDivisionError as ex:
    print('You cannot divide by zero!\n' + str(ex))
else:
    print(result)

print('something here')