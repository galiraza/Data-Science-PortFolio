import requests
from bs4 import BeautifulSoup
import pandas as pd
# list to store data
data=[]

proceed=True # ya ik  Boolean variable ya condition check kernay ka liay for while loop
current_page=1 # ya webscrape kernay ka liay 1 page ha jo next page kaliay increment ho jay ga
while(True): # ya infinite loop ha chalti rhy gi jab tak isy brake na kia jiay
    print("Scraping Page No : " +str(current_page))
    url='https://quotes.toscrape.com/page/' + str(current_page)+'/'
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    qoutes=soup.find_all('div',class_='quote')
    for q in qoutes:
        item={} # ya empty dictionry ha jo scrped item ko store kray gi and phir data ka andar apend ker day gi
        item['name']=q.find('span',class_='text').text.strip()
        data.append(item)
    current_page+=1
    if current_page==11:
        break
    else:
        pass

    df=pd.DataFrame(data)
    df.to_csv('Qoutes.csv')
