
import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

response = requests.get(url)
response.encoding = response.apparent_encoding  # Automatically detect encoding

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all book containers
    books = soup.find_all('article', class_='product_pod')
    
    # Loop through each book and extract information
    for book in books:
        # Extract the title
        title = book.h3.a['title']
        
        # Extract the price
        price = book.find('p', class_='price_color').text
        #price = price.replace('£', '')
        
        # Extract availability
        availability = book.find('p', class_='instock availability').text.strip()
        
        # Extract the link to the book's detail page
        book_url = book.h3.a['href']
        book_url = url + book_url   # Construct the full URL
        
        # Send a request to the book's detail page
        book_response = requests.get(book_url)
        if book_response.status_code == 200:
            book_soup = BeautifulSoup(book_response.text, 'html.parser')
            
            # Extract the genre from the breadcrumb navigation
            genre = book_soup.find('ul', class_='breadcrumb').find_all('a')[2].text
            if genre == 'Default':
                genre = 'N/A'
        
        # Print the information
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Availability: {availability}")
        print(f"Genre: {genre}")
        print("-" * 40)
