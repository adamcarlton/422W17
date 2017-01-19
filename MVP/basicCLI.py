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
    self.aBook = FileOps.open_address_book(self.fname)

  def displayAddressBook(self):
    print "You have the following contacts in your address book:"
    counter = 1
    for address in self.aBook.addresses:
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


  def create(self):
    pass

  def retrieve(self):
    pass

  def update(self):
    pass

  def delete(self):
    pass

  def quit(self):
    sys.exit(1)


    
if __name__ == "__main__":
  args = arg_parser()
  CLI(args.fname)
    


