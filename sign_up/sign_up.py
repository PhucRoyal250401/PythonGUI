from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title('Sign Up')
root.geometry('925x500+300+200')
root.configure(bg='white')
root.resizable(False, False)


def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            file = open('./sign_up/datasheet.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('./sign_up/datasheet.txt', 'w')
            file.write(str(r))

            messagebox.showinfo('Signup', 'Sign up successfully')

        except:
            file = open('./sign_up/datasheet.txt', 'w')
            pp = str({username, password})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalid', 'Both password should match')


def sign():
    root.destroy()  # Close GUI


img = PhotoImage(file='./sign_up/login.png')
Label(root, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(root, width=350, height=390, bg='white')
frame.place(x=480, y=50)

heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


# ------------------------
def on_enter(e):
    if user.get() == 'Username':
        user.delete(0, 'end')


def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, fg='black', border=0, bg='white',
             font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


# ------------------------
def on_enter(e):
    if code.get() == 'Password':
        code.delete(0, 'end')


def on_leave(e):
    if code.get() == '':
        code.insert(0, 'Password')


code = Entry(frame, width=25, fg='black', border=0, bg='white',
             font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


# ------------------------
def on_enter(e):
    if confirm_code.get() == 'Confirm Password':
        confirm_code.delete(0, 'end')


def on_leave(e):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'Confirm Password')


confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white',
                     font=('Microsoft YaHei UI Light', 11))
confirm_code.place(x=30, y=220)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind('<FocusIn>', on_enter)
confirm_code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)


# ------------------------
Button(frame, width=42, pady=7, text='Sign up',
       bg='#57a1f8', fg='white', border=0, command=signup).place(x=25, y=280)

label = Label(frame, text="I have an account", fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=90, y=320)

sign_in = Button(frame, width=6, text='Sign in', border=0,
                 bg='white', fg='#57a1f8', cursor='hand2', command=sign)
sign_in.place(x=200, y=320)

root.mainloop()
