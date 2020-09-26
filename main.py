

from bs4 import BeautifulSoup

import requests

html = requests.get("https://www.nfl.com/players/aaron-rodgers/stats/").content

soup = BeautifulSoup(html, "html.parser")
 # print(soup.prettify())

gb_stats = soup.find_all("th", class_="nfl-t-stats__col-16")
gb_numbers = soup.find_all("td", class_="nfl-t-stats__col-16")
head = []
data = []
for td in gb_numbers:
    data.append(td.string.strip())

# print(data[:17])

for th in gb_stats:
    head.append(th.string)


#print(head)

for td in gb_numbers:
    data.append(td.string.strip())


data2 = data[-17:]

#print(data[-17:])

for item in range(len(head)):
    print(f" {head[item]} - {data2[item]}")














