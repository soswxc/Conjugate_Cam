from openpyxl import Workbook
from bs4 import BeautifulSoup

wb = Workbook()
ws = wb.active

with open('filing-details.html', encoding="UTF-8") as e:
    r = e.read()

soup = BeautifulSoup(r,'html.parser')
all_tables = soup.find_all('table')
table_list = []
for item in all_tables:
    if item.get('style') == "border-collapse:collapse;display:inline-table;vertical-align:top;width:100.000%" and item.text != "":
        table_list.append(item)

for table in table_list:
    rows = table.find_all('tr')
    for i,row in enumerate(rows):
        row_text = []
        col = row.find_all('td')
        for item in col:
            if i > 0 and item.text == "":
                continue
            if item.text == "$":
                continue
            row_text.append(item.text)

        ws.append(row_text)
wb.save("sample.xlsx")

