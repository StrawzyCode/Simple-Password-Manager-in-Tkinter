from tkinter import *
from tkinter import messagebox
import os


def new_password():
 
    new_window = Toplevel()
    new_window.title("Create a new password")
    new_window.geometry("400x300")
    new_window.resizable(0,0)
    new_window.configure(bg="#e0e0e0")
   
    Label(new_window, text="Account Name", bg="#e0e0e0", font=("Arial", 15)).grid(row=0, column=0)
    account_name = Entry(new_window, width=30)
    account_name.grid(row=0, column=1, padx=10, pady=10)
    Label(new_window, text="Password", bg="#e0e0e0", font=("Arial", 15)).grid(row=1, column=0)
    password = Entry(new_window, width=30)
    password.grid(row=1, column=1, padx=10, pady=10)
    Label(new_window, text="Confirm Password", bg="#e0e0e0", font=("Arial", 15)).grid(row=2, column=0)
    confirm_password = Entry(new_window, width=30)
    confirm_password.grid(row=2, column=1, padx=10, pady=10)
    
   
    def save_password():
        account = account_name.get()
        password1 = password.get()
        password2 = confirm_password.get()
        
   
        if password1 != password2:
            messagebox.showerror("Error", "Passwords do not match")
        else:
            file = open("passwords.txt", "a")
            
            file.write(account + " " + password1 + " ")
            file.close()

            messagebox.showinfo("Success", "Password saved")

            new_window.destroy()
            

    Button(new_window, text="Save Password", width=15, font=("Arial", 15), command=save_password).grid(row=3, column=1, pady=10)

def retrieve_password():
    retrieve_window = Toplevel()
    retrieve_window.title("Retrieve a password")
    retrieve_window.geometry("400x300")
    retrieve_window.resizable(0,0)
    retrieve_window.configure(bg="#e0e0e0")
  
    Label(retrieve_window, text="Account Name", bg="#e0e0e0", font=("Arial", 15)).grid(row=0, column=0)
    account_name = Entry(retrieve_window, width=30)
    account_name.grid(row=0, column=1, padx=10, pady=10)

    def retrieve():
        account = account_name.get()
        file = open("passwords.txt", "r")

        data = file.read()

        if account in data:
            data = data.split()

            index = data.index(account)

            password = data[index+1]

            messagebox.showinfo("Password", "Password for " + account + " is " + password)

            retrieve_window.destroy()
            
        else:
            messagebox.showerror("Error", "Account not found")

            retrieve_window.destroy()

    Button(retrieve_window, text="Retrieve Password", width=15, font=("Arial", 15), command=retrieve).grid(row=1, column=1, pady=10)

def delete_password():
    delete_window = Toplevel()
    delete_window.title("Delete a password")
    delete_window.geometry("400x300")
    delete_window.resizable(0,0)
    delete_window.configure(bg="#e0e0e0")
   
    Label(delete_window, text="Account Name", bg="#e0e0e0", font=("Arial", 15)).grid(row=0, column=0)
    account_name = Entry(delete_window, width=30)
    account_name.grid(row=0, column=1, padx=10, pady=10)

    def delete():
        account = account_name.get()
        file = open("passwords.txt", "r")
        
        data = file.read()

        if account in data:
            data = data.split()

            index = data.index(account)

            del data[index]
            del data[index]

            file = open("passwords.txt", "w")

            for i in data:
                file.write(i + " ")

            file.close()

            messagebox.showinfo("Success", "Password deleted")

            delete_window.destroy()
            
        else:
            messagebox.showerror("Error", "Account not found")
            delete_window.destroy()
        
    Button(delete_window, text="Delete Password", width=15, font=("Arial", 15), command=delete).grid(row=1, column=1, pady=10)
def add_password():
    add_window = Toplevel()
    add_window.title("Add a password")
    add_window.geometry("400x300")
    add_window.resizable(0,0)
    add_window.configure(bg="#e0e0e0")
    
    Label(add_window, text="Account Name", bg="#e0e0e0", font=("Arial", 15)).grid(row=0, column=0)
    account_name = Entry(add_window, width=30)
    account_name.grid(row=0, column=1, padx=10, pady=10)
    Label(add_window, text="Password", bg="#e0e0e0", font=("Arial", 15)).grid(row=1, column=0)
    password = Entry(add_window, width=30)
    password.grid(row=1, column=1, padx=10, pady=10)
    Label(add_window, text="Confirm Password", bg="#e0e0e0", font=("Arial", 15)).grid(row=2, column=0)
    confirm_password = Entry(add_window, width=30)
    confirm_password.grid(row=2, column=1, padx=10, pady=10)

    def save_password():
        account = account_name.get()
        password1 = password.get()
        password2 = confirm_password.get()

        if password1 != password2:
            messagebox.showerror("Error", "Passwords do not match")
        else:
            file = open("passwords.txt", "a")

            file.write(account + " " + password1 + " ")
            file.close()
            
            messagebox.showinfo("Success", "Password saved")
 
            add_window.destroy()
    
    Button(add_window, text="Save Password", width=15, font=("Arial", 15), command=save_password).grid(row=3, column=1, pady=10)

def change_password():
    change_window = Toplevel()
    change_window.title("Change a password")
    change_window.geometry("400x300")
    change_window.resizable(0,0)
    change_window.configure(bg="#e0e0e0")
   
    Label(change_window, text="Account Name", bg="#e0e0e0", font=("Arial", 15)).grid(row=0, column=0)
    account_name = Entry(change_window, width=30)
    account_name.grid(row=0, column=1, padx=10, pady=10)
    Label(change_window, text="New Password", bg="#e0e0e0", font=("Arial", 15)).grid(row=1, column=0)
    new_password = Entry(change_window, width=30)
    new_password.grid(row=1, column=1, padx=10, pady=10)
    Label(change_window, text="Confirm Password", bg="#e0e0e0", font=("Arial", 15)).grid(row=2, column=0)
    confirm_password = Entry(change_window, width=30)
    confirm_password.grid(row=2, column=1, padx=10, pady=10)

    def change():
        account = account_name.get()
        password1 = new_password.get()
        password2 = confirm_password.get()

        if password1 != password2:
            messagebox.showerror("Error", "Passwords do not match")
        else:
            file = open("passwords.txt", "r")

            data = file.read()

            if account in data:
                data = data.split()

                index = data.index(account)

                data[index+1] = password1

                file = open("passwords.txt", "w")

                for i in data:
                    file.write(i + " ")

                file.close()

                messagebox.showinfo("Success", "Password changed")

                change_window.destroy()

            else:
                messagebox.showerror("Error", "Account not found")

                change_window.destroy()

    Button(change_window, text="Change Password", width=15, font=("Arial", 15), command=change).grid(row=3, column=1, pady=10)

def show_passwords():
    show_window = Toplevel()
    show_window.title("Show all passwords")
    show_window.geometry("400x300")
    show_window.resizable(0,0)
    show_window.configure(bg="#e0e0e0")

    file = open("passwords.txt", "r")
    
    data = file.read()

    data = data.split()

    Label(show_window, text="Account Name - Password", bg="#e0e0e0", font=("Arial", 15)).grid(row=0, column=0, padx=10, pady=10)
    Label(show_window, text=data, bg="#e0e0e0", font=("Arial", 15)).grid(row=1, column=0, padx=10, pady=10)

def show_menu():
    menu_window = Toplevel()
    menu_window.title("Menu")
    menu_window.geometry("400x300")
    menu_window.resizable(0,0)
    menu_window.configure(bg="#e0e0e0")

    Button(menu_window, text="Add a password", width=15, font=("Arial", 15), command=add_password).grid(row=0, column=0, padx=10, pady=10)
    Button(menu_window, text="Delete a password", width=15, font=("Arial", 15), command=delete_password).grid(row=1, column=0, padx=10, pady=10)
    Button(menu_window, text="Change a password", width=15, font=("Arial", 15), command=change_password).grid(row=2, column=0, padx=10, pady=10)
    Button(menu_window, text="Show all passwords", width=15, font=("Arial", 15), command=show_passwords).grid(row=3, column=0, padx=10, pady=10)


def create_account():
    create_window = Toplevel()
    create_window.title("Create an account")
    create_window.geometry("400x300")
    create_window.resizable(0,0)
    create_window.configure(bg="#e0e0e0")

    Label(create_window, text="Username", bg="#e0e0e0", font=("Arial", 15)).grid(row=0, column=0)
    new_username = Entry(create_window, width=30)
    new_username.grid(row=0, column=1, padx=10, pady=10)
    Label(create_window, text="Password", bg="#e0e0e0", font=("Arial", 15)).grid(row=1, column=0)
    new_password = Entry(create_window, width=30)
    new_password.grid(row=1, column=1, padx=10, pady=10)
    Label(create_window, text="Confirm Password", bg="#e0e0e0", font=("Arial", 15)).grid(row=2, column=0)
    confirm_password = Entry(create_window, width=30)
    confirm_password.grid(row=2, column=1, padx=10, pady=10)

    def create():
        username = new_username.get()
        password1 = new_password.get()
        password2 = confirm_password.get()

        if password1 != password2:
            messagebox.showerror("Error", "Passwords do not match")
        else:
            file = open("passwords.txt", "w")

            file.write(username + " " + password1 + " ")

            file.close()

            messagebox.showinfo("Success", "Account created")

            create_window.destroy()

    Button(create_window, text="Create Account", width=15, font=("Arial", 15), command=create).grid(row=3, column=1, pady=10)

def show_login():
    login_window = Toplevel()
    login_window.title("Login")
    login_window.geometry("400x300")
    login_window.resizable(0,0)
    login_window.configure(bg="#e0e0e0")
   
    Label(login_window, text="Username", bg="#e0e0e0", font=("Arial", 15)).grid(row=0, column=0)
    username_entry = Entry(login_window, width=30)
    username_entry.grid(row=0, column=1, padx=10, pady=10)
    Label(login_window, text="Password", bg="#e0e0e0", font=("Arial", 15)).grid(row=1, column=0)
    password_entry = Entry(login_window, width=30)
    password_entry.grid(row=1, column=1, padx=10, pady=10)
    def login():
        username = username_entry.get()
        password = password_entry.get()

        file = open("passwords.txt", "r")

        data = file.read()

        data = data.split()
        login_window.destroy()
        if username == data[0] and password == data[1]:
            show_menu()

            login_window.destroy()
        elif username == "" or password == "":
            messagebox.showerror("Error", "Please enter a username and password")
        else:
            messagebox.showerror("Error", "Incorrect username or password")
    
    Button(login_window, text="Login", width=15, font=("Arial", 15), command=login).grid(row=2, column=1, pady=10)
    Button(login_window, text="Create an account", width=15, font=("Arial", 15), command=create_account).grid(row=3, column=1, pady=10)

def show_main():
    main_window = Tk()
    main_window.title("Password Manager")
    main_window.geometry("340x300")
    main_window.resizable(0,0)
    main_window.configure(bg="#e0e0e0")
    def main_window_destroy():
        main_window.destroy()

    Label(main_window, text="Welcome to the password manager", bg="#e0e0e0", font=("Arial", 15)).grid(row=0, column=0, padx=10, pady=10)
    Label(main_window, text="Please login or create an account", bg="#e0e0e0", font=("Arial", 15)).grid(row=1, column=0, padx=10, pady=10)
    
    Button(main_window, text="Login", width=15, font=("Arial", 15), command=show_login).grid(row=2, column=0, pady=10)
    Button(main_window, text="Create an account", width=15, font=("Arial", 15), command=create_account).grid(row=3, column=0, pady=10)
    
    main_window.mainloop()

show_main()


