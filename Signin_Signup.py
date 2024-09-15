import tkinter as tk
import json
from tkinter import messagebox


def on_signin_submit(signin_win, email, password):
    try:
        with open("text.txt", "r", encoding="utf8") as file:
            data = json.load(file)
    except:
        data = {}
    if email+password not in data:
        messagebox.showerror(title="Error", message="Wrong password or email id.")
    else:
        information = "Here are your informations-\n\n"
        for key in data[email+password]:
            information += f"{key}:    {data[email+password][key]}\n" 
            
        info = tk.Toplevel(signin_win, bg="#FFE26F")
        tk.Label(
            info,
            text=information,
            padx=15,
            pady=15,
            justify="left",
            fg="#203E5F",
            bg="#FFE26F"
        ).grid(row=0, column=0, sticky="w")
def on_signin():
    signin_win = tk.Toplevel(root, padx=25, pady=25,  bg="#FFE26F")
    email = tk.StringVar()
    tk.Label(
        signin_win,
        text="Email: ",
        padx=15,
        pady=15, 
        fg="#203E5F",
        bg="#FFE26F"       
        ).grid(row=0, column=0, sticky="w")
    tk.Entry(
        signin_win,
        textvariable=email,
        width=35,
    ).grid(row=0, column=1, sticky="w")
    
    password = tk.StringVar()
    tk.Label(
        signin_win,
        text="Password: ",
        padx=15,
        pady=15,
        fg="#203E5F",
        bg="#FFE26F"
    ).grid(row=1, column=0)
    tk.Entry(
        signin_win,
        textvariable=password,
    ).grid(row=1, column=1,sticky="w")
    
    tk.Button(
        signin_win,
        text="Sign in",
        font=("Arial", 13),
        command=lambda:on_signin_submit(signin_win, email.get(), password.get()),
        bg="#203E5F",
        fg="white"
    ).grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="e")
    
        
        
        
def on_submit(name, email, address, mob_no, _state, country, college, dept, roll, gen, password, cpassword, signup_win):
    if password.get() != cpassword.get():
        messagebox.showerror(title="Error", message="Passwords are not matching.")
    else:
        if gen:
            gender = "male"
        else:
            gender = "female"
        data_dict = {
            email.get()+password.get():{
                "name": name.get(),
            "email": email.get(),
            "address": address.get(),
            "mobile": mob_no.get(),
            "state": _state.get(),
            "country": country.get(),
            "college": college.get(),
            "department": dept.get(),
            "Roll no": roll.get(),
            "Gender": gender,
            "password": password.get()
            }
        }
        try:
            with open("text.txt", "r", encoding="utf8") as file:
                data = json.load(file)
        except:
            with open("text.txt", "w", encoding="utf8") as file:
                data={}
        if email.get()+password.get() in data:
            messagebox.showerror(title="Error", message="This user already exist.")
        else:
            with open("text.txt", "w", encoding="utf8") as file:
                    data.update(data_dict)
                    json.dump(data, file, indent=4)
            signup_win.destroy()
            messagebox.showinfo(title="Success", message="You successfully signed up.")
            
            
def on_signup():
    signup_win=tk.Toplevel(root)
    signup_win.title("title")
    signup_win.config(bg="#FFE26F", padx=15, pady=15)
    tk.Label(
        signup_win,
        text="Fill in the following information:",
        padx=15,
        pady=15,
        bg="#FFE26F",
        fg="#203E5F",
        font=("Arial", 14)
        ).grid(row=0, column=0, columnspan=2, sticky="w")
    
    name = tk.StringVar(signup_win)
    tk.Label(signup_win, text="Name: ", padx=15, pady=15, bg="#FFE26F", fg="#1160AA").grid(row=1, column=0, sticky="w")
    tk.Entry(signup_win, textvariable=name).grid(row=1, column=1)
    
    email = tk.StringVar(signup_win)
    tk.Label(
        signup_win,
        text="Email: ",
        padx=15,
        pady=15,
        bg="#FFE26F",
        fg="#1160AA"
        ).grid(row=1, column=2, sticky="w")
    tk.Entry(
        signup_win, 
        textvariable=email,
        ).grid(row=1, column=3)
    
    address = tk.StringVar(signup_win)
    tk.Label(
        signup_win,
        text="Adress: ",
        padx=15,
        pady=15,
        bg="#FFE26F",
        fg="#1160AA"
    ).grid(row=2, column=0, sticky="w")
    tk.Entry(
        signup_win,
        textvariable=address,
    ).grid(row=2, column=1)
    
    mob_no = tk.StringVar(signup_win)
    tk.Label(
        signup_win,
        text="Mobile no.: ",
        padx=15,
        pady=15,
        bg="#FFE26F",
        fg="#1160AA"
    ).grid(row=2, column=2, sticky="w")
    tk.Entry(
        signup_win,
        textvariable=mob_no,
    ).grid(row=2, column=3)
    
    country = tk.StringVar(signup_win)
    tk.Label(
        signup_win,
        text="Country: ",
        padx=15,
        pady=15,
        bg="#FFE26F",
        fg="#1160AA"
    ).grid(row=3, column=0, sticky="w")
    tk.Entry(
        signup_win,
        textvariable=country,
    ).grid(row=3, column=1)
    
    _state = tk.StringVar(signup_win)
    tk.Label(
        signup_win,
        text="State: ",
        padx=15,
        pady=15,
        bg="#FFE26F",
        fg="#1160AA"
    ).grid(row=3, column=2, sticky="w")
    tk.Entry(
        signup_win,
        textvariable=_state,
    ).grid(row=3, column=3)
    
    college = tk.StringVar(signup_win)   
    colleges = ["HIT", "IEM", "Techno India", "SNU", "MSIT", "NSEC", "KIIT"] 
    tk.Label(
        signup_win,
        text="College name: ",
        padx=15,
        pady=15,
        bg="#FFE26F",
        fg="#1160AA"
    ).grid(row=4, column=0, sticky="w")
    tk.OptionMenu(
        signup_win,
        college,
        *colleges,
    ).grid(row=4, column=1)
    
    dept = tk.StringVar(signup_win) 
    depts = ["CSE", "IT", "ECE", "CSEDS", "CSEAIML", "CSEIOT", "ETCE", "CE", "CHE", "ME", "EE"]   
    tk.Label(
        signup_win,
        text="Department name: ",
        padx=15,
        pady=15,
        bg="#FFE26F",
       fg="#1160AA"
    ).grid(row=4, column=2, sticky="w")
    tk.OptionMenu(
        signup_win,
        dept,
        *depts,
    ).grid(row=4, column=3)
    
    roll = tk.StringVar(signup_win)    
    tk.Label(
        signup_win,
        text="Roll no.: ",
        padx=15,
        pady=15,
        fg="#1160AA",
        bg="#FFE26F"
    ).grid(row=5, column=0, sticky="w")
    tk.Entry(
        signup_win,
        textvariable=roll,
    ).grid(row=5, column=1)
    
    gen_frame = tk.Frame(signup_win, bg="#FFE26F")
    gen_frame.grid(row=5, column=3)    
    gender = tk.BooleanVar(gen_frame)
    tk.Label(
        signup_win,
        text="Choose gender: ",
        padx=15,
        pady=15,
        bg="#FFE26F",
        fg="#1160AA"
    ).grid(row=5, column=2, sticky="w")
    tk.Radiobutton(
        gen_frame,
        variable=gender,
        text="Male",
        value=True,
         bg="#FFE26F"
    ).grid(row=5, column=3)
    tk.Radiobutton(
        gen_frame,
        variable=gender,
        text="Female",
        value=False,
         bg="#FFE26F"
    ).grid(row=5, column=4)
    
    password = tk.StringVar()    
    tk.Label(
        signup_win,
        text="Password",
        padx=15,
        pady=15,
        bg="#FFE26F",
        fg="#1160AA"
    ).grid(row=6, column=0, sticky="w")
    tk.Entry(
        signup_win,
        textvariable=password,
    ).grid(row=6, column=1)
    
    cpassword = tk.StringVar()    
    tk.Label(
        signup_win,
        text="Confirm password",
        padx=15,
        pady=15,
        bg="#FFE26F",
        fg="#1160AA"
    ).grid(row=6, column=2, sticky="w")
    tk.Entry(
        signup_win,
        textvariable=cpassword,
    ).grid(row=6, column=3)
    
    signup_btn = tk.Button(
        signup_win,
        text="Sign up",
        font=("Arial", 13),
        command=lambda:on_submit(name, email, address, mob_no, _state, country, college, dept, roll, gender.get(), password, cpassword, signup_win),
        padx=5,
        pady=5,
        bg="#1160AA",
        fg="white"
        ).grid(row=17, column=0, columnspan=4, sticky="e")
    

    
root = tk.Tk()
root.title("Sign up page")
root.config(bg="#EEC550")

tk.Label(
    root, 
    text="Welcome", 
    font=("Arial", 50, "normal"),
    padx=30,
    pady=30,
    bg="#EEC550",
    fg="#203E5F"
    ).grid(row=0, columnspan=2)

tk.Button(
    root,
    text="Sign up",
    font=("Arial",15),
    fg="white",
    bg="#203E5F",
    command=on_signup
    ).grid(row=1, column=0, sticky="e", padx=20, pady=30)
tk.Button(
    root,
    text="Sign in",
    font=("Arial",15),
    fg="white",
    bg="#203E5F",
    command=on_signin
    ).grid(row=1, column=1, sticky="w", padx=20, pady=30)


root.mainloop()
