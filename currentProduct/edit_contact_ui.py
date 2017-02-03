from Tkinter import *
from coolDialog import CoolDialog
class EditContact(CoolDialog):
  """ Dialog is currently hard coded, which is terrible. 

  If I find time I'll update and make it dynamic.
  """
  def __init__(self, parent, address, title = None):
    self.address = address[1]
    self.delete = False
    CoolDialog.__init__(self, parent, title)

  def buttonbox(self):
    box = Frame(self)

    save = Button(box, text="Save", width=10, command=self.save, default=ACTIVE)
    save.pack(side=LEFT, padx=5, pady=5)
    delete = Button(box, text="Delete", width=10, command=self._delete)
    delete.pack(side=LEFT, padx=5, pady=5)
    cancel = Button(box, text="Cancel", width=10, command=self.cancel)
    cancel.pack(side=LEFT, padx=5, pady=5)

    self.bind("<Return>", self.save)
    self.bind("<Alt>", self.delete)
    self.bind("<Escape>", self.cancel)

    box.pack()

  def _delete(self, event=None):
    self.delete = True
    print "Yeahp!"
    if not self.validate():
        self.initial_focus.focus_set() # put focus back
        return
    self.withdraw()
    self.update_idletasks()
    self.destroy()

  def body(self, master):
    Label(master, text="First Name: ",   font='Helvetica -14').grid(row=0)
    Label(master, text="Last Name: ",    font='Helvetica -14').grid(row=1)
    Label(master, text="House Number: ", font='Helvetica -14').grid(row=2)
    Label(master, text="Street: ",       font='Helvetica -14').grid(row=3)
    Label(master, text="City: ",         font='Helvetica -14').grid(row=4)
    Label(master, text="State: ",        font='Helvetica -14').grid(row=5)
    Label(master, text="Zip: ",          font='Helvetica -14').grid(row=6)

    self.e0 = Entry(master)
    self.e1 = Entry(master)
    self.e2 = Entry(master)
    self.e3 = Entry(master)
    self.e4 = Entry(master)
    self.e5 = Entry(master)
    self.e6 = Entry(master)

    self.e0.insert(END, self.address.first_name)
    self.e1.insert(END, self.address.last_name)
    self.e2.insert(END, self.address.house_number)
    self.e3.insert(END, self.address.street)
    self.e4.insert(END, self.address.city)
    self.e5.insert(END, self.address.state)
    self.e6.insert(END, self.address.zipcode)

    self.e0.grid(row=0, column=1)
    self.e1.grid(row=1, column=1)
    self.e2.grid(row=2, column=1)
    self.e3.grid(row=3, column=1)
    self.e4.grid(row=4, column=1)
    self.e5.grid(row=5, column=1)
    self.e6.grid(row=6, column=1)
    return self.e1

  def apply(self):
    first_name   = str(self.e0.get())
    last_name    = str(self.e1.get())
    house_number = int(self.e2.get())
    street       = str(self.e3.get())
    city         = str(self.e4.get())
    state        = str(self.e5.get())
    zip_         = str(self.e6.get())
    self.result = (last_name, first_name, house_number, street, city, state, zip_)

