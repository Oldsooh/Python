import csv
import matplotlib.pyplot as plt

from datetime import datetime

file_name = 'network/test_files/sitka_weather_2014.csv'

days = []
highs = []
lows = []

with open(file_name, 'r') as fo:
    # creates a csv reader from a file handle delegated to csv file
    reader = csv.reader(fo)

    # Feteches the header row
    header_row = next(reader)
    # print(header_row)

    # Prints each column header with its index
    # for index, column_header in enumerate(header_row):
    #     print(str(index) + ': ' + str(column_header))

    for row in reader:
        day = datetime.strptime(row[0], '%Y-%m-%d')
        days.append(day)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

    # print(highs)

    # Creates figure
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(days, highs, c='red')
    plt.plot(days, lows, c='green')
    plt.fill_between(days, highs, lows, facecolor='blue', alpha=0.1)

    plt.title("Daily high temperature, 2014", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()

    plt.ylabel("Temperature(F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

    print('end')