def get_recipe_price(prices, optionals=None, **ingredients):
    total_price = 0
    for ingredient, quantity in ingredients.items():
        if optionals and ingredient in optionals:
            continue
        price_per_100g = prices.get(ingredient, 0)
        ingredient_price = price_per_100g * (quantity / 100)
        total_price += ingredient_price
    return total_price


print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
print(get_recipe_price({}))
