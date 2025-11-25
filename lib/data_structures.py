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
    """
    Returns a list of names of each spicy food.
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
    
    Returns:
        List of strings with the names of each spicy food
    """
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    """
    Returns a list of foods where heat level is greater than 5.
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
    
    Returns:
        List of dictionaries with heat_level > 5
    """
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    """
    Prints each spicy food with its cuisine and heat level.
    Format: Name (Cuisine) | Heat Level: 🌶🌶🌶
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
    """
    for food in spicy_foods:
        heat_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Returns a single dictionary for the food matching the given cuisine.
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
        cuisine: String representing the cuisine to search for
    
    Returns:
        Dictionary for the spicy food matching the cuisine
    """
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    """
    Prints only the spicy foods with heat level greater than 5.
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
    """
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)


def get_average_heat_level(spicy_foods):
    """
    Returns the average heat level of all spicy foods.
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
    
    Returns:
        Integer representing the average heat level
    """
    total_heat = sum([food["heat_level"] for food in spicy_foods])
    return total_heat // len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    """
    Adds a new spicy food to the list and returns the updated list.
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
        spicy_food: Dictionary representing a new spicy food to add
    
    Returns:
        List with the new spicy food added
    """
    spicy_foods.append(spicy_food)
    return spicy_foods