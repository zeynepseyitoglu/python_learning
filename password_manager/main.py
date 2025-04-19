from tkinter import *

window = Tk()
window.title('Password manger')
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

website_label = Label(text='Website')

email_label = Label(text='Email')

password_label = Label(text='Password')


window.mainloop()