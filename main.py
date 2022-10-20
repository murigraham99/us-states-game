from turtle import Turtle, Screen
import pandas
screen = Screen()
image = "blank_states_img.gif"
screen.bgpic(image)
STATES = []
score = 0
screen.title("US States Quiz")
data = pandas.read_csv("50_states.csv")
STATES = data["state"].values.tolist()

print(STATES)
guessed_states = []
missed_states =[]

while len(guessed_states) < len(STATES):

    answear_raw = screen.textinput(f" {score}/50 US States found", "Guess a state:")
    answear = answear_raw.title()

    if answear == "Stop":
        for element in STATES:
            missed_states = [state for state in guessed_states if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missed.csv")
        break

    for state in STATES:

        if answear == state:
            score += 1
            state_data = data[data.state == answear]
            t = Turtle()
            t.penup()
            t.ht()
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answear)
            guessed_states.append(answear)
        else:
            pass


