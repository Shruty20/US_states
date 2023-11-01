import turtle
import pandas

screen = turtle.Screen()
screen.title("US STATE GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")  #read the data from file
all_states = data["state"].to_list()   #convert the data to the list
guessed_states = []                    #empty list for guessing state whatever user enters


while len(guessed_states) < 50:   #states are 50 in total
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's the state's name?").title()  #title to capitalize first letter automatically
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]           # to print details of missed states
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_missed")                         #convert file to csv format
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()  #create a new turtle
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


