import json
import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session


# Configure application
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///store.db")

@app.route("/")
def index():
    return render_template("index.html", current_route="/")

@app.route("/signed_in")   
def signedin():
    return render_template("signed.html", current_route="signed_in") 


@app.route("/log_in")
def log_in():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/inventory")
def inventory():
    return render_template("inventory.html")


@app.route("/admin_login")    
def admin_login():
    return render_template("inventorylogin.html")


@app.route("/admin_registration")    
def admin_registration():
    return render_template("inventoryreg.html")

######## Product listing page    ########
# Route to display products that are in the data base
@app.route("/products")  
def products():
    products = db.execute("SELECT id, pdt_name, brand, category, subcategory FROM products_list")  
    products_total = db.execute("SELECT COUNT(*) AS [products_total] FROM products_list")

    products_list = []
    for item in products:
        id = item['id']
        name = item['pdt_name']
        brand = item['brand']
        category = item['category']  
        subcategory = item['subcategory']
        products_dict = {"id":id, "name":name, "brand": brand, "category":category, "subcategory": subcategory}
        products_list.append(products_dict)

        keys = list(products_list[0].keys())
        new_keys = []
        
        for key in keys:
           new_key = key.capitalize()
           #print(new_key)
           new_keys.append(new_key)
       
        product_names = True

    return render_template("inventory.html", product_names=product_names, new_keys=new_keys, products_list=products_list, products_total=products_total) 

# Route to add products to the products database
@app.route("/add_product", methods=['GET','POST'])  
def add_product():
    # Retrieve categories from database for select menu in form
    categories = db.execute("SELECT * FROM product_categories")
    
    category_dict = {} 
    for dict_item in categories:   
        category = dict_item['pdt_category']
        if category in category_dict:
            category_dict[category].append(dict_item['pdt_subcategory'])
        else:
            #category_dict[category] =  []
            #category_dict[category].append(dict_item['pdt_subcategory'])
            category_dict[category] = [dict_item['pdt_subcategory']]

    json_category_dict = json.dumps(category_dict)     

    currencies = db.execute("SELECT * FROM currencies")
    currencies_list = [dict['name'] for dict in currencies]   

    if request.method == "GET":
        add_pdt = True       
        return render_template("add-edit-product.html", add_pdt=add_pdt, category_dict=category_dict, json_category_dict=json_category_dict, currencies_list=currencies_list)
        
    else:
        name = request.form.get("pdt_name")   
        specs = request.form.get("specs") 
        brand = request.form.get("brand")
        category = request.form.get("category")
        scategory = request.form.get("scategory")
        currency = request.form.get("currency")
        price = request.form.get("px")
        #image = request.form.get()
        db.execute("INSERT into products_list(pdt_name, specs, brand, category, subcategory, currency, price) VALUES (?,?,?,?,?,?,?)", name, specs, brand, category, scategory, currency, price)
    return redirect("/products")    


#Route to edit products
@app.route("/edit_product", methods=["GET", "POST"])
def edit_product():
    id = request.form.get("id")
    

    # Retrieve categories from database for select menu in form
    categories = db.execute("SELECT * FROM product_categories")
    
    category_dict = {} 
    for dict_item in categories:   
        category = dict_item['pdt_category']
        if category in category_dict:
            category_dict[category].append(dict_item['pdt_subcategory'])
        else:
            #category_dict[category] =  []
            #category_dict[category].append(dict_item['pdt_subcategory'])
            category_dict[category] = [dict_item['pdt_subcategory']]
    print(category_dict)        

    json_category_dict = json.dumps(category_dict)     

    currencies = db.execute("SELECT * FROM currencies")
    currencies_list = [dict['name'] for dict in currencies]   
    
    if id:
        edit_pdt = True
        pdts_toedit = db.execute("SELECT * FROM products_list WHERE id = ?", id)
        id = pdts_toedit[0]["id"]
        name = pdts_toedit[0]["pdt_name"]
        specs = pdts_toedit[0]["specs"]
        brand = pdts_toedit[0]["brand"]
        category = pdts_toedit[0]["category"]
        subcategory = pdts_toedit[0]["subcategory"]
        currency= pdts_toedit[0]["currency"]
        price= pdts_toedit[0]["price"]
    return render_template("add-edit-product.html", edit_pdt=edit_pdt, category_dict=category_dict,  json_category_dict=json_category_dict, currencies_list=currencies_list, id=id, name=name, specs=specs, brand=brand, category=category, subcategory=subcategory, currency=currency, price=price)  

# Route to update products
@app.route("/update_product", methods=["POST"])
def update_product():
    #print("This is the update products route")
    id = request.form.get("id")
    #print(id)

    if id:
        name = request.form.get("pdt_name")
        specs = request.form.get("specs")
        brand = request.form.get("brand")
        category = request.form.get("category")
        subcategory = request.form.get("subcategory")
        currency = request.form.get("currency")
        price = request.form.get("price")
        db.execute("UPDATE products_list SET pdt_name = ?, specs = ?, brand = ?, category = ?, subcategory = ?, currency = ?, price = ? WHERE id = ?", name, specs, brand, category, subcategory, currency, price, id )
    return redirect("/products")    

     
#Route to delete products
@app.route("/delete_pdt", methods=["POST"])
def delete_pdt():
    id = request.form.get("id")
    print(id)

    if id:
        db.execute("DELETE FROM products_list WHERE id = ?", id)
        print("deleted")
    return redirect("/products")    

    

# Route to add product categories
@app.route("/add_product_category", methods=["GET", "POST"])
def add_product_category():
    if request.method == "POST":
        category = request.form.get("category")  
        subcategory = request.form.get("subcategory")  
        # Add categories to pdt_categories table
        db.execute("INSERT INTO product_categories(pdt_category) VALUES (?)", category)
        pdt_category_id = db.execute("SELECT last_insert_rowid() AS category_id")
        pdtcategory_id = pdt_category_id[0]["category_id"]
        print("Product category id is", pdtcategory_id)
        # Add subcategories to pdt_subcategories table
        db.execute("INSERT INTO product_subcategories(pdt_subcategory) VALUES (?)", subcategory)
        pdt_subcategory_id = db.execute("SELECT last_insert_rowid() AS subcategory_id")
        pdtsubcategory_id = pdt_subcategory_id[0]["subcategory_id"]
        print("Product subcategory id is", pdtsubcategory_id)

        # Add category_id and subcategory_id to product_categories_subcategories
        db.execute("INSERT INTO product_categories_subcategories(pdt_category_id, pdt_subcategory_id) VALUES (?,?)", pdtcategory_id, pdtsubcategory_id)


    categories = db.execute("SELECT * FROM product_categories")
    print(categories)
    total_categories = db.execute("SELECT COUNT(pdt_category) AS [category_total] FROM product_categories")
    total_subcategories = db.execute("SELECT COUNT(pdt_subcategory) AS [subcategory_total] FROM product_subcategories")

    product_categories = True
   
    return render_template("inventory.html", categories=categories, product_categories=product_categories, total_categories=total_categories, total_subcategories=total_subcategories)

# Route to direct user to edit the product categories
@app.route("/edit_pdt_category", methods=["GET","POST"]) 
def edit_pdt_category():
    id = request.form.get("id")
    edit_pdtcategory = True

    if id:
        # Retrieve values for pdt categories for editing
        categories = db.execute("SELECT * FROM product_categories WHERE id = ?", id)
        category_id = categories[0]["id"]
        category = categories[0]["pdt_category"]
        subcategory = categories[0]["pdt_subcategory"]
    return render_template("inventory.html", edit_pdtcategory= edit_pdtcategory, category_id=category_id, category=category, subcategory=subcategory)


# Route to update product categories in the database
@app.route("/update_pdt_category", methods=["POST"])
def update_pdt_category():
    id = request.form.get("id")

    if id:
        #Update category in database
        category = request.form.get("category")
        subcategory = request.form.get("subcategory")
        db.execute("UPDATE product_categories SET pdt_category = ?, pdt_subcategory = ? WHERE id = ?", category, subcategory, id)
    return redirect("/add_product_category")  


# Route to delete the product categories
@app.route("/delete_pdt_category", methods=["POST"]) 
def delete_pdt_category():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM product_categories WHERE id = ?", id)
    return redirect("/add_product_category")    
        
    

@app.route("/purchases")    
def purchases():
    purchases = True
    return render_template("inventory.html", purchases=purchases)

@app.route("/purchase_order") 
def purchase_order():
    purchase_order = True
    products_items = db.execute("SELECT * FROM products_list")  

    items = []
    for product in products_items:
        number = product['id']
        item = product['pdt_name']
        specs = product['specs']
        price = product['price']
        items_dict = {"number":number, "item":item, "specs":specs, "price":price}
        items.append(items_dict)
    print(items)    

 
    json_productslist = json.dumps(items)      

    currencies = db.execute("SELECT * FROM currencies")
    currencies_list = [dict['name'] for dict in currencies]     

    return render_template("inventory.html", items = items, purchase_order=purchase_order, currencies_list=currencies_list, json_productslist=json_productslist)   

@app.route("/purchaseorder_info", methods=['POST'])
def purchaseorder_info():
    data = request.get_json()  
    #print(data)

    product_name = data["selected"]
    session['product_name'] = product_name
    return (product_name)

    
@app.route('/get_info', methods=['GET'])
def get_info():
    info = db.execute("SELECT specs, price FROM products_list WHERE pdt_name = ?", session['product_name'])  

    info_list = []
    for item in info:
        specs = item['specs']
        price = item['price']
        info_dict = {"specs": specs, "price": price}
        info_list.append(info_dict)
          
    return jsonify(info_list)


# Route to suppliers list form
@app.route("/suppliers")
def suppliers():
    supplier_list = True

    # Retrieve suppliers and supplier categories from database
    suppliername_categories = db.execute("SELECT suppliers_list.id,supplier_name, GROUP_CONCAT(pdt_category) AS pdt_categories FROM suppliers_list JOIN supplier_product_categories ON suppliers_list.id = supplier_product_categories.supplier_id JOIN product_categories ON supplier_product_categories.category_id = product_categories.id GROUP BY supplier_name")
    print(suppliername_categories)

    for item in suppliername_categories:
        categories = item["pdt_categories"]
        print(categories)
        print(type(categories))
        categories_list = categories.split(",")
        print(categories_list)
        item["pdt_categories"] = categories_list
    print(suppliername_categories)

    #supplier_category_dict = {}
    #for dict_item in suppliername_categories:
        #supplier_name = dict_item["supplier_name"]
        #categories_supplied = dict_item["pdt_categories"]
        #categories_supplied_list = categories_supplied.split(",")
        #supplier_category_dict[supplier_name]= categories_supplied_list
    #print(supplier_category_dict)    

    return render_template("inventory.html", supplier_list=supplier_list, suppliername_categories=suppliername_categories)


# Route to add supplier to suppliers data base
@app.route("/add_supplier", methods=["GET", "POST"])   
def add_supplier():
    if request.method == "GET":
        add_supplier_form = True
        # To receive product categories from the product_categories table to select pdt categories on the form
        supplier_product_category = db.execute("SELECT DISTINCT pdt_category FROM product_categories")
        print(supplier_product_category)

        return render_template("inventory.html", add_supplier_form=add_supplier_form, supplier_product_category=supplier_product_category)

    else:
    
        supplier = request.form.get("supplier_name")    
        supplier_email = request.form.get("supplier_email") 
        supplier_tel = request.form.get("supplier_tel")  
        supplier_pdt = request.form.getlist("supplier_pdt")   
        print(supplier + supplier_email + supplier_tel)
        print(supplier_pdt)
        
        db.execute("INSERT INTO suppliers_list(supplier_name, supplier_email, supplier_tel) VALUES (?,?,?)", supplier, supplier_email, supplier_tel)
        supplier_id = db.execute("SELECT last_insert_rowid() AS id")
        supplierid_value = supplier_id[0]["id"]
        print("Supplier id is", supplierid_value)

        supplier_pdtcategories = db.execute("SELECT id, pdt_category FROM product_categories")

        for supplier_category in supplier_pdt:
            for dict_item in supplier_pdtcategories:
                if supplier_category in dict_item.values():
                    category = supplier_category
                    print(category)
                    product_category_id = db.execute("SELECT id FROM product_categories WHERE pdt_category = ?", category)
                    pdt_categoryid_value = product_category_id[0]["id"]
                    print("Product id", pdt_categoryid_value)
                    db.execute("INSERT INTO supplier_product_categories(supplier_id, category_id) VALUES (?,?)",  supplierid_value, pdt_categoryid_value)

             
        return redirect("/add_supplier")


# Route to display the edit suppliers form
@app.route("/edit_supplier", methods=["POST"])
def edit_supplier():
    update_supplier = True
    edit_supplier_id = request.form.get("id")

    supplier_info = db.execute("SELECT * FROM suppliers_list WHERE id = ?", edit_supplier_id)
    print(supplier_info)
    # To receive product categories from the product_categories table to select pdt categories on the form
    supplier_pdt_category = db.execute("SELECT DISTINCT pdt_category FROM product_categories")
    print(supplier_pdt_category)
    return render_template("inventory.html", update_supplier=update_supplier, supplier_info=supplier_info, supplier_pdt_category=supplier_pdt_category)

# Route to update the suppliers detials   
#@app.route("/update_supplier", methods=["POST"]) 
#def update_supplier():










