from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.level_player1 = 1
        self.level_player2 = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Player 1: Level {self.level_player1} | Player 2: Level {self.level_player2}", align="left",
                   font=FONT)

    def increase_level(self, player):
        if player == 1:
            self.level_player1 += 1
        elif player == 2:
            self.level_player2 += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
