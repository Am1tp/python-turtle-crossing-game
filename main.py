import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move,key="w")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()

    if player.ycor() == 280:    # go to next level if player reaches finish line, increase score, car speed
        player.next_level()
        scoreboard.update_level()
        car_manager.move_cars_faster()
        screen.update()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

            continue

screen.exitonclick()