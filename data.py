from cs50 import SQL

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///store.db")
 
products = db.execute("SELECT pdt_name, brand, category, subcategory FROM products_list")  

products_list = []
for item in products:
    name = item['pdt_name']
    brand = item['brand']
    category = item['category']  
    subcategory = item['subcategory']
    products_dict = {"name":name, "brand": brand, "category":category, "subcategory": subcategory}
    products_list.append(products_dict)

keys = list(products_list[0].keys())

#print(keys)



products_items = db.execute("SELECT * FROM products_list")  
id = db.execute("SELECT last_insert_rowid() AS ID")
print(id)

items = []
for product in products_items:
    number = product['id']
    item = product['pdt_name']
    specs = product['specs']
    price = product['price']
    items_dict = {"number":number, "item":item, "specs":specs, "price":price}
    items.append(items_dict)
#print(items)   

supplier_categories = ["Audio", "Laptops"]

supplier_pdtcategories = db.execute("SELECT id, pdt_category FROM product_categories")
#print(supplier_pdtcategories)

for supplier_category in supplier_categories:
    for dict_item in supplier_pdtcategories:
        if supplier_category in dict_item.values():
            category = supplier_category
            #print(category)

suppliers = {"ABC": ["Phones", "Laptops"]} 

for item in suppliers:
    print(item)

#for supplier, category in suppliers.items():
    #print(supplier)
    #print(category)

new_categories = db.execute("SELECT * FROM product_categories")
#print(new_categories) 

new_dataset = [{'id': 1, 'supplier_name': 'ABC Electronics', 'pdt_categories': ['Audio', 'Laptops']}, {'id': 2, 'supplier_name': 'Digital Products Limited', 'pdt_categories': ['Accessories', 'Accessories', 'Accessories', 'Laptops']}]

for dict_item in new_dataset:
    for key in dict_item:
        print(item)
        #print(categories)

supplier_product_category = db.execute("SELECT DISTINCT pdt_category FROM product_categories")   
print(supplier_product_category)     



 


 
    


        











    