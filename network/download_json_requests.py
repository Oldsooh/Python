import requests
import pygal

json_file_name = 'network/test_files/btc_close_2017.json'
result_file_name = 'network/test_files/btc_close_result.svg'
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

req = requests.get(json_url)

with open(json_file_name, 'w') as f:
    f.write(req.text)

btc_data = req.json()

# print(btc_data)

dates = []
months = []
weeks = []
weekdays = []
close = []

for data in btc_data:
    dates.append(data['date'])
    months.append(int(data['month']))
    weeks.append(int(data['week']))
    weekdays.append(data['weekday'])
    close.append(int(float(data['close'])))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.x_title = 'BTC($)'
line_chart.x_labels = dates
line_chart.x_labels_major = dates[::20]
line_chart.add('BTC', close)

line_chart.render_to_file(result_file_name)

print('all things done')
