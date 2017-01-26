from tkinter import *


def Edit():
    edit = Tk()
    edit.title("address book Edit Page")
    edit.geometry('300x200') 

    # frame1 show the name of the contact
    frame1 = Frame(edit)
    frame1.pack()
    label1 = Label(frame1, text = '', font = 'Helvetica -18 bold')   
    label1.grid(row = 0, column = 0)

    # the frame2 include the main information
    frame2 = Frame(edit)
    frame2.pack(fill = BOTH, expand = YES)

    # these are the label for phone, address, city, state and zip
    PhoneLabel = Label(frame2, text = "Phone: ", font = 'Helvetica -14')
    AddressLabel = Label(frame2, text = "Address: ", font = 'Helvetica -14')
    CityLabel = Label(frame2, text = "City: ", font = 'Helvetica -14')
    StateLabel = Label(frame2, text = "State: ", font = 'Helvetica -14')
    ZipLabel = Label(frame2, text = "Zip: ", font = 'Helvetica -14')

    # setting the entry element
    phoneNumber = IntVar()
    address = StringVar()
    city = StringVar()
    state = StringVar()
    zipcode = IntVar()

    # setting the elements default value
    phoneNumber.set('5412212860')
    address.set('University Road')
    city.set('Eugene')
    state.set('OR')
    zipcode.set('97405')

    # setting the entry of GUI
    PhoneEntry = Entry(frame2, textvariable = phoneNumber)
    AddressEntry = Entry(frame2, textvariable = address)
    CityEntry = Entry(frame2, textvariable = city)
    StateEntry = Entry(frame2, textvariable = state)
    ZipEntry = Entry(frame2, textvariable = zipcode)

    #grid the above labels
    PhoneLabel.grid(row = 0, column = 0)
    AddressLabel.grid(row = 1, column = 0)
    CityLabel.grid(row = 2, column = 0)
    StateLabel.grid(row = 3, column = 0)
    ZipLabel.grid(row = 4, column = 0)

    #grid the above rentries
    PhoneEntry.grid(row = 0, column = 1)
    AddressEntry.grid(row = 1, column = 1)
    CityEntry.grid(row = 2, column = 1)
    StateEntry.grid(row = 3, column = 1)
    ZipEntry.grid(row = 4, column = 1)

    # frame3 include 2 button, save and cancel
    frame3 = Frame(edit)
    frame3.pack(side = BOTTOM, fill = X)

    button1 = Button(frame3, text=" save ")
    button2 = Button(frame3, text="cancel", command = edit.destroy)
    button1.pack(side = LEFT, fill = X, expand = YES)
    button2.pack(side = RIGHT, fill = X, expand = YES)
    edit.mainloop()


