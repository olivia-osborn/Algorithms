#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    least_batches = None
    # iterate over the recipe
    # for each corresponding ingredient, divide: recipe/ingredients (rounded down)
    # If least_batches = None, set first division to this variable
    # Elif: if the division is less than the least_batches amount, replace least_batches with that new amount
    # return least_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
