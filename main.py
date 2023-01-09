import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

# Send an HTTP request to the website
response = requests.get(URL)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the book containers
book_containers = soup.find_all('article', class_='product_pod')

# Extract the data for each book
for book in book_containers:
    # Find the title of the book
    title = book.h3.a.attrs['title']

    # Find the price of the book
    price = book.find('p', class_='price_color').text

    # Print the data for each book
    print(title, price)


"""
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/flyfir248/webscraper.git
git push -u origin main

"""