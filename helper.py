import json

from cs50 import SQL

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///store.db")
 
# Opening JSON file with contains product data scrapped from Amazon
with open('data.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
#print(json_object)
print(len((json_object)))

#<img src="../static/Images/dellxps_files/" alt="">
#'Dell XPS 13 9310 Laptop - 13.4-inch OLED 3.5K (3456x2160) Touchscreen Display, Intel Core i7-11195G7, 16GB LPDDR4x, 512GB SSD, Intel Iris Xe Graphics, 1-Year Premium Support, Windows 11 Home - Silver'

#product_categories = ["laptop", {"audio":['headphone', 'earphone']}, {"accessory":['keyboard', 'laptop-stand', 'bag']}]  

db_products = db.execute("SELECT pdt_name FROM products_list")
#print(db_products)

db_productslist = [dict['pdt_name'] for dict in db_products]
print(db_productslist)

product = []

for data_dict in json_object: 
    pdt = data_dict['pdtname'].split("/")
    name = pdt[0] 
    pdt_name = data_dict['pdtname'].split(":") 
    rspecs = pdt_name[1]
    specs = rspecs.split(",")
    new_specs = []
    for item in specs:
        new_item = ""
        if item[0] == " ":
            new_item = item[1:]
        else:
            new_item = item
        new_specs.append(new_item)  
    new_specs_str = ', '.join(new_specs)      
    rbrand = name.split(" ") 
    brand = rbrand[0]

    category = data_dict["category"]
    subcategory = data_dict["sub_category"]
    # Image files
    img_link = data_dict['imglink'][1:]
    print(img_link)
    
    new_img = "../static/Images" + img_link
    print(new_img)

    # Product price
    currency = "usd"
    price = data_dict['price']
    new_price = ""
    for ch in price:
        if ch.isnumeric():
            new_price = new_price + ch
    new_price = int(new_price)  
    print(new_price)      

    pdt_dict = {"name": name, "specs": new_specs_str, "brand": brand, "category": category, "subcategory": subcategory,"img": new_img,"currency": currency, "price": new_price}
    #print(pdt_dict)
    product.append(pdt_dict)

    if pdt_dict["name"] not in db_productslist:
        #print("Not found")
        db.execute("INSERT INTO products_list (pdt_name, specs, brand, category, subcategory, currency, price, image) VALUES (?,?,?,?,?,?,?,?)", name, new_specs_str, brand, category, subcategory, currency, new_price, new_img)

db_currency = db.execute("SELECT symbol, name FROM currencies")
#print(db_currency)
db_currencydict = {}

for dict_item in db_currency:
    db_currencydict[dict_item["symbol"]] = dict_item["name"]
      
#print(db_currencydict)    

# Opening JSON file with contains currencies
with open('currency.json', 'r') as openfile:
 
    # Reading from json file
    currencies_object = json.load(openfile)
 
#print(currencies_object)
#print(len((currencies_object)))

for dict_item in currencies_object:
    symbol = dict_item["symbol"].split(" ")
    new_symbol = symbol[0]
    name = dict_item["name"]

    currency_dict = {"symbol": new_symbol, "name": name}
    #print(currency_dict)

    if new_symbol not in db_currencydict and name not in db_currencydict.values():
        print("Not found")
        db.execute("INSERT INTO currencies (symbol, name) VALUES (?,?)", new_symbol, name)




    

