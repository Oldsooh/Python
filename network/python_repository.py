import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


api_url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

response = requests.get(api_url)


status_code = response.status_code
result = []
total_repositories_count = 0


if status_code != 200:
    print('ERROR:' + str(status_code))
else:
    result = response.json()

if result:
    total_repositories_count = result['total_count']
    returned_repositories = result['items']


print('total repositories count: ' + str(total_repositories_count))

# first_repository = returned_repositories[0]

# for key in sorted(first_repository.keys()):
#     print(key)


names, stars = [], []
for repo in returned_repositories:
    name = repo['name']
    names.append(name)

    star_count = repo['stargazers_count']
    # description = repo['description']
    url_link = repo['html_url']

    description = 'The total stars of ' + name
    star = {
        'value': star_count, 
        'label': description,
        'xlink': url_link}
    stars.append(star)

chart_style = LS('#333366', base_style=LCS)
chart_config = pygal.Config()
chart_config.show_legend = False
chart_config.title_font_size = 24
chart_config.label_font_size = 14
chart_config.major_label_font_size = 18
chart_config.truncate_label = 15
chart_config.show_y_guides = False
chart_config.width = 1000

chart = pygal.Bar(chart_config, style=chart_style,
                  x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file(
    'network/test_files/Most-Starred-Python-Projects-on-GitHub.svg')

print('The end')
