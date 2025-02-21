from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handel_login():
    email=email_input.get()
    password=password_input.get()
    print(email,password)

    if email =='sanjana324@gmail.com' and password == '1234':
        messagebox.showinfo('Login','Login successful!')
    else:
        messagebox.showerror('Error','Login Failed!')



root = Tk()
root.title("Login Form")

root.maxsize(400,400)

root.geometry("350x500")
root.configure(background='#0096DC')
img = Image.open('flipkart-logo.png')
resized_img = img.resize((70,70))


img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img)
img_label.pack(pady=(10,10))

text_label=Label(root,text='Flipkart',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdan',14))

email_label=Label(root,text="Enter Email",fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input=Entry(root,width=50)                   #to create a input box
email_input.pack(ipady=6,pady=(1,15))              #display the input(pack)
                                                   #ipady=width of y axis
                                                   #pady=space between

password_label = Label(root, text="Enter Password", fg='white', bg='#0096DC')
password_label.pack(pady=(20, 5))
password_label.config(font=('verdana', 12))

password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1, 15))

login_button=Button(root,text="Login Here",fg="white",bg="black",command=handel_login)
login_button.pack(ipady=6, pady=(10,2))
login_button.config(font=('verdana',12,'bold'))


root.mainloop()

