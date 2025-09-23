def recipe():

    ingredients = [
        "1/4 Cup Sugar",
        "1 Tbs Baking Powder",
        "4 Cups Flour",
        "2 Cups Milk",
        "3 Large Eggs",
        "Chocolate (Desired amount)"
    ]

    procedure = {
        "Step 1": "Beat eggs, Warm milk and mix",
        "Step 2": "Add Baking powder and mix",
        "Step 3": "Add flour and whisk to make cake butter", 
        "Step 4": "Bake the cake at 200 degrees for 30 minutes" 
    }

    print("Chocolate Cake Ingredients.")
    print("-" * 40)
    for ingredient in ingredients:
        print(ingredient)
        +1
    
    print("\nProcess")
    print("-" * 40)
    print(procedure)

recipe()