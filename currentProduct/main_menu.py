from Tkinter import *
from address import Address
from addressbook import AddressBook
from fileops import FileOps, AlreadyExistsException, EmptyAddressBookException
from add_contact_ui import AddContact
from edit_contact_ui import EditContact
import argparse
import tkMessageBox
import os
import sys
import tkFileDialog as filedialog

class FileFoundException(Exception):
  pass

class FileNotFoundException(Exception):
  pass


class BetterListBox(object):
  """ The wonderful listbox object doesn't work with objects """
  def __init__(self, the_list, parent, gui):
    """
    Args:
      the_list (list[tuple]): Should be a list of tuples, each item in the list
      should be a tuple of (Display string, Object)
    """
    self.the_list = the_list
    self.parent = parent
    # This is terrible Don't ever do this.
    self.gui = gui
    
  def create_contact_list_box(self, scrollbar):
    self.contact_list_box = Listbox(self.parent, yscrollcommand=scrollbar.set)
    self.contact_list_box.bind('<ButtonRelease-1>', self.click_name)
    for item in self.the_list:
      self.add_item(item)
    self.contact_list_box.pack()

  def add_item(self, item):
    self.contact_list_box.insert(END, item[0])

  def click_name(self, event):
    widget = event.widget
    selection = widget.curselection()
    addy = self.the_list[selection[0]]
    print addy[1]
    edit_contact = EditContact(self.parent, addy)
    editted_addy = edit_contact.result
    delete_addy = edit_contact.delete
    
    if editted_addy:
      new_addy = Address(*editted_addy)
      self.gui.add_contact(new_addy)
      self.gui.delete_contact(addy[1])
    elif delete_addy:
      self.gui.delete_contact(addy[1])

class GUI(object):
  """ Basic GUI for our address book """
  def __init__(self, fname=''):
    self.set_file(fname)
    if self.fname != '':
      self.load()
    self.saved = True
    self.start_gui()

  def start_gui(self):
    self.root = Tk()
    self.root.title("Address Book")
    self.set_menu_bar(self.root)
    #self.add_contact_search(self.root)
    if hasattr(self, "aBook"):
      self.list_contacts(self.aBook[self.state])
    else:
      self.new_address_book()
      self.list_contacts(self.aBook[self.state])

    self.add_new_contact_button()
    self.root.mainloop()

  def munge_contact_list(self, contact_list):
    """ Will munge the contact list for our listbox.

    Output of get_contact_list() is a triple tuple with the possibility for None
    objects. This will munge from that triple tuple to something acceptable for
    our listbox.

    Args:
      contact_list (list[tuple]): triple tuple
    
    Returns:
      tuple: double tuple with display text and address object.
    """
    contacts = []
    for contact in contact_list:
      if contact[0] != "" and contact[1] != "":
        contacts.append(("{}, {}".format(contact[1], contact[0]), contact[2]))
      elif contact[1] != "":
        contacts.append((contact[1], contact[2]))
      elif contact[0] != "":
        contacts.append((contact[0], contact[2]))
      else:
        continue
    contacts.sort()
    return contacts

  def list_contacts(self, aBook):
    """ Lists the contacts on the screen """
    if hasattr(self, "frame"):
      self.frame.destroy()
    self.frame = Frame(self.root)
    self.frame.pack(fill=BOTH, expand=YES)
    scrollbar = Scrollbar(self.frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    contact_list = self.get_contact_list(aBook)
    contacts = self.munge_contact_list(contact_list)

    bListBox = BetterListBox(contacts, self.frame, self)
    bListBox.create_contact_list_box( scrollbar)

  def add_new_contact_button(self):
    self.add_new_contact_frame = Frame(self.root)
    self.add_new_contact_frame.pack(side=BOTTOM, expand=YES)
    button = Button(self.add_new_contact_frame, text="Add new contact",
        command=self.add_contact)
    button.pack(fill=X)

  def add_contact(self, new_addy = None):
    if not new_addy:
      result = AddContact(self.root, "Add Contact").result
      if result:
        new_addy = Address(*result)
      else:
        return

    old_state = self.aBook[self.state]
    self._increment_state()
    self.aBook[self.state] = old_state
    self.aBook[self.state].add_address(new_addy)
    self.list_contacts(self.aBook[self.state])

  def delete_contact(self, addy = None):
    old_state = self.aBook[self.state]
    self._increment_state()
    self.aBook[self.state] = old_state
    self.aBook[self.state].delete_address(addy)
    self.list_contacts(self.aBook[self.state])

  def add_contact_search(self, page):
    """ Sets up the contact search box. """
    frame = Frame(page, bg='white')
    frame.pack(side=TOP, fill=X, expand=YES)
    contact_label =  Label(frame, text="Contacts", bg='white', fg='blue',
        font='Helvetica -18 bold')
    blank_label = Label(frame, text="          ", bg='white')
    # TODO: Figure out what the fuck this is.
    self.name = StringVar()
    entry_name = Entry(frame, textvariable=self.name, bg='white')
    search_name = Button(frame, text="Search", bg='white')
    # TODO: Figure out what the fuck these blank labels do.
    label3 = Label(frame,text="", bg='white')
    label4 = Label(frame,text="  ", bg='white')

    # grid the word "Contacts" and search button
    contact_label.grid(row = 0, column = 0)
    blank_label.grid(row = 0, column = 2)
    entry_name.grid(row = 0, column = 3)
    search_name.grid(row = 0, column = 4)
    label3.grid(row = 0, column = 5)
    label4.grid(row = 1, column = 0)

  def set_menu_bar(self, page):
    """ Sets the menu bar for a page.

    Since tkinter is stupid... we need to set the menu bar for every page we
    want it on. I guess that makes sense... I don't really care at this point.
    
    Args:
      page (Tk): tk page object thing
    """
    menubar = Menu(page)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=self.new_address_book)
    filemenu.add_command(label="Save...", command=self.save)
    filemenu.add_command(label="Save as...", command=self.save_as)
    filemenu.add_command(label="Load", command=self._load)
    filemenu.add_command(label="Quit", command=self.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=self.undo)
    editmenu.add_command(label="Redo", command=self.redo)
    menubar.add_cascade(label="Edit", menu=editmenu)
    page.config(menu=menubar)

  def new_address_book(self):
    """ Lets you create a new address book. """
    fileName = filedialog.asksaveasfilename(filetypes=(("Address Books", "*.addb"), ("All files", "*.*")))

    print fileName

    if fileName == '':
      return
    
    try:
      open(fileName, "r")
      raise FileFoundException("File {} already exists.\n Overwrite?".format(fileName))
    except IOError as e:
      open(fileName, "w")
    except FileFoundException as e:
      if tkMessageBox.askyesno("File Exists", e.args[0]):
        os.remove(fileName)
        open(fileName, "w")
      else:
        self.new_address_book()
        return
    self.set_file(fileName)
    self.load()
    self.list_contacts(self.aBook[self.state])

  def save(self):
    """ Assumes you want to save where ever you loaded from """
    self._save(self.fname, overwrite=True)

  def save_as(self):
    """ Pops up a dialog box asking where you want to save """
    fileName = filedialog.asksaveasfilename(filetypes=(("Address Books",
      "*.addb"), ("All files", "*.*")))
    if fileName == "":
      return
    # Filedialog handles the case where the file already exists. So we can
    # overwrite without worrying. 
    self._save(fileName, overwrite=True)

  def _save(self, fname, overwrite=False):
    """ Actual internal save operation interaction. """
    try:
      FileOps.save_address_book_as(self.aBook[self.state], fname, overwrite)
    except AlreadyExistsException as e:
      if tkMessageBox.askyesno("Already Exists", e.args[0] + "\nWould you like to overwrite?"):
        FileOps.save_address_book_as(self.aBook[self.state], fname,
            overwrite=True)

  def set_file(self, fname):
    """ Sets the filename to fname
    
    Sets the filename to the absolute path. 
    Checks if the file exists.
    Throws an exception if the file doesn't exist.

    Args:
      fname (string): Path to the file
    """
    if fname is not '':
      fname = os.path.abspath(fname)
      if not os.path.exists(fname):
        raise FileNotFoundException("File {} was not found.".format(fname))
    self.fname = fname

  def _load(self):
    """ Pops up dialog to load an addressbook """
    fileName = filedialog.askopenfilename(filetypes=(("Address Books", "*.addb"), ("All files", "*.*")))

    if fileName == "":
      return

    try:
      open(fileName, "r")
    except IOError as e:
      error_msg = "File {} doesn't exist, create it?".format(fileName)
      if tkMessageBox.askyesno("File Missing", error_msg):
        open(fileName, "w")
      else:
        self._load()
        return

    self.set_file(fileName)
    self.load()
    self.list_contacts(self.aBook[self.state])

  def load(self):
    """ Loads the address book located at the currently referenced filename """
    self._increment_state()
    try:
      self.aBook[self.state] = FileOps.open_address_book(self.fname)
    except EmptyAddressBookException as e:
      self.aBook[self.state] = AddressBook(self.fname) 
    except AttributeError as e:
      self.aBook = [None for _ in range(0,19)]
      self.aBook[self.state] = FileOps.open_address_book(self.fname)

  def get_contact_list(self, abook):
    """ Gets the list of contacts """
    retVal = []
    for address in abook.addresses:
      retVal.append((address.first_name,
        address.last_name, address))
    return retVal

  def undo(self):
    if self.undos > 0:
      self._decrement_state()

  def redo(self):
    if self.redos > 0:
      self._increment_state()

  def _increment_state(self):
    try:
      if self.state < 19:
        self.state += 1
      else:
        self.state = 0
    except:
      self.state = 0

    try:
      if self.undos < 20:
        self.undos += 1
    except:
      self.undos = 1

    try:
      if self.redos > 0:
        self.redos -= 1
    except:
      self.redos = 0

  def _decrement_state(self):
    try:
      if self.state == 0:
        self.state = 19
      else:
        self.state -= 1
    except:
      self.state = 0

    try:
      if self.undos > 0:
        self.undos -= 1
    except:
      self.undos = 0

    try:
      if self.redos < 20:
        self.redos += 1
    except:
      self.redos = 1
 
  def quit(self):
    sys.exit(0)

GUI("tests/test_address_book")
