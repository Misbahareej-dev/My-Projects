# ============================================================
#                 FOOD RECOMMENDATION SYSTEM
#                    Developed in Python
# ============================================================

# ---------------------- FOOD DATABASE ------------------------

foods = [

    # Healthy Food
    {
        "name": "Grilled Chicken",
        "category": "Healthy Food",
        "price": 550,
        "type": "Non-Vegetarian",
        "rating": 4.8,
        "diabetes": True,
        "bp": True
    },
    {
        "name": "Vegetable Salad",
        "category": "Healthy Food",
        "price": 350,
        "type": "Vegetarian",
        "rating": 4.7,
        "diabetes": True,
        "bp": True
    },
    {
        "name": "Oatmeal Bowl",
        "category": "Healthy Food",
        "price": 300,
        "type": "Vegetarian",
        "rating": 4.6,
        "diabetes": True,
        "bp": True
    },
    {
        "name": "Grilled Fish",
        "category": "Healthy Food",
        "price": 650,
        "type": "Non-Vegetarian",
        "rating": 4.9,
        "diabetes": True,
        "bp": True
    },

    # Desi Food
    {
        "name": "Daal Chawal",
        "category": "Desi Food",
        "price": 300,
        "type": "Vegetarian",
        "rating": 4.5,
        "diabetes": True,
        "bp": True
    },
    {
        "name": "Chicken Biryani",
        "category": "Desi Food",
        "price": 450,
        "type": "Non-Vegetarian",
        "rating": 4.9,
        "diabetes": False,
        "bp": False
    },
    {
        "name": "Chicken Karahi",
        "category": "Desi Food",
        "price": 650,
        "type": "Non-Vegetarian",
        "rating": 4.7,
        "diabetes": False,
        "bp": False
    },
    {
        "name": "Chana Masala",
        "category": "Desi Food",
        "price": 280,
        "type": "Vegetarian",
        "rating": 4.4,
        "diabetes": True,
        "bp": True
    },

    # Fast Food
    {
        "name": "Chicken Burger",
        "category": "Fast Food",
        "price": 500,
        "type": "Non-Vegetarian",
        "rating": 4.6,
        "diabetes": False,
        "bp": False
    },
    {
        "name": "French Fries",
        "category": "Fast Food",
        "price": 250,
        "type": "Vegetarian",
        "rating": 4.3,
        "diabetes": False,
        "bp": False
    },
    {
        "name": "Pizza",
        "category": "Fast Food",
        "price": 800,
        "type": "Vegetarian",
        "rating": 4.8,
        "diabetes": False,
        "bp": False
    },
    {
        "name": "Chicken Shawarma",
        "category": "Fast Food",
        "price": 400,
        "type": "Non-Vegetarian",
        "rating": 4.7,
        "diabetes": False,
        "bp": False
    },

    # Sweet Food
    {
        "name": "Fruit Bowl",
        "category": "Sweet Food",
        "price": 300,
        "type": "Vegetarian",
        "rating": 4.6,
        "diabetes": True,
        "bp": True
    },
    {
        "name": "Chocolate Cake",
        "category": "Sweet Food",
        "price": 450,
        "type": "Vegetarian",
        "rating": 4.7,
        "diabetes": False,
        "bp": False
    },
    {
        "name": "Gulab Jamun",
        "category": "Sweet Food",
        "price": 250,
        "type": "Vegetarian",
        "rating": 4.5,
        "diabetes": False,
        "bp": False
    },
    {
        "name": "Fruit Custard",
        "category": "Sweet Food",
        "price": 350,
        "type": "Vegetarian",
        "rating": 4.4,
        "diabetes": True,
        "bp": True
    }
]


# ---------------------- TITLE -------------------------------

def show_title():
    print("\n" + "=" * 65)
    print("             FOOD RECOMMENDATION SYSTEM")
    print("=" * 65)
    print("        Find food according to your preferences")
    print("=" * 65)


# ---------------------- INPUT FUNCTIONS ----------------------

def get_name():
    while True:
        name = input("\nEnter your name: ").strip()

        if name:
            return name

        print("Name cannot be empty.")


def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))

            if age > 0:
                return age

            print("Age must be greater than 0.")

        except ValueError:
            print("Please enter a valid age.")


def get_budget():
    while True:
        try:
            budget = float(input("\nEnter your budget in PKR: "))

            if budget > 0:
                return budget

            print("Budget must be greater than 0.")

        except ValueError:
            print("Please enter a valid amount.")


# ---------------------- HEALTH CONDITION ---------------------

def choose_health_condition():

    print("\n" + "-" * 65)
    print("                HEALTH CONDITION")
    print("-" * 65)

    print("1. No Special Condition")
    print("2. Diabetes")
    print("3. High Blood Pressure")

    while True:

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            return "None"

        if choice == "2":
            return "Diabetes"

        if choice == "3":
            return "High Blood Pressure"

        print("Invalid choice. Please select 1, 2 or 3.")


# ---------------------- FOOD CATEGORY ------------------------

def choose_category():

    print("\n" + "-" * 65)
    print("                  FOOD CATEGORY")
    print("-" * 65)

    print("1. Healthy Food")
    print("2. Desi Food")
    print("3. Fast Food")
    print("4. Sweet Food")

    categories = {
        "1": "Healthy Food",
        "2": "Desi Food",
        "3": "Fast Food",
        "4": "Sweet Food"
    }

    while True:

        choice = input("\nChoose an option (1-4): ").strip()

        if choice in categories:
            return categories[choice]

        print("Invalid choice. Please select 1-4.")


# ---------------------- FOOD TYPE ----------------------------

def choose_food_type():

    print("\n" + "-" * 65)
    print("                    FOOD TYPE")
    print("-" * 65)

    print("1. Vegetarian")
    print("2. Non-Vegetarian")
    print("3. Both")

    while True:

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            return "Vegetarian"

        elif choice == "2":
            return "Non-Vegetarian"

        elif choice == "3":
            return "Both"

        print("Invalid choice. Please select 1-3.")


# ---------------------- SHOW MENU ----------------------------

def show_category_menu(category):

    category_foods = []

    print("\n" + "=" * 65)
    print(f"                 {category.upper()} MENU")
    print("=" * 65)

    for food in foods:

        if food["category"] == category:

            category_foods.append(food)

            print(f"\n{len(category_foods)}. {food['name']}")
            print(f"   Price       : {food['price']} PKR")
            print(f"   Type        : {food['type']}")
            print(f"   Rating      : {food['rating']}/5")

    return category_foods


# ---------------------- SEARCH -------------------------------

def search_food():

    print("\n" + "=" * 65)
    print("                     SEARCH FOOD")
    print("=" * 65)

    keyword = input(
        "Enter food name or keyword: "
    ).strip().lower()

    results = []

    for food in foods:

        if keyword in food["name"].lower():

            results.append(food)

    if not results:

        print("\nNo food found.")

        return

    print("\nSearch Results:")

    for food in results:

        print("\n" + "-" * 40)
        print("Food     :", food["name"])
        print("Category :", food["category"])
        print("Price    :", food["price"], "PKR")
        print("Type     :", food["type"])
        print("Rating   :", food["rating"], "/5")


# ---------------------- SUITABILITY --------------------------

def is_suitable(food, condition):

    if condition == "Diabetes":
        return food["diabetes"]

    elif condition == "High Blood Pressure":
        return food["bp"]

    return True


# ---------------------- RECOMMENDATIONS -----------------------

def get_recommendations(
        category,
        food_type,
        condition,
        budget
):

    recommendations = []

    for food in foods:

        # Category filter
        if food["category"] != category:
            continue

        # Budget filter
        if food["price"] > budget:
            continue

        # Food type filter
        if food_type != "Both":

            if food["type"] != food_type:
                continue

        # Health preference filter
        if not is_suitable(food, condition):
            continue

        recommendations.append(food)

    # Sort by rating
    recommendations.sort(
        key=lambda item: item["rating"],
        reverse=True
    )

    return recommendations


# ---------------------- DISPLAY RECOMMENDATIONS ---------------

def display_recommendations(recommendations):

    print("\n" + "=" * 65)
    print("                MULTIPLE RECOMMENDATIONS")
    print("=" * 65)

    if not recommendations:

        print("\nSorry! No matching food was found.")
        print("Try increasing your budget or changing your preferences.")

        return

    for number, food in enumerate(recommendations, start=1):

        print(f"\n{number}. {food['name']}")
        print(f"   Price  : {food['price']} PKR")
        print(f"   Type   : {food['type']}")
        print(f"   Rating : {food['rating']}/5")

        print("   ✓ Matches your selected preferences")


# ---------------------- SELECT FOOD --------------------------

def select_food(category_foods):

    print("\n" + "=" * 65)
    print("                  SELECT YOUR FOOD")
    print("=" * 65)

    for number, food in enumerate(category_foods, start=1):

        print(
            f"{number}. {food['name']} "
            f"- {food['price']} PKR"
        )

    while True:

        try:

            choice = int(
                input(
                    "\nWhich food would you like to choose? "
                )
            )

            if 1 <= choice <= len(category_foods):

                return category_foods[choice - 1]

            print("Please select a valid food number.")

        except ValueError:

            print("Please enter a number.")


# ---------------------- FINAL SUMMARY ------------------------

def show_final_summary(
        name,
        age,
        condition,
        category,
        food_type,
        budget,
        selected_food,
        recommendations
):

    print("\n\n" + "=" * 65)
    print("                    FINAL SUMMARY")
    print("=" * 65)

    print("\nUser Information")
    print("-" * 40)

    print("Name             :", name)
    print("Age              :", age)
    print("Health Condition :", condition)
    print("Food Category    :", category)
    print("Food Type        :", food_type)
    print("Budget           :", budget, "PKR")

    print("\nYour Selected Food")
    print("-" * 40)

    if selected_food:

        print("Food   :", selected_food["name"])
        print("Price  :", selected_food["price"], "PKR")
        print("Rating :", selected_food["rating"], "/5")

    else:

        print("No food selected.")

    print("\nRecommended Options")
    print("-" * 40)

    if recommendations:

        for food in recommendations:

            print(
                f"- {food['name']} "
                f"({food['price']} PKR)"
            )

    else:

        print("No recommendations available.")

    # Best recommendation
    if recommendations:

        best = recommendations[0]

        print("\n" + "=" * 65)
        print("                 BEST RECOMMENDATION")
        print("=" * 65)

        print("\n🏆", best["name"])
        print("Price  :", best["price"], "PKR")
        print("Rating :", best["rating"], "/5")

        print(
            f"\nBased on your selected preferences, "
            f"I recommend {best['name']}."
        )

    print("\n" + "=" * 65)
    print("       Thank you for using our system!")
    print("=" * 65)


# ---------------------- MAIN PROGRAM -------------------------

def main():

    while True:

        show_title()

        # User details
        name = get_name()
        age = get_age()

        # Preferences
        condition = choose_health_condition()
        category = choose_category()

        # Show complete category data
        category_foods = show_category_menu(category)

        # Food type
        food_type = choose_food_type()

        # Budget
        budget = get_budget()

        # Recommendations
        recommendations = get_recommendations(
            category,
            food_type,
            condition,
            budget
        )

        # Show recommendations
        display_recommendations(recommendations)

        # User's own food choice
        selected_food = select_food(category_foods)

        # Search
        print("\n" + "-" * 65)
        print("Would you like to search for another food?")
        print("1. Yes")
        print("2. No")

        search_choice = input(
            "\nEnter your choice: "
        ).strip()

        if search_choice == "1":
            search_food()

        # Final summary
        show_final_summary(
            name,
            age,
            condition,
            category,
            food_type,
            budget,
            selected_food,
            recommendations
        )

        # Repeat
        print("\nWould you like to use the system again?")
        print("1. Yes")
        print("2. No")

        again = input("\nEnter your choice: ").strip()

        if again != "1":

            print("\nThank you! Goodbye 👋")
            break


# ---------------------- START PROGRAM ------------------------

if __name__ == "__main__":
    main()