import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.yelp.com/menu/al-noor-lawndale-2"
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

csv_file = open("menu.csv", "w", newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['dish Name', 'Price'])
for i in range(0,71):
    stock=[]
    html_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_page.content, 'lxml')
    title=soup.find("div", class_="menu-sections").find_all("div", class_="menu-item")
    menu = title[i].find("div", class_="arrange_unit arrange_unit--fill menu-item-details").find("h4").get_text()
    value = title[i].find("div", class_="menu-item-prices arrange_unit").find("li").get_text()
    stock.append(menu.strip())
    stock.append(value.strip())
    csv_writer.writerow(stock)
csv_file.close()