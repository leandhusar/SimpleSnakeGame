import random

#First it selects a random position for the food
foodX = random.randint(1, 38)
foodY = random.randint(1, 38)
food_position = [foodX, foodY]

#Function that changes the food position without getting over any part of the snake
def changeFoodPosition(snake_body):
    foodX, foodY = random.randint(1, 38), random.randint(1, 38)
    temp_food = [foodX, foodY]
    while(checkCoincidence(snake_body, temp_food)):
        foodX, foodY = random.randint(1, 38), random.randint(1, 38)
        temp_food = [foodX, foodY]
    return temp_food
 
def checkCoincidence(snake_body, temp_food):
    for square in snake_body:
        if square == temp_food:
            return True
    return False