from cs50 import SQL

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///store.db")
 
supplier_product_categories = db.execute("SELECT * FROM product_categories")
supplier_product_subcategories = db.execute("SELECT * FROM product_subcategories")
print(supplier_product_categories)
print(supplier_product_subcategories)