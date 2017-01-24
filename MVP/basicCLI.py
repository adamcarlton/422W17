""" Basic command line interface for address book MVP. """
from address import Address
from addressbook import AddressBook
from fileops import FileOps
import argparse
import os
import sys

def arg_parser():
  """
  Argument Parser

  Returns:
    argparse.Namespace: object that holds attributes with the values of the 
      arguments added.
  """
  parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  parser.add_argument('-f', '--filename', dest='fname', default='')

  return parser.parse_args()

class FileNotFoundException(Exception):
  pass

class CLI(object):
  def __init__(self, fname):
    self.set_file(fname)
    if self.fname == '':
      self.request_filename()
    self.load()
    self.main()
  
  def main(self):
    while True:
      self.displayAddressBook()
      action = self.request_action()
      action()

  def set_file(self, fname):
    if fname is not '':
      fname = os.path.abspath(fname)
      if not os.path.exists(fname):
        raise FileNotFoundException("File {} was not found.".format(fname))
    self.fname = fname

  def request_filename(self):
    fname = raw_input("Filename was not provided. Please provide a filename: ")
    try:
      self.set_file(fname)
    except FileNotFoundException:
      print "File was not found. Please check the path and try again."
      self.request_filename()

  def load(self):
    self._increment_state()
    try:
        self.aBook[self.state] = FileOps.open_address_book(self.fname)
    except:
        self.aBook = [None for _ in range(0,19)]
        self.aBook[self.state] = FileOps.open_address_book(self.fname)

  def displayAddressBook(self):
    print "You have the following contacts in your address book:"
    counter = 1
    for address in self.aBook[self.state].addresses:
      print "{}.".format(counter), address.first_name, address.last_name
      counter += 1

  def request_action(self):
    action_dict = {"c": self.create,
                   "r": self.retrieve,
                   "u": self.update,
                   "d": self.delete,
                   "q": self.quit
                   }
    print "What would you like to do?"
    print "(C)reate a new address."
    print "(R)etrieve an address."
    print "(U)pdate an existing one."
    print "(D)elete an address."
    print "(Q)uit"
    act = raw_input("")
    return action_dict.get(act[0].lower(), self.main)

  @staticmethod
  def convert_input(in_str):
    try:
      retVal = int(in_str)
    except ValueError:
      retVal = in_str
    return retVal 


  def create(self):
    self._increment_state()
    addy = self.create_address()
    self.aBook[self.state].add_address(addy)
      

  def retrieve(self, action = "retrieve"):
    action_dict = {"l": self.displayAddressBook}
    retVal = None

    if self.aBook[self.state].is_empty():
      print "Address is currently empty. Unable to retrieve any addresses"
      return retVal

    print "Which address would you like to {}?".format(action)
    print "Please use the provided number on the address line."
    print "You may also (L)ist the current address book."
    act = self.convert_input(raw_input(""))

    if isinstance(act, int):
      if self.aBook[self.state].in_range(act):
        retVal = self.aBook[self.state].addresses[act - 1]
        print retVal
      elif self.aBook[self.state].is_empty():
        print "Address book is empty"
      else:
        print "Please use a number between 1 and {}".format(len(self.aBook[self.state].addresses))
        retVal = self.retrieve()
    elif action_dict.get(act[0].lower(), None):
      action_dict.get(act[0].lower())()
      retVal = self.retrieve()
    else:
      print "Not a valid selection"
      retVal = self.retrieve()
    return retVal

  def update(self):
    pass
    
  def delete(self):
    addy = self.retrieve("delete")
    previous_addy_book = self.aBook[self.state]
    self._increment_state()
    self.aBook[self.state] = previous_addy_book
    self.aBook[self.state].delete_address(addy)

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
    sys.exit(1)


    
if __name__ == "__main__":
  args = arg_parser()
  CLI(args.fname)
    


