import requests
import csv
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

# Send an HTTP request to the website
response = requests.get(URL)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the book containers
book_containers = soup.find_all('article', class_='product_pod')

# Open a CSV file for writing
with open('books.csv', 'w', newline='') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Title', 'Price', 'Link'])

    # Extract the data for each book
    for book in book_containers:
        # Find the title of the book
        title = book.h3.a.attrs['title']


        # Find the price of the book
        price = book.find('p', class_='price_color').text

        # Find the link to the book
        link = book.h3.a.attrs['href']

        # Write the data for the book to the CSV file
        writer.writerow([title, price, link])