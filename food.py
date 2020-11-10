import random

foodX = random.randint(1, 38)
foodY = random.randint(1, 38)
food_position = [foodX, foodY]

#Funcion para cambiar la direccion de la comida
def changeFoodPosition(snake_body):
    foodX, foodY = random.randint(1, 38), random.randint(1, 38)
    temp_food = [foodX, foodY]
    while(checkCoincidence(snake_body, temp_food)):
        foodX, foodY = random.randint(1, 38), random.randint(1, 38)
        temp_food = [foodX, foodY]
    return temp_food

#Esta funcion verifica que ninguna parte del cuerpo de la serpiente coincida con ella   
def checkCoincidence(snake_body, temp_food):
    for square in snake_body:
        if square == temp_food:
            return True
    return False