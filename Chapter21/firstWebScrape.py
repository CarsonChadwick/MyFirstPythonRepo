from bs4 import BeautifulSoup
import requests
import pandas as pd

oResponse = requests.get("http://books.toscrape.com/")

soup = BeautifulSoup(oResponse.text, 'html.parser')

myBooks= soup.find_all('a', {"title": "A Light in the Attic"})

for books in myBooks :
    print(books["href"])
# for childTag in soup.descendants :
  #   if (childTag.name == 'h3') :
    #     for newChildTag in childTag.descendants :
      #       if (newChildTag.name) :
        #         print(newChildTag.name)