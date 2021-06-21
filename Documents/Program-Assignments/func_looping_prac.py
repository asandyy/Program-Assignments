'''
def triangle_area(base, height):
    area = (1/2) * (base * height)
    return area

print(triangle_area(3, 4))  #would return 6 and print to console
print(triangle_area(8, 11))     #would return 44 and print to console
'''
#create dictionary of foods
grocery_price = {"Chicken": 1.59, "Beef": 1.99, 
                "Cheese": 1.00, "Milk": 2.50}

def total_price(food_1, food_2):
    total_cost = grocery_price[food_1] + grocery_price[food_2]
    print("The total price of", food_1, "and", food_2 ,"is", total_cost)

total_price("Beef", "Cheese")


def price_difference(food_1, food_2):
    difference_cost = grocery_price[food_1] - grocery_price[food_2]
    print("The difference between", food_1, "and", food_2, "is", difference_cost)

price_difference("Beef", "Cheese")