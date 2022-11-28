from selenium import webdriver
from bs4 import BeautifulSoup

Chrome = '/Users/jun/Desktop/实验室/开源项目/chromedriver'
browser = webdriver.Chrome(Chrome)
browser.get('https://numpy.org/about/#steering-council')
html = browser.page_source
# print(html)
soup = BeautifulSoup(html, 'lxml')
infos = soup.find_all(name='ul')
# print(infos)


# Crawl the data of steering council and store in dict 'council_data'
council_data = {"steering council": [], "emeritus": [], "teams": [], "subcommittee": []}
for i in range(len(infos)):
    names = infos[i].find_all(name='li')
    # print(names)
    if i == 0:
        for name in names:
            council_data['steering council'].append(name.string)
    if i == 1:
        for name in names:
            council_data['emeritus'].append(name.string)
    if i == 2:
        for name in names:
            council_data['teams'].append(name.string)
    if i == 3:
        for name in names:
            council_data['subcommittee'].append(name.string)

print(council_data)


# Crawl the data of teams and store in dict 'team_data'
browser.get('https://numpy.org/teams/')
html = browser.page_source
# print(html)
soup = BeautifulSoup(html, 'lxml')
infos = soup.find_all(attrs={'class': 'team'})
team_data = {"Maintainers": [],
             "Docs team": [],
             "Web team": [],
             "Triage team": [],
             "Survey team": [],
             "Emeritus maintainers": []}

for info in infos:
    members = info.find_all(attrs={'class': 'member'})
    for member in members:
        tmp_data = {"name": member.a.text, "github_link": member.a.attrs['href']}
        if info.find(attrs={'class': 'name title'}).string == "Maintainers":
            team_data['Maintainers'].append(tmp_data)
        elif info.find(attrs={'class': 'name title'}).string == "Docs team":
            team_data['Docs team'].append(tmp_data)
        elif info.find(attrs={'class': 'name title'}).string == "Web team":
            team_data['Web team'].append(tmp_data)
        elif info.find(attrs={'class': 'name title'}).string == "Triage team":
            team_data['Triage team'].append(tmp_data)
        elif info.find(attrs={'class': 'name title'}).string == "Survey team":
            team_data['Survey team'].append(tmp_data)
        elif info.find(attrs={'class': 'name title'}).string == "Emeritus maintainers":
            team_data['Emeritus maintainers'].append(tmp_data)

print(team_data['Maintainers'])
