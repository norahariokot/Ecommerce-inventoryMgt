import json
from bs4 import BeautifulSoup

# Read the HTML file
with open('currency.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all 'a' elements with the specified class
a_elements = soup.find_all('a', class_='_1k5if')

# Initialize an empty list to store currency information
currencies = []

# Loop through each 'a' element
for a_element in a_elements:
    # Find 'b' element with class "_1oSQL" and get the symbol
    b_element = a_element.find('b', class_='_1oSQL')
    symbol = b_element.text.strip() if b_element else ''

    # Find 'p' element and get the name
    p_element = a_element.find('p')
    name = p_element.text.strip() if p_element else ''

    # Append currency information to the list
    currencies.append({
        'symbol': symbol,
        'name': name
    })

# Write the currency information to currency.json
with open('currency.json', 'w', encoding='utf-8') as json_file:
    json.dump(currencies, json_file, ensure_ascii=False, indent=2)

print('Currency data written to currency.json')
