import json
from bs4 import BeautifulSoup

# Read the HTML file
with open('bags.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with the specified class
product_divs = soup.find_all('div', class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')

# Initialize an empty list to store the product information
products = []

# Loop through each product div
for product_div in product_divs:
    # Find img element with class "s-image" and get the imglink
    img_element = product_div.find('img', class_='s-image')
    imglink = img_element['src'] if img_element else ''

    # Find span element with class "a-size-medium a-color-base a-text-normal" and get the pdtname
    span_element = product_div.find('span', class_='a-size-medium a-color-base a-text-normal')
    pdtname = span_element.text.strip() if span_element else ''

    # Find span element with class "a-price-whole" and get the price
    span_price = product_div.find('span', class_='a-price-whole')
    price = span_price.text.strip() if span_price else ''

    # Append product information to the list
    products.append({
        'imglink': imglink,
        'pdtname': pdtname,
        'price': price
    })

# Write the product information to data.json
with open('bags.json', 'w', encoding='utf-8') as json_file:
    json.dump(products, json_file, ensure_ascii=False, indent=2)

print('Data written to data.json file')
