import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Nigeria_States.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.penup()
pen.color("green")
pen.hideturtle()

data = pandas.read_csv("nigerian_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 37:
    answer_state = screen.textinput(title=f"Guess The State {len(guessed_states)}/37",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missed_states = {"States To Learn": [state for state in all_states if state not in guessed_states]}
        data_frame = pandas.DataFrame(missed_states)
        print(data_frame)
        data_frame.to_csv("states_to_learn.csv")
        pen.goto(167, -213)
        pen.write(f"You Guessed: {len(guessed_states)}/37",
                                   align="center", font=("Bodoni MT", 15, "normal"))
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state = data[data.state == answer_state]
        new_pen = turtle.Turtle()
        new_pen.penup()
        new_pen.color("green")
        new_pen.shape("circle")
        new_pen.shapesize(stretch_wid=0.2, stretch_len=0.2)
        new_pen.goto(int(state.x), int(state.y))
        new_pen.write(answer_state)
    if len(guessed_states) == 37:
        pen.goto(167, -213)
        pen.write("Cheers You Guessed\nall 37 States Correctly", align="center", font=("Bodoni MT", 15, "normal"))

screen.mainloop()



