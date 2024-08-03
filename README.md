# Shopping DataBase App Prototype

# Goal
This app is designed to solve my daily shopping problems. i.e. whether this price is "reasonable" enough for me to purchase. Is it a steal? Is it a OK price?

This app shall allow users to 
1. keep track of their shopping price (how much cheaper is this beef compared to the one I bought last week?)
2. to support goal 1, we will need a quick unit price calculator 
3. a keyword searching feature (once the db grow large) to help user quickly find the target
4. (optional) image-based searching 
5. (maybe) share price with others 
6. (maybe) accept commercial banner or pop up for price sensitive or price-value-ratio sensitive customers.

# DB design
1. Table1, product table
This table prototype a product that you see in real life grocery stores.
It shall include:
    1. id,
    2. upc, unique product code (similar to the bar code on the cover bag)
    3. product title
    4. (optional) category
    5. manufactor
    6. (optional) a simple description

2. Table2, purchase record
This table prototype a purchase behavior, where each row is one product bought.
It shall include:
    1. product id
    2. price
    3. weight
    4. unit
    5. price per unit
    6. date
    7. store (which store)
    8. location
    9. product_photo
    10. has_discount
    11. notes

# How to Run
'''bash
// front end
cd price-compare-frontend
npm start

// backend
cd price_compare_app
uvicorn app.main:app --reload

// nope
> python manage.py runserver
'''

# Possible Add ons
1. Food nutrition api from EDAMAM (https://developer.edamam.com/food-database-api-demo)
