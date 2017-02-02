class TypeException(Exception):
  pass

class Address(object):
  """ Address is a class that holds an entire 'Americanized' address """
  def __init__(self, last_name, first_name, house_number, street, city, state, zipcode):
    """ Basic initialization class of the Address object.

    Utilizes the update functions to do the actual initialization.

    Args:
      last_name (str): Last name of the person.
      first_name (str): First name of the person.
      house_number (int): House number of the person.
      street (str): Street the person lives on.
      city (str): city the person lives in
      state (str): state the person lives in
      zipcode (int): zipcode the person lives in
    """
    self.update_first_name(first_name)
    self.update_last_name(last_name)
    self.update_house_number(house_number)
    self.update_street(street)
    self.update_city(city)
    self.update_state(state)
    self.update_zipcode(zipcode)

  def __str__(self):
    """ Returns a str representing an Americanized Address 
    
    Return:
      str: The americanized address
    """
    return "{fn} {ln}\n{hn} {street}, {city}, {state} {zipcode}".format(fn=self.first_name,
                                                                        ln=self.last_name,
                                                                        hn=self.house_number,
                                                                        city=self.city,
                                                                        street=self.street,
                                                                        state=self.state,
                                                                        zipcode=self.zipcode
                                                                        )

  def to_dict(self):
    retVal = {"first_name": self.first_name,
              "last_name": self.last_name,
              "house_number": self.house_number,
              "street": self.street,
              "city": self.city,
              "state": self.state,
              "zipcode": self.zipcode
              }
    return retVal

  def update_first_name(self, name):
    """ Updates the first name. 

    If the name is not of type str - will throw an exception.

    Args:
      name (str): first name of the person
    """
    if not isinstance(name, str):
      raise TypeException("Name was not of type str, got type {}".format(type(name)))
    self.first_name = name

  def update_last_name(self, name):
    """ Updates the last name. 

    If the name is not of type str - will throw an exception.

    Args:
      name (str): last name of the person
    """
    if not isinstance(name, str):
      raise TypeException("Name was not of type str, got type {}".format(type(name)))
    self.last_name = name

  def update_house_number(self, house_number):
    """ Updates the house number. 

    If the name is not of type int - will throw an exception.

    Args:
      house_number (int): the house number
    """
    if not isinstance(house_number, int):
      raise TypeException("house_number was not of type int, got type {}".format(type(house_number)))
    self.house_number = house_number

  def update_street(self, street):
    """ Updates the street. 

    If the street is not of type str - will throw an exception.

    Args:
      street (str): street of the person
    """
    if not isinstance(street, str):
      raise TypeException("street was not of type str, got type {}".format(type(street)))
    self.street = street

  def update_city(self, city):
    """ Updates the city. 

    If the city is not of type str - will throw an exception.

    Args:
      city (str): city of the person
    """
    if not isinstance(city, str):
      raise TypeException("city was not of type str, got type {}".format(type(city)))
    self.city = city

  def update_state(self, state):
    """ Updates the state. 

    If the state is not of type str - will throw an exception.

    Args:
      state (str): state of the person
    """
    if not isinstance(state, str):
      raise TypeException("state was not of type str, got type {}".format(type(state)))
    self.state = state

  def update_zipcode(self, zipcode):
    """ Updates the zipcode. 

    If the zipcode is not of type int - will throw an exception.

    Args:
      zipcode (int): zipcode of the person
    """
    if not isinstance(zipcode, str):
      raise TypeException("zipcode was not of type str, got type {}".format(type(zipcode)))
    self.zipcode = zipcode

