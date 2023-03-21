from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=100, pady=20)


def convert():
    new_num = 1.609 * float(input.get())
    my_label_1.config(text=new_num)


my_label = Label(text='Miles', font=("Arial", 15, "bold"))
my_label.grid(column=2, row=0)

my_label_1 = Label(text="0", font=("Arial", 15, "bold"))
my_label_1.grid(column=1, row=1)

my_label_2 = Label(text='is equal to', font=("Arial", 15, "bold"))
my_label_2.grid(column=0, row=1)

my_label_3 = Label(text='Km', font=("Arial", 15, "bold"))
my_label_3.grid(column=2, row=1)

input = Entry(width=7)
input.grid(column=1, row=0)

button = Button(text="Calculate", command=convert)
button.grid(column=1,row=2)








window.mainloop()