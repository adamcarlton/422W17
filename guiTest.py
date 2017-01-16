import Tkinter as tk

address_book = tk.Tk()
#
#initial setup of gui. Instantiating Labels and their entry fields.
#
name_label = tk.Label(address_book, text = "First and Last name of Person:")
name_label.grid(row = 0, column = 0, sticky = tk.W, padx = 20, pady = 30)
name_entry = tk.Entry(address_book)
name_entry.grid(row = 0, column = 1, padx = 20)

street_label = tk.Label(address_book, text = "Street address of Person:")
street_label.grid(row = 1, column = 0, sticky = tk.W, padx = 20, pady = 30)
street_entry = tk.Entry(address_book)
street_entry.grid(row = 1, column = 1, padx = 20)

loc_label = tk.Label(address_book, text = "City, State, Zipcode of Person")
loc_label.grid(row = 2, column = 0, sticky = tk.W, padx = 20, pady = 30)
loc_entry = tk.Entry(address_book)
loc_entry.grid(row = 2, column = 1, padx = 20)
#
#generate function gives a standard layout of an address
#
def generate():
    name = name_entry.get()
    street = street_entry.get()
    loc = loc_entry.get()
    if len(name) > 0 and len(street) > 0 and len(loc) > 0:
        address = name + "\n" + street + "\n" + loc
        address_label = tk.Label(address_book, text = address)
        address_label.grid(row = 3, column = 1, sticky = tk.W, padx = 20, pady = 30)
#
#openAd will be used for opening an address book
#
def openAd():
    open_label = tk.Label(address_book, text = "I do nothing yet")
    open_label.grid(row = 4, column = 1, sticky = tk.W, padx = 20, pady = 30)

#
#save will be used for saving the current address book
#
def save():
    save_label = tk.Label(address_book, text = "I do nothing yet")
    save_label.grid(row = 5, column = 1, sticky = tk.W, padx = 20, pady = 30)

#
#load will used to load an existing address book
#
def load():
    load_label = tk.Label(address_book, text = "I do nothing yet")
    load_label.grid(row = 6, column = 1, sticky = tk.W, padx = 20, pady = 30)

#
#below code sets up buttons and gives then a command to execute when clicked
#
generate_button = tk.Button(address_book, text = "Generate address", command = generate)
generate_button.grid(row = 7, column = 0, columnspan = 2, pady = 30)

open_button = tk.Button(address_book, text = "Open address book", command = openAd)
open_button.grid(row = 8, column = 0, columnspan = 2, pady = 30)

save_button = tk.Button(address_book, text = "save address book", command = save)
save_button.grid(row = 9, column = 0, columnspan = 2, pady = 30)

load_button = tk.Button(address_book, text = "load address book", command = load)
load_button.grid(row = 10, column = 0, columnspan = 2, pady = 30)
address_book.mainloop()
