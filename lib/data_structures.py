spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names
    pass
    
def get_spiciest_foods(spicy_foods):
    return [heat for heat in spicy_foods if heat['heat_level'] > 5]
    pass

def print_spicy_foods(spicy_foods):
   for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]  # Creating heat level emojis
        
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
        

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food  

    return None
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = "🌶" * food["heat_level"]  # Creating heat level emojis
            
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
    pass

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  
    
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    average = total_heat_level / len(spicy_foods)
    return int(average) 
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(new_food)
    return spicy_foods
new_food = {
    "name": "Griot",
    "cuisine": "Haitian",
    "heat_level": 10,
}

updated_spicy_foods = create_spicy_food(spicy_foods, new_food)

pass
