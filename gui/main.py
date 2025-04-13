import tkinter

window = tkinter.Tk()
window.title('first gui')
window.minsize(width=500, height=300)

#Create a label 
my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.pack()

def button_clicked():
    entry_input = input.get()
    my_label.config(text=entry_input)
    print('I got clicked')

#add a button 
button = tkinter.Button(text='Click me', command=button_clicked)
button.pack()

#entry 
input = tkinter.Entry()
input.pack()
entry_input = input.get()













window.mainloop()