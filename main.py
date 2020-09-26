# peso = int(input("Seu peso: "))
# tipo = input("l or k ")

# if tipo.upper() == "L":
#  converted = (peso * 0.45)
# print(f" Você pesa {converted}kg ")
# elif tipo.upper() == "K":
# converted = (peso // 0.45)
# print(f" Você pesa {converted} lbs")


# numbers = [1, 1, 1, 1, 7]

# for x_count in numbers:
#  output = ""
# for count in range(x_count):
#    output += "x"
# print(output)


# numbers = [2, 4, 10, 20, 32, 9, 73, 7, 17]
# numbers.insert(0, 12)
# print(numbers)
"""
numero = int(input("Escolha um numero "))
numbers = [20, 10, 12, 12, 10, 42]

if numbers.count(numero):
    print("Numero aparece mais de uma vez")
else:
    print("Numero único")
"""

# def nome(name):
#  print(f"Hello {name}")


# nome("Lucas")

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














