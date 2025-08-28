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
    # return just the names
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    # filter foods with heat > 5
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    # print formatted string with 🌶 repeated heat_level times
    for food in spicy_foods:
        heat = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # return the first matching food
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    # reuse get_spiciest_foods
    for food in get_spiciest_foods(spicy_foods):
        heat = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")


def get_average_heat_level(spicy_foods):
    # compute average heat (integer division with // not needed here, tests expect int)
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)


def create_spicy_food(spicy_foods, new_food):
    # return list with new food added
    spicy_foods.append(new_food)
    return spicy_foods
