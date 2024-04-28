from tkinter import *
from tkinter import messagebox

def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} is Obesity') 
    else:
        messagebox.showerror('BMI Calculator', 'Something went wrong!')   

ws = Tk()
ws.title('BMI Calculator')
ws.geometry('400x300')
ws.config(bg="light grey")

var = IntVar()

frame = Frame(
    ws,
    padx=10, 
    pady=10,
    bg="light grey"
)
frame.pack(expand=True)


age_lb = Label(
    frame,
    text="Enter Age",
    font=("Helvetica", 12),
    bg="light grey"
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame,
    font=("Helvetica", 12)
)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Select Gender',
    font=("Helvetica", 12),
    bg="light grey"
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame,
    bg="light grey"
)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text='Male',
    variable=var,
    value=1,
    font=("Helvetica", 12),
    bg="light grey"
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text='Female',
    variable=var,
    value=2,
    font=("Helvetica", 12),
    bg="light grey"
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="Enter Height (cm)",
    font=("Helvetica", 12),
    bg="light grey"
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Enter Weight (kg)",
    font=("Helvetica", 12),
    bg="light grey"
)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
    font=("Helvetica", 12)
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
    font=("Helvetica", 12)
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame,
    bg="light grey"
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi,
    font=("Helvetica", 12),
    bg="sky blue"
)
cal_btn.pack(side=LEFT, padx=5)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry,
    font=("Helvetica", 12),
    bg="light green"
)
reset_btn.pack(side=LEFT, padx=5)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda: ws.destroy(),
    font=("Helvetica", 12),
    bg="red",
    fg="white"
)
exit_btn.pack(side=RIGHT, padx=5)

ws.mainloop()
