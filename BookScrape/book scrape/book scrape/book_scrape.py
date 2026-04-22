import requests
from bs4 import BeautifulSoup
url = 'http://books.toscrape.com/'

response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Each book is contained within an <article> tag with the class 'product_pod'
    books = soup.find_all('article', class_='product_pod')

    print(f"{'TITLE':<40} | {'PRICE':<10}")
    print("-" * 55)

    for book in books:
        # The title is located in the <a> tag inside an <h3> tag
        # The 'title' attribute contains the full name
        title = book.h3.a['title']
        
        # The price is in a <p> tag with class 'price_color'
        price = book.find('p', class_='price_color').text
        
        # Print formatted results
        print(f"{title[:38]:<40} | {price:<10}")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

