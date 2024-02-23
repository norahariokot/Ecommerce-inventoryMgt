# E-COMMERCE AND INVENTORY MANAGEMENT APP
## Video Demo:  <https://youtu.be/CKMRqK0HDUg>

### Project Description:
The project is both an ecommerce app and an inventory management system. The home page is the home page for the online store where users can buy products and on the backend, admin authorised users (ideally) the owner of the shop can manage the store's inventory. The inventory management system enables the owner to create purchase orders and verify inventory based on the purchase orders.

The motivation behind buiding this app was to challenge myself to automate inventory management which is a crucial and mandate task, with this app. Inventory mangement will be automated and quicker also elminating human error and ensure efficiency in store management.

Coding the project was fun however, the major challenge I faced was time element, building this app took longer than I thought but it was very rewarding because I learnt alot. 

### Technologies used:
- HTML
- CSS
- JavaScript
- Flask
- Python
- Sqlite

### Project File structure
.
├── README.md
    
    ├── __pycache__
    ├── amazon.txt
    ├── app.py
    ├── data.json
    ├── data.py
    ├── flask_session
    ├── helper.py
    ├── scrapper.py
    ├── static
    ├── store.db
    └── templates

### How the app works
The app is coded using both front end technologies: HTML, JS and CSS. These were used to create the user interface for all the web pages in the app. 
The index.html file is is the home page of the app. Users visit the page to view products they can shop. To buy items or add them to their charts users will be required to sign or create new accounts.

On the backend the app is supported by an inventory management system that can only be accessed by authorised users. They can sign in to access the inventory management dashboard.
The inventory management dashboard enables the administrator to create purchase orders and verify them as well as update in the inventory database. Thereby offering efficiency and accuracy in the store's management.

All the data used both user data and product data is stored in a database. The information stored includes user login information, chart information and purchase information. On the backend it stores the inventory database and well as the sales of the products.

The project also used various routes to enable users access the various resources in the app, like sign in pages and desired resources.

The app also contains other helper files, to obtain product information for this project. I created a webscrapper to scrap data from an already existing ecommerce site to scrap product information like product name, specs, images and prices. I opted for web scraping over APIs because most APIs were not free and also had limitations on the information that could be accessed pertaining to the targeted sites.


### Usage
Run flask run 