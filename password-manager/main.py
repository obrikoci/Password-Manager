from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- SEARCH GENERATOR ------------------------------- #
def search():
    website = web_entry.get()
    try:
        with open("/Users/your_user/Desktop/data_pass.json", "r") as data_file:
                data = json.load(data_file)
    except:
        messagebox.showinfo(title="Error!", message="Empty File. No Data Found.")
    else:
        if website in data:
            email = data[website]["Email/Username"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Website not Found", message=f"The details for {website} do not exist.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers )for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "Email/Username": user,
            "Password": password,
        }
    }

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Important!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail/Username:{user} "
                                                      f"\nPassword:{password}\n Do you want to save?")
        if is_ok:
            try:
                with open("/Users/obrikoci/Desktop/data_pass.json", "r") as data_file:
                    data = json.load(data_file)
            except:
                with open("/Users/obrikoci/Desktop/data_pass.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
                    messagebox.showinfo(title="Succsess",
                                        message="Check your password file to see your new added details.")
            else:
                data.update(new_data)

                with open("/Users/obrikoci/Desktop/data_pass.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                    messagebox.showinfo(title="Succsess",
                                        message="Check your password file to see your new added details.")
            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)
                web_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

web_entry = Entry(width=21)
web_entry.focus()
web_entry.grid(row=1, column=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

user_entry = Entry(width=38)
user_entry.insert(0, "email")
user_entry.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

search_button = Button(text="Search", width=12, command=search)
search_button.grid(row=1, column=2)

pass_button = Button(text="Generate Password", width=12, command=generate_password)
pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
