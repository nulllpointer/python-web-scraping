import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd

url_top_news = "https://www.imdb.com/news/top?ref_=nv_tp_nw"
url_box_office = "https://www.imdb.com/chart/boxoffice?ref_=nv_ch_cht"



page = requests.get(url_box_office)
soup = BeautifulSoup(page.text, 'html.parser')
# hero = soup.p['news-article-list']
'''
with open('imdb-top-news.csv', 'w') as f:
    for anchor in soup.find_all('h2', 'news-article__title'):
        f.write(anchor.get_text())
'''


# print(soup.find('table', {'class':'chart full-width'}))
table_data=soup.find('table', {'class': 'chart full-width'})

table_data_list = table_data.find_all('td')


# headline = soup.find(class_='ratingColumn')
# print(headline.string)

# for a in soup.find_all('td', 'ratingColumn'):
#     print(a.get_text())




ratingColumn=[t.get_text() for t in soup.find_all('span', 'secondaryInfo')]
titleColumn=[t.get_text() for t in soup.find_all('td', 'titleColumn')]
weeksColumn=[t.get_text() for t in soup.find_all('td', 'weeksColumn')]

data_output = {
               'titleColumn': titleColumn,
            'ratingColumn': ratingColumn,
            'weeksColumn': weeksColumn,

               }
df = pd.DataFrame(data_output, columns=['titleColumn','ratingColumn','weeksColumn'])
print(df)
df.to_csv('imdb.csv')





# titleColumn = [t.find(class_='ratingColumn').string for t in table_data]
# print(titleColumn)





