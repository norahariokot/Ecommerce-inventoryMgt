from cs50 import SQL

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///store.db")
 
my_dict = {'Laptops': 'None', 'Accessories': 'Laptop stands'}

for key, value in my_dict.items():
    category = key
    subcategory = value
    #print(f"{category}:{subcategory}")
    category_id = db.execute("SELECT id FROM product_categories WHERE pdt_category == ?", category)
    categoryid_value = category_id[0]["id"]
    if subcategory != "None":
            subcategory_id = db.execute("SELECT id FROM product_subcategories WHERE pdt_subcategory == ?", subcategory)
            subcategoryid_value = subcategory_id[0]["id"]
    else:
        subcategoryid_value = ""        

    print(categoryid_value)
    print(subcategoryid_value)