product_categories = ["laptop", {"audio":['headphone', 'earphone']}, {"accessory":['keyboard', 'laptop-stand', 'bag']}]  

data = [
    
  {
    "imglink": "./jbl_files/61HrC2qBTwL._AC_UY218_.jpg",
    "pdtname": "JBL Live 660NC / Audio Headphone: Wireless Over-Ear Noise Cancelling Headphones, Long Lasting Battery - 8 hours, Voice Assistant - Black, Medium",
    "price": "99."
  },
  {
    "imglink": "./jbl_files/518X-lGLUsL._AC_UY218_.jpg",
    "pdtname": "JBL Endurance Peak 3 / Audio Headphone: Wireless Headphones, Noise Cancellation, Purebass sound, Black, Small",
    "price": "79."
  },
  {
    "imglink": "./jbl_files/61cC3eF3uEL._AC_UY218_.jpg",
    "pdtname": "JBL Tune 510BT / Audio Headphone: Wireless On-Ear Headphones,  Noise Cancelling, Portable Mini Bluetooth Speaker, IP67 Waterproof and dustproof, 10 Hours of Playtime, Purebass Sound, Black",
    "price": "149"
  }
  
]



for dict in data:
    #new_category = "" 
    #new_subcategory = ""
    for item in product_categories:
        #print (item)
        #print (type(item))
        #print("Item is ", item)
        #category = "" 
        #sub_category = ""
        if type(item) == str:
            print("string")
            category = item
            new_subcategory = ""
            if category.lower() in dict['pdtname'].lower():
                new_category = category 
          
        elif type(item) == dict:
            print("dictionary")
            category_item =   list(item.keys())[0] 
            #print("category_item", category_item) 
            category = str(category_item) 
            if category.lower() in dict['pdtname'].lower():
                new_category = category 
            sub_category_item = list(item.values())
            for sub_item in sub_category_item:
                if sub_category_item[sub_item].lower() in dict['pdtname'].lower():
                    new_subcategory = sub_item

    #print("Category is", new_category)
    #print(new_subcategory)   


# Categories and sub-categories
    new_category = "" 
    new_subcategory = ""
    for item in product_categories:
        category = "" 
        sub_category = ""
        if type(item) == str:
            category = item
            new_subcategory = ""
            if category.lower() in data_dict['pdtname'].lower():
                new_category = category 
            
        elif type(item) == dict:
            #print("Dictionary")
            category_item =   list(item.keys())
            #print("Category item", category_item) 
            category = ''.join(category_item)
            #print(category)
            if category.lower() in data_dict['pdtname'].lower():
                new_category = category 
            sub_category_item = list(item.values())
            #print(sub_category_item)
            for sub_item in sub_category_item:
                #print(sub_item)
                for sub_subitem in sub_item:
                    #print(sub_subitem)
                    if sub_subitem.lower() in data_dict['pdtname'].lower():
                        #print("found")
                        new_subcategory = sub_subitem    



      






   





