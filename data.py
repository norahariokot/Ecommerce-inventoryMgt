from cs50 import SQL

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///store.db")
 
my_list = [{'supplier_id': 1, 'supplier_name': 'ABC Electronics', 'category_id': 1, 'pdt_category': 'Laptops', 'subcategory_id': None, 'pdt_subcategory': None}, {'supplier_id': 1, 'supplier_name': 'ABC Electronics', 'category_id': 3, 'pdt_category': 'Accessories', 'subcategory_id': 2, 'pdt_subcategory': 'Keyboards'}, {'supplier_id': 1, 'supplier_name': 'ABC Electronics', 'category_id': 3, 'pdt_category': 'Accessories', 'subcategory_id': 3, 'pdt_subcategory': 'Laptop stands'}, {'supplier_id': 2, 'supplier_name': 'Digital Products Limited', 'category_id': 2, 'pdt_category': 'Audio', 'subcategory_id': 1, 'pdt_subcategory': 'Headphones'}, {'supplier_id': 2, 'supplier_name': 'Digital Products Limited', 'category_id': 3, 'pdt_category': 'Accessories', 'subcategory_id': 4, 'pdt_subcategory': 'Laptop bags'}]

my_dict = {}
for supplier in my_list:
    if supplier["supplier_name"] in my_dict:
        my_dict[supplier["supplier_name"]].append({"pdt_category": supplier["pdt_category"], "pdt_subcategory": supplier["pdt_subcategory"]})
    else:
        my_dict[supplier["supplier_name"]] = [{"supplier_id": supplier["supplier_id"], "pdt_category": supplier["pdt_category"], "pdt_subcategory": supplier["pdt_subcategory"]}]
       
for supplier, supplier_info in my_dict.items():
    for info in supplier_info:
        print(info)
        if "supplier_id" in info:
            print(info["supplier_id"])
    

   





