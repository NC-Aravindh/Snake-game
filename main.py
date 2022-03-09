from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

score = Score()
snake = Snake()
food = Food()
screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)

screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")

no_of_segments = len(snake.segments)
game_on =True
while game_on:
    screen.update()
    time.sleep(0.1)


    snake.move_forward()
    if snake.head.distance(food) < 15:
        score.update_score()
        food.move()
        snake.extend()



    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.tail.xcor() < -290 or snake.tail.ycor() <- 290 :
        game_on = False
        score.game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(snake.tail) < 10:
            game_on = False
            score.game_over()

print("Game over")
screen.mainloop()
