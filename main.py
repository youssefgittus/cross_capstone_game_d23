import time
from turtle import Screen
from player import Player, Player2
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
player2 = Player2()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player2.go_up, "w")
screen.onkey(player.go_down, "Down")
screen.onkey(player2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20 or car.distance(player2) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level(1)
    if player2.is_at_finish_line():
        player2.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level(2)

screen.exitonclick()
