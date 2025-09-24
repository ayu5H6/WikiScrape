from bs4 import BeautifulSoup
import requests

url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_India"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

page=requests.get(url,headers=headers)
print(page)
info=BeautifulSoup(page.text,"html.parser")
table=info.find_all('table')[0]
titles=table.find_all('th')
# print(titles)
world_titles=[title.text.strip() for title in titles]
# print(world_titles)

import pandas as pd
df=pd.DataFrame(columns=world_titles)
# print(df)

column_data=table.find_all('tr')
for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    if individual_row_data and len(individual_row_data)==len(world_titles):
        length=len(df)
        df.loc[length]=individual_row_data
print(df)
df.to_csv(r'C:\Users\ayush\OneDrive\Desktop\Analyst\Scraping\Companies.csv')