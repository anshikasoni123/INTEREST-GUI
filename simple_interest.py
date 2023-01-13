from tkinter import *

window = Tk()
window.title("SIMPLE INTEREST CALCULATOR")
window.geometry("500x500")
window.configure(bg="seagreen")

def calculate_interest():
    p = int(principle_entry.get())
    r = int(rate_entry.get())
    t = int(time_entry.get())
    i = (p*r*t)/100
    interest = round(i,2)
    result_label.destroy()
    output_msg = Label(result_frame,text = "Interest on Rs." + str(p) + " at rate of interest " + str(r) + "% for " + str(t) + " years is Rs." + str(interest),bg = "gray",font=("Calibri",12),width=55)
    output_msg.place(x=20,y=40)
    output_msg.pack()

heading = Label(window,text="SIMPLE INTEREST CALCULATOR",font=("Calibri",20),fg="white",bg="seagreen")
heading.place(x=50,y=20)

principle_label = Label(window,text="Write your principle money",font=("Calibri",12),fg = "white",bg = "seagreen",bd=2)
principle_label.place(x=20,y=90)

principle_entry = Entry(window,text="",bd=2,width=20)
principle_entry.place(x=225,y=92)

rate_label = Label(window,text="Write your rate of interest",font=("Calibri",12),fg = "white",bg = "seagreen",bd=2)
rate_label.place(x=20,y=130)

rate_entry = Entry(window,text="",bd=2,width=20)
rate_entry.place(x=225,y=132)

time_label = Label(window,text="Write your time",font=("Calibri",12),fg = "white",bg = "seagreen",bd=2)
time_label.place(x=20,y=170)

time_entry = Entry(window,text="",bd=2,width=20)
time_entry.place(x=225,y=172)

calculate_button = Button(window,text="CALCULATE",fg="white",bg="seagreen",bd=4,command=calculate_interest)
calculate_button.place(x=10,y=250)

result_frame = LabelFrame(window,text="Interest",bg="seagreen",font=("Calibri",12))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=300)

result_label = Label(result_frame,text="",bg="seagreen",font=("Calibri",12),width=55)
result_label.place(x=20,y=20)
result_label.pack()


window.mainloop()