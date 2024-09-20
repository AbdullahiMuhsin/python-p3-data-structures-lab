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
    This function takes in a list of spicy foods as an argument.

    It then uses a list comprehension to create a new list that
    contains only the names of the foods in the list.

    For example, if the list of spicy foods contains the following
    dictionaries:

        [
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

    The function will return the following list:

        ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

    """
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print("{} ({} | Heat Level: {})".format(
            food["name"], food["cuisine"], " " * food["heat_level"]))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in get_spiciest_foods(spicy_foods):
        print("{} ({} | Heat Level: {})".format(
            food["name"], food["cuisine"], " " * food["heat_level"]))

def get_average_heat_level(spicy_foods):
    """
    Calculate the average heat level of a list of spicy foods.

    This function takes a list of dictionaries as an argument, where each
    dictionary represents a spicy food and has a "heat_level" key with an
    integer value.

    The function then uses a generator expression to sum up all the heat levels
    of the spicy foods in the list.

    Finally, it divides the sum by the number of spicy foods in the list to get
    the average heat level.
    """
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    return total_heat / num_foods

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Iterate over the list of spicy foods.
    for food in spicy_foods:
        # Checking if the cuisine of the current food matches the cuisine we're looking for.
        if food["cuisine"] == cuisine:
            # If it matches, return the entire food object.
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, new_spicy_food):
    """
    This function takes in a list of spicy foods and a new spicy food to be added
    to the list. It will append the new spicy food to the list and then return
    the list of spicy foods.

    :param spicy_foods: A list of spicy foods. Each spicy food is a dictionary
                        with keys "name", "cuisine", and "heat_level".
    :param new_spicy_food: A dictionary representing the new spicy food to be
                           added to the list. It should have keys "name",
                           "cuisine", and "heat_level".
    :return: The list of spicy foods with the new spicy food added.
    """
    spicy_foods.append(new_spicy_food)
    return spicy_foods
