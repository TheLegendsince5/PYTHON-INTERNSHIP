import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

def check():
    Name = name.get()
    Age = age.get()
    Email = email.get()
    Gender = gender.get()
    Hobbies = []
    if hobby1.get(): Hobbies.append("Reading")
    if hobby2.get(): Hobbies.append("Traveling")
    if hobby3.get(): Hobbies.append("Gaming")
    
    if not Name or not Age or not Email or not Gender or not Hobbies:
        noti.set("Please fill all the fields")
        return
    
    if not Name.isalpha():
        noti.set("Name should contain only alphabets")
        return

    if not Age.isdigit():
        noti.set("Age should be a number")
        return
    
    if "@" not in Email or "." not in Email:
        noti.set("Please enter a valid email address")
        return

    details = f"Name: {Name}\nAge: {Age}\nEmail: {Email}\nGender: {Gender}\nHobbies: {', '.join(Hobbies)}"
    messagebox.showinfo("Submission Successful", details)
    noti.set("Entered successfully")

def clear():
    name.set("")
    age.set("")
    email.set("")
    gender.set("")
    hobby1.set(False)
    hobby2.set(False)
    hobby3.set(False)
    noti.set("")

def save():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(f"Name: {name.get()}\n")
            file.write(f"Age: {age.get()}\n")
            file.write(f"Email: {email.get()}\n")
            file.write(f"Gender: {gender.get()}\n")
            hobbies = [h for h in ["Reading", "Traveling", "Gaming"] if globals()[f'hobby{["Reading", "Traveling", "Gaming"].index(h)+1}'].get()]
            file.write(f"Hobbies: {', '.join(hobbies)}\n")
        messagebox.showinfo("Save", "Details saved successfully!")

def load():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            name.set(lines[0].split(": ")[1].strip())
            age.set(lines[1].split(": ")[1].strip())
            email.set(lines[2].split(": ")[1].strip())
            gender.set(lines[3].split(": ")[1].strip())
            hobbies = lines[4].split(": ")[1].strip().split(', ')
            hobby1.set("Reading" in hobbies)
            hobby2.set("Traveling" in hobbies)
            hobby3.set("Gaming" in hobbies)
        noti.set("Details loaded successfully!")

root = tk.Tk()
root.geometry("400x500")
root.configure(bg="purple")
root.title("Enhanced Registration Form")

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.map('TButton', foreground=[('active', 'blue')], background=[('active', 'lightgray')])

ttk.Label(root, text="Registration", background="violet", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
ttk.Label(root, text="Name", background="violet", width=10).grid(row=1, column=0, pady=5)
name = tk.StringVar()
ttk.Entry(root, textvariable=name, width=30).grid(row=1, column=1, pady=5)

ttk.Label(root, text="Age", background="violet", width=10).grid(row=2, column=0, pady=5)
age = tk.StringVar()
ttk.Entry(root, textvariable=age, width=30).grid(row=2, column=1, pady=5)

ttk.Label(root, text="Email", background="violet", width=10).grid(row=3, column=0, pady=5)
email = tk.StringVar()
ttk.Entry(root, textvariable=email, width=30).grid(row=3, column=1, pady=5)

ttk.Label(root, text="Gender", background="violet", width=10).grid(row=4, column=0, pady=5)
gender = tk.StringVar()
ttk.Radiobutton(root, text="Male", variable=gender, value="Male").grid(row=4, column=1, sticky="w")
ttk.Radiobutton(root, text="Female", variable=gender, value="Female").grid(row=4, column=1)
ttk.Radiobutton(root, text="Other", variable=gender, value="Other").grid(row=4, column=1, sticky="e")

ttk.Label(root, text="Hobbies", background="violet", width=10).grid(row=5, column=0, pady=5)
hobby1 = tk.BooleanVar()
hobby2 = tk.BooleanVar()
hobby3 = tk.BooleanVar()
ttk.Checkbutton(root, text="Reading", variable=hobby1).grid(row=5, column=1, sticky="w")
ttk.Checkbutton(root, text="Traveling", variable=hobby2).grid(row=5, column=1)
ttk.Checkbutton(root, text="Gaming", variable=hobby3).grid(row=5, column=1, sticky="e")

noti = tk.StringVar()
ttk.Label(root, textvariable=noti, background="purple", foreground="yellow", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=2, pady=10)

ttk.Button(root, text="Enter", command=check).grid(row=7, column=0, pady=5, padx=5)
ttk.Button(root, text="Clear", command=clear).grid(row=7, column=1, pady=5, padx=5)
ttk.Button(root, text="Save", command=save).grid(row=8, column=0, pady=5, padx=5)
ttk.Button(root, text="Load", command=load).grid(row=8, column=1, pady=5, padx=5)

root.mainloop()
