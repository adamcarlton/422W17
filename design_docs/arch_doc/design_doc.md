\[Overview\] Our goal is to create an Address Book meeting the
requirements of the product specifications provided by Prof. Faulk. We
will do this in three main phases:

-   Minimum Viable Product (MVP)\
    This will be the phase where we implement a minimial product that
    can perform the basic CRUD operations of an address book.

-   GUI Implementation\
    This will be the phase where we develop the GUI and link it to
    our MVP.

-   Feature implementation\
    This is the phase where we implement all features that are not
    CRUD related.

As a group we discussed what tools and software we’ll be utilizing. To
this end we have agreed upon the following:

-   Programming Language\
    Our main language will be Python 2.7.12. Python 2.7.12 was chosen
    due to the experience with the language on the team.

-   GUI Framework\
    The Tkinter package was chosen for our GUI framework. It was chosen
    due to its ease of use and alteration. We’ll be iterating quickly
    and need a framework that supports efficient and rapid development.

-   Save Format\
    Our initial inclination for a save format was a mysql or mongo
    database. It was decided that a database requires too much overhead
    for such a simple application. We’ve decided to utilize the YAML
    file format in order to simplify the process of loading and saving.
    YAML corresponds directly with Python dictionary objects, and the
    PyYAML library makes loading, munging, and saving these objects easy
    and simple.

-   Class Design Specifications\
    Most class specifications will be done in UML. UML is ubiquitous and
    readily understood by all members of the team.

\[Minimum Viable Product (MVP)\] The minimum viable product will be an
command line address book that can perform the basic Create, Read,
Update, Delete (CRUD) commands for an address book. This first step will
provide us with a solid platform to link a GUI to in the future.\
Objects:

-   Address\
    This is the most basic object. Will contain all of the ’standard’
    address parameters, and functions for interacting with them.

    ![image](AddressUML){width="\textwidth"}

-   AddressBook\
    This is the book itself, it will handle updates to the book.

    ![image](AddressBookUML){width="\textwidth"}

-   FileOps\
    This will be a static class that has the methods for interaction
    with the file system, producing address books from disk, and saving
    them to file using the YAML format.

    ![image](FileOPSUML){width="\textwidth"}

-   basicCLI\
    This will be our base for interaction with an AddressBook.

    Important design considerations:

    -   Undo/Redo functionality\
        Undo and redo are important functions. We considered
        implementing either the [Memento
        Pattern](https://en.wikipedia.org/wiki/Memento_pattern) or the
        [Command Pattern](https://en.wikipedia.org/wiki/Command_pattern)
        but both were deemed too heavy handed for such a simple
        application.\
        We’ve decided to go with a simple stateful approach, there will
        be a list called aBook, which will hold AddressBook objects.
        With every Create, Update, or Delete operation the AddressBook
        will be copied to the new state, and the new state will recieve
        the operation. The trade-off for the easier implementation is
        that this is memory intensive, and will reduce the number of
        undo and redo operations that we can perform.

    -   Interface Layer\
        The basicCLI should be entirely an interface layer with our
        three basic objects: Address, AddressBook, and FileOps. This
        will prove that we’ve created and designed a solid
        implementation, and ensure that our transition to a GUI
        interface will be simple and easy. To that end it is important
        that this implementation only ever interface with the underlying
        objects, rather than expanding or changing them. In example:
        Adding or deleting should utilize the add and delete functions
        provided by AddressBook. If the update function was being
        implemented here it would create a new Address object and
        replace the old one by deleting it and adding the new one.

    Our basicCLI will support the following use cases:

    -   Create\
        The ability to instantiate a new Address and place in the
        current AddressBook. The create() function will need to copy the
        current state to a new state, increment the current state to the
        new state, and then add the new address to the current
        state’s AddressBook.

    -   Retrieve\
        The ability to print to console an address from the
        current AddressBook. Will also return the Address object for
        updating and deleting. The retrieve() function will need to
        allow the user to select which contact they want from the list.

    -   Update\
        The ability to alter the attributes of an Address. As the update
        function will look considerably different from the GUI
        implementation, it will not need to be implemented for
        the basicCLI.

    -   Delete\
        The ability to remove an Address object from the current
        AddressBook. Will utilize the retrieve() function to get the
        specific address object that will need be removed from
        the AddressBook. Like the create() function, will need to copy
        the current state to a new state, increment the current state to
        the new state, and then remove the address from the current
        state AddressBook.

    -   Save\
        The ability to save to file the current AddressBook. Should just
        pass the current state’s AddressBook to the FileOps
        save\_address\_book() function.

    -   Save As\
        The ability to save to file the current AddressBook as a
        different filename. Should request a filename from the user, and
        pass the filename and current state’s AddressBook to the
        FileOps save\_address\_book\_as() function.

    -   Undo\
        The ability to undo any of the create(), update(), or
        delete() actions. Should move the current state to the previous
        state, simply by decrementing the state and the undo count and
        incrementing the redo count. If we are at the earliest
        state, i.e. undo count is at zero - do nothing.

    -   Redo\
        The ability to redo any undo action. Should move the current
        state to the next state, simply by incrementing the state and
        undo count, and decrementing the redo count. If we are at the
        latest state, i.e. redo count is at zero - do nothing.

    ![image](basicCLIUML){width="\textwidth"}

\[Graphical User Interface implementation\] The graphical user interface
(GUI) will rely heavily on feedback from the customer. It is within this
phase that we’ll be able to present the customer with something they can
interact with. Initially the GUI will support the same feature set as
the basicCLI
