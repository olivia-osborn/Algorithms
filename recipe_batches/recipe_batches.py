#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    least_batches = None
    # iterate over the recipe
    for i in recipe:
        if i not in ingredients:
            least_batches = 0
            return least_batches
        # for each corresponding ingredient, divide: recipe/ingredients (rounded down)
        for j in ingredients:
            if i == j:
                divided = int(ingredients.get(j) / recipe.get(i))
                # If least_batches = None, set first division to this variable
        if least_batches == None:
            least_batches = divided
        # Elif: if the division is less than the least_batches amount, replace least_batches with that new amount
        elif divided < least_batches:
            least_batches = divided
    # return least_batches
    return least_batches


print(recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}, {
      'milk': 1288, 'flour': 9, 'sugar': 95}))  # 0
print(recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10}, {
      'milk': 198, 'butter': 52, 'cheese': 10}))  # 1
print(recipe_batches({'milk': 2, 'sugar': 40, 'butter': 20}, {
      'milk': 5, 'sugar': 120, 'butter': 500}))  # 2
print(recipe_batches({'milk': 2}, {'milk': 200}))  # 100


# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
