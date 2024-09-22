import tkinter

root=tkinter.Tk()
root.title("My first GUI")
root.geometry('500x500')

label=tkinter.Label(root,text="Hello world!",font=("arial",18))
label.pack(padx=10,pady=10)

textbox=tkinter.Text(root,font=("times",10))
textbox.pack(padx=5,pady=5)

button=tkinter.Button(root,text="Click here",font=("arial",10))
button.pack()

root.mainloop()