from bs4 import BeautifulSoup
import requests
# The .find('element', attrs={'attribute_name' : 'attribute_value'}). This finds the first element within the HTML soup
# The find._all ('element_name', attrs={'attribute_name' : 'attribute_value'}) gets all the elements within the html soup taht you run. Returns a list.
# The .get_text() grabs all the text from the HTML
# The .get('attribute_name') gets the name of an attribute
# so if you have <p class="example text"> and you did .get('class') it would 

response = requests.get("http://books.toscrape.com/index.html")
soup = BeautifulSoup(response.text, "html.parser")

print(soup)

first_book_price = soup.find('p', attrs={'class' : 'price_color'})
text = first_book_price.get_text()
print(text)