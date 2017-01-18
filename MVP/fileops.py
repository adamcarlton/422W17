from address import Address
from addressBook import AddressBook
import os
import yaml

class AlreadyExistsException(Exception):
  pass

class EmptyAddressBookException(Exception):
  pass

class FileOps(object):
  """ Simple file operations converting from YAML to address objects, and from 
  address objects to YAML files.
  """
  @staticmethod
  def open_address_book(fileName):
    """ Opens an address book from file.

    Args:
      fileName (str): path to the filename.
    """
    fName = os.path.abspath(fileName)
    retVal = AddressBook(fName)
    with open(fName, "r") as stream:
      aBook = yaml.load(stream)
    if aBook is None:
      raise EmptyAddressBookException("Addressbook located at {} is empty.".format(fName))
    for address in aBook:
      values = address["address"]
      curAdd = Address(values["last_name"], values["first_name"], values["house_number"],
                       values["street"], values["city"], values["state"], values["zipcode"])
      retVal.add_address(curAdd)
    return retVal

  @staticmethod
  def save_address_book(addressBook):
    """ Saves the address book to wherever it was got from. 

    Args:
      addressBook (AddressBook): The addressbook to be saved.
    """
    fName = addressBook.fileName
    with open(fName, "w") as addbook:
      yaml.dump(addressBook.to_dict(), addbook, default_flow_style=False)

  @staticmethod
  def save_address_book_as(addressBook, fName):
    """ Saves the addressbook to a new location.

    Args:
      addressBook (AddressBook): The Address Book to be saved.
      fName (string): The location of the address book.
    """
    if os.path.exists(fName):
      raise AlreadyExistsException("The file, {}, already exists".format(fName))
    with open(fName, "w") as addbook:
      yaml.dump(addressBook.to_dict(), addbook, default_flow_style=False)

