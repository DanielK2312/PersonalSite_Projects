from bs4 import BeautifulSoup
from requests import get
import pandas as pd

"""Script to scrape searc results from car seller 
and make fle with listings found"""

headers = ({'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit\
/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})

base_url = "https://www.carroya.com/buscar/vehiculos/automovil/t4v1d30c71.do#paginaActual=1"
response = get(base_url, headers=headers)
html_soup = BeautifulSoup(response.text, 'html.parser')
content_list = html_soup.find_all('div', attrs={'class': 'car-ad sft-ad'})

basic_info = []
for item in content_list:
    basic_info.append(item.find_all('div', attrs={'class': 'car-ad-info'}))

names = []
for item in basic_info:
    for i in item:
        names.append(i.find_all(
            "h2", attrs={"class": "car-ad-name"})[0].text.strip())

years = []
for item in basic_info:
    for i in item:
        years.append(i.find_all(
            "h3", attrs={"class": "car-ad-year"})[0].text.strip())

prices = []
for item in basic_info:
    for i in item:
        prices.append(i.find_all("div", attrs={
                      "class": "car-ad-price"})[0].string.replace(u'\xa0', u' ').strip())

tables = []
motors = []
mileages = []
data = [motors, mileages]
for item in basic_info:
    for i in item:
        tables.append(i.find_all("table", attrs={
                      "class": "used-specs-table"})[0])
for table in tables:
    motors.append(table.find("td", attrs={"class": "car-ad-cc"}).string)
    mileages.append(table.find("td", attrs={"class": "car-ad-km"}).string)


data = pd.DataFrame({"Name": names, "Year": years, "Motor": motors, "Mileage (Km)": mileages, "Price": prices})[
    ["Name", "Year", "Motor", "Mileage (Km)", "Price"]]
data.head()
data.drop_duplicates().to_excel('Car_list.csv')
