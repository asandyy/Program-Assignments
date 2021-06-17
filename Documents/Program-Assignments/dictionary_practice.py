#create dictionary of foods
grocery_price = {"Chicken": 1.59, "Beef": 1.99, 
                "Cheese": 1.00, "Milk": 2.50}

chicken_price = grocery_price["Chicken"]
beef_price = grocery_price["Beef"]
cheese_price = grocery_price["Cheese"]
milk_price = grocery_price["Milk"]

print(chicken_price)
print(beef_price)
print(chicken_price)
print(cheese_price)

#create dictionary of daily max temperatures
max_temperature = {"Monday": 72, "Tuesday": 75, 
                "Wednesday": 87, "Thursday": 79}

print(max_temperature["Monday"])
print(max_temperature["Tuesday"])
print(max_temperature["Wednesday"])
print(max_temperature["Thursday"])

#create dict of shoe with inventory counts
shoe_inventory = {"Jordan 13": 1, "Yeezy": 8,
                "Foamposite": 10, "AirMax": 5,
                "SB Dunk": 20}
shoe_inventory["SB Dunk"] -= 2
shoe_inventory["Yeezy"] += 1
