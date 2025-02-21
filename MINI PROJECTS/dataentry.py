import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accepted=accept_var.get()
    if accepted=="Accepted":


      firstname=first_name_entry.get()
      lastname=last_name_entry.get()
      if firstname and lastname:
         title=title_combobox.get()
         age=age_spinbox.get()
         nationality=nationality_label_entry.get()
    

         registration_status=reg_status_var.get()
         number_of_courses=numcourses_spinbox.get()
         number_of_semisters=numsem_spinbox.get()
    
         print("First name:",firstname,"Last name:",lastname)
         print("Title:",title,"Age:",age,"Nationality:",nationality)
         print("Registration Status:",registration_status)
         print("Courses:",number_of_courses,"Semister:",number_of_semisters)
         print("Registration status", registration_status)
         print("------------------------------------------")
      else:
         tkinter.messagebox.showwarning(title="Error",message="firstname and lastname are required")   
    else:
       tkinter.messagebox.showwarning(title="Error",message="You have not accepted terms and conditions")
       print("Error.") 
    


window=tkinter.Tk()
window.title("Data entry form")
frame=tkinter.Frame(window)
frame.pack()

user_info_frame=tkinter.LabelFrame(frame,text="User information")
user_info_frame.grid(row=0,column=0 ,padx=20 ,pady=10)

first_name_label=tkinter.Label(user_info_frame,text="First name")
first_name_label.grid(row=0,column=0)

last_name_label=tkinter.Label(user_info_frame,text="Last name")
last_name_label.grid(row=0,column=1)

first_name_entry=tkinter.Entry(user_info_frame)
last_name_entry=tkinter.Entry(user_info_frame)

first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title_label=tkinter.Label(user_info_frame,text="Title")
title_combobox=ttk.Combobox(user_info_frame , values=["","Mr.","Ms.","Dr."])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_label=tkinter.Label(user_info_frame,text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3 ,column=0)

nationality_label=tkinter.Label(user_info_frame,text="Nationality")
nationality_label_entry=tkinter.Entry(user_info_frame)

nationality_label.grid(row=2,column=1)
nationality_label_entry.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

courses_frame=tkinter.LabelFrame(frame)
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)

registered_label=tkinter.Label(courses_frame,text="Registration Status")

reg_status_var=tkinter.StringVar(value="Not Registered") #contain the value of check button
registered_check=tkinter.Checkbutton(courses_frame,text="Currently Registered",
                                     variable=reg_status_var,onvalue="Registered",offvalue="Not Registered")
registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

numcourses_label=tkinter.Label(courses_frame,text="Completed Courses")
numcourses_spinbox=tkinter.Spinbox(courses_frame, from_=0,to='infinity')
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

numsem_label=tkinter.Label(courses_frame,text="Completed Sem")
numsem_spinbox=tkinter.Spinbox(courses_frame,from_=0 ,to=8)
numsem_label.grid(row=0,column=2)
numsem_spinbox.grid(row=1,column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)


terms_frame=tkinter.LabelFrame(frame,text="Terms And Conditions")    
terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)

accept_var= tkinter.StringVar(value="Not accepted")

terms_check=tkinter.Checkbutton(terms_frame,text="I accept the terms and condition",
                                variable=accept_var,onvalue="Accepted",offvalue="Not Accepted")
terms_check.grid(row=0,column=0)

button=tkinter.Button(frame,text="Enter Data",command= enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)

window.mainloop()



