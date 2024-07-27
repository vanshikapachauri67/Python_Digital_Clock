from tkinter import*
import datetime

clock = Tk()
clock.geometry("1000x700")
clock.title("***Digital clock***")
clock.configure(background="light green")


def date_time():
    now = datetime.datetime.now()
    hr =now.strftime("%I")
    m = now.strftime("%M")
    s = now.strftime("%S")
    am = now.strftime("%p")
    d = now.strftime("%d")
    month = now.strftime("%b")
    y = now.strftime("%y")
    day =now.strftime("%a")
    lab_hr.config(text=hr)
    lab_m.config(text=m)
    lab_s.config(text=s)
    lab_am.config(text=am)
    lab_d.config(text=d)
    lab_mth.config(text=month)
    lab_y.config(text=y)
    lab_dy.config(text=day)
    lab_hr.after(200,date_time)

lab_hr = Label(clock,text="00",font=("Time New Roman", 40, "bold"),fg="white",bg="red")
lab_hr.place(x=150,y=20,height=100,width=100)

lab_m = Label(clock,text="00",font=("Time New Roman", 40, "bold"),fg="white",bg="red")
lab_m.place(x=350,y=20,height=100,width=100)

lab_s = Label(clock,text="00",font=("Time New Roman", 40, "bold"),fg="white",bg="red")
lab_s.place(x=550,y=20,height=100,width=100)

lab_am = Label(clock,text="00",font=("Time New Roman", 40, "bold"),fg="white",bg="red")
lab_am.place(x=750,y=20,height=100,width=100)


lab_hr_text = Label(clock,text="Hour",font=("Time New Roman", 20, "bold"),fg="black",bg="yellow")
lab_hr_text.place(x=150,y=170,height=50,width=100)

lab_m_text = Label(clock,text="Min",font=("Time New Roman", 20, "bold"),fg="black",bg="yellow")
lab_m_text.place(x=350,y=170,height=50,width=100)

lab_s_text = Label(clock,text="Sec",font=("Time New Roman", 20, "bold"),fg="black",bg="yellow")
lab_s_text.place(x=550,y=170,height=50,width=100)

lab_am_text = Label(clock,text="Am/Pm",font=("Time New Roman", 20, "bold"),fg="black",bg="yellow")
lab_am_text.place(x=750,y=170,height=50,width=100)

lab_d = Label(clock,text="00",font=("Time New Roman", 40, "bold"),fg="white",bg="red")
lab_d.place(x=150,y=320,height=100,width=100)

lab_mth = Label(clock,text="00",font=("Time New Roman", 40, "bold"),fg="white",bg="red")
lab_mth.place(x=350,y=320,height=100,width=100)

lab_y = Label(clock,text="00",font=("Time New Roman", 40, "bold"),fg="white",bg="red")
lab_y.place(x=550,y=320,height=100,width=100)

lab_dy = Label(clock,text="00",font=("Time New Roman", 40, "bold"),fg="white",bg="red")
lab_dy.place(x=750,y=320,height=100,width=100)

lab_d_text = Label(clock,text="Date",font=("Time New Roman", 20, "bold"),fg="black",bg="yellow")
lab_d_text.place(x=150,y=470,height=50,width=100)

lab_mth_text = Label(clock,text="Month",font=("Time New Roman", 20, "bold"),fg="black",bg="yellow")
lab_mth_text.place(x=350,y=470,height=50,width=100)

lab_y_text = Label(clock,text="Year",font=("Time New Roman", 20, "bold"),fg="black",bg="yellow")
lab_y_text.place(x=550,y=470,height=50,width=100)

lab_dy_text = Label(clock,text="Day",font=("Time New Roman", 20, "bold"),fg="black",bg="yellow")
lab_dy_text.place(x=750,y=470,height=50,width=100)

date_time()

clock.mainloop()