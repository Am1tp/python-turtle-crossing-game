import random
import time
from turtle import Turtle
from random import Random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_distance = 5

    def generate_car(self):
        randint = random.randint(1,6)       # control number of cars on screen using random int
        if randint == 1:

            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(x = 300, y = random.choice(range(-250, 250)))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)

    def move_cars_faster(self):
        self.move_distance += MOVE_INCREMENT





