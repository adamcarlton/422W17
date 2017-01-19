import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import fileops

class TestConfig(unittest.TestCase):
  test_against = [{'address': {'city': 'Literally-The-Worst', 'first_name': 'George', 'last_name': 'Lucas', 'street': 'Terrible Director Ln.', 'state': 'OR', 'house_number': 123, 'zipcode': '97229'}}, {'address': {'city': 'Alpha', 'first_name': 'Gene', 'last_name': 'Roddenberry', 'street': 'Enterprise', 'state': 'OR', 'house_number': 1701, 'zipcode': '97229'}}]

  def test_load(self):
    aBook = fileops.FileOps.open_address_book("test_address_book")
    self.assertEqual(aBook.to_dict(), self.test_against)

  def test_save(self):
    aBook = fileops.FileOps.open_address_book("test_address_book")
    fileops.FileOps.save_address_book_as(aBook, "test_save")
    newBook = fileops.FileOps.open_address_book("test_save")
    self.assertEqual(aBook.to_dict(), newBook.to_dict())
    os.remove("test_save")

if __name__ == '__main__':
  unittest.main()
