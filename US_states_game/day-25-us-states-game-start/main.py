import turtle
import pandas

sc = turtle.Screen()
sc.title('US States Game')

img = 'blank_states_img.gif'
sc.bgpic(img)

data = pandas.read_csv('50_states.csv')
states = data['state'].to_list()

""" def get_coordinates(x, y):
    print(x, y)

turtle.onscreenclick(get_coordinates) """
guessed_states = []


while len(guessed_states) < 50:
    answer_state = sc.textinput(title=f'{len(guessed_states)}/50 Guessed', prompt='What\'s another state name?')
    answer_state = answer_state.title()

    if answer_state == 'Exit':
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('missing_states.csv')
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #Get the relevant row
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())



turtle.mainloop()












#sc.exitonclick()