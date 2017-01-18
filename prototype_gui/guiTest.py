import Tkinter as tk

def generate():
    """ Generate function gives a standard layout of an American Address.

    Uses the tkinter library to display an americanized address in the gui.
    
    """
    name = name_entry.get()
    street = street_entry.get()
    loc = loc_entry.get()
    if len(name) > 0 and len(street) > 0 and len(loc) > 0:
        address = name + "\n" + street + "\n" + loc
        address_label = tk.Label(address_book, text = address)
        address_label.grid(row = 3, column = 1, sticky = tk.W, padx = 20, pady = 30)

def openAd():
    """ Currently not implemented. Will eventually open an address. """
    open_label = tk.Label(address_book, text = "I do nothing yet")
    open_label.grid(row = 4, column = 1, sticky = tk.W, padx = 20, pady = 30)

def save():
    """ Currently not implemented. Will eventually save an address. """
    save_label = tk.Label(address_book, text = "I do nothing yet")
    save_label.grid(row = 5, column = 1, sticky = tk.W, padx = 20, pady = 30)

def load():
    """ Currently not implemented. Will eventually save an address. """
    load_label = tk.Label(address_book, text = "I do nothing yet")
    load_label.grid(row = 6, column = 1, sticky = tk.W, padx = 20, pady = 30)


# Initial setup of gui.
# TODO: We need to move all this code to a class that abstracts away from TK. - Zach 2017-01-17


# Instantiating Labels and their entry fields. 
address_book = tk.Tk()

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


# Below code sets up buttons and gives then a command to execute when clicked

generate_button = tk.Button(address_book, text = "Generate address", command = generate)
generate_button.grid(row = 7, column = 0, columnspan = 2, pady = 30)

open_button = tk.Button(address_book, text = "Open address book", command = openAd)
open_button.grid(row = 8, column = 0, columnspan = 2, pady = 30)

save_button = tk.Button(address_book, text = "save address book", command = save)
save_button.grid(row = 9, column = 0, columnspan = 2, pady = 30)

load_button = tk.Button(address_book, text = "load address book", command = load)
load_button.grid(row = 10, column = 0, columnspan = 2, pady = 30)
address_book.mainloop()
