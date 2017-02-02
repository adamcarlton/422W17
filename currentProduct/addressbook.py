from address import Address
from address import TypeException

class AddressBook(object):
  """ A basic address book object. """
  def __init__(self, fileName, addresses = []):
    """ Basic initialization class.

    Args:
      fileName (str): name and hopefully path of the file.
      addresses (list): List of addresses
    """
    self.fileName = fileName
    self.addresses = []
    for address in addresses:
      self.add_address(address)

  def to_dict(self):
    addresses = [x.to_dict() for x in self.addresses]
    retVal = [ {"address": address} for address in addresses]
    return retVal

  def is_empty(self):
    return len(self.addresses) == 0

  def in_range(self, num):
      if not isinstance(num, int):
          raise TypeException("num is not of type int, got type {}".format(type(num)))
      return 1 <= num <= len(self.addresses)

  def add_address(self, address):
    """ Adds an address to the address book.

    Verifies that the address is actually of the Address object type. Will
    throw an exception if it isn't.

    Args:
      address (Address): The Address object we want to append.
    """
    if not isinstance(address, Address):
      raise TypeException("address is not of type Address, got type {}".format(type(address)))
    self.addresses.append(address)

  def delete_address(self, address):
    """ Deletes an address from the address book.

    Verifies that the address is actually of the Address object type. Will
    throw an exception if it isn't. If the address to be deleted is not 
    actually in the address book - will ignore the delete operation.

    Args:
      address (Address): the Address object we want to delete.
    """
    if not isinstance(address, Address):
      raise TypeException("address is not of type Address, got type {}".format(type(address)))
    try:
        self.addresses.remove(address)
    except ValueError as e:
        pass
