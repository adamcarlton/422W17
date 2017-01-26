from tkinter import *


def add_contact(Thename):
    AddNew = Tk()
    AddNew.title("address book New Contact Page")
    AddNew.geometry('300x200') 

    # frame1 just show the name of the contact
    frame1 = Frame(AddNew)
    frame1.pack()
    label1 = Label(frame1, text = Thename, font = 'Helvetica -18 bold') 
    label1.grid(row = 0, column = 0)

    # the frame2 include the main information
    frame2 = Frame(AddNew)
    frame2.pack(fill = BOTH, expand = YES)

    # setting the label for phone, address, city, state and zip
    NameLabel = Label(frame2, text = "Name: ", font = 'Helvetica -14')
    PhoneLabel = Label(frame2, text = "Phone: ", font = 'Helvetica -14')
    AddressLabel = Label(frame2, text = "Address: ", font = 'Helvetica -14')
    CityLabel = Label(frame2, text = "City: ", font = 'Helvetica -14')
    StateLabel = Label(frame2, text = "State: ", font = 'Helvetica -14')
    ZipLabel = Label(frame2, text = "Zip: ", font = 'Helvetica -14')


    # setting the entry element
    contactname = StringVar()
    phoneNumber = IntVar()
    address = StringVar()
    city = StringVar()
    state = StringVar()
    zipcode = IntVar()

    # setting the elements default value
    contactname.set('John')
    phoneNumber.set('5412212860')
    address.set('University Road')
    city.set('Eugene')
    state.set('OR')
    zipcode.set('97405')

    # setting the entry of GUI
    NameEntry = Entry(frame2, textvariable = contactname)
    PhoneEntry = Entry(frame2, textvariable = phoneNumber)
    AddressEntry = Entry(frame2, textvariable = address)
    CityEntry = Entry(frame2, textvariable = city)
    StateEntry = Entry(frame2, textvariable = state)
    ZipEntry = Entry(frame2, textvariable = zipcode)

    #grid the above labels
    NameLabel.grid(row = 0, column = 0)
    PhoneLabel.grid(row = 1, column = 0)
    AddressLabel.grid(row = 2, column = 0)
    CityLabel.grid(row = 3, column = 0)
    StateLabel.grid(row = 4, column = 0)
    ZipLabel.grid(row = 5, column = 0)

    #grid the above rentries
    NameEntry.grid(row = 0, column = 1)
    PhoneEntry.grid(row = 1, column = 1)
    AddressEntry.grid(row = 2, column = 1)
    CityEntry.grid(row = 3, column = 1)
    StateEntry.grid(row = 4, column = 1)
    ZipEntry.grid(row = 5, column = 1)
        

    frame3 = Frame(AddNew)
    frame3.pack(side = BOTTOM, fill = X)

    button1 = Button(frame3, text=" save ")
    button2 = Button(frame3, text="cancel")
    button1.pack(side = LEFT, fill = X, expand = YES)
    button2.pack(side = RIGHT, fill = X, expand = YES)

    AddNew.mainloop()



