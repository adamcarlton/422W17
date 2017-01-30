from Tkinter import *
import edit_UI


def Info(TheName):
    info = Tk()
    info.title("address book Contact")
    info.geometry('250x200')
    name = TheName

    frame1 = Frame(info)
    frame1.pack()
    label1 = Label(frame1, text = TheName, font = 'Helvetica -18 bold')
        
    label1.grid(row = 0, column = 0)


    frame2 = Frame(info)
    frame2.pack(fill = BOTH, expand = YES)
    PhoneLabel = Label(frame2, text = "Phone: ", font = 'Helvetica -14')
    AddressLabel = Label(frame2, text = "Address: ", font = 'Helvetica -14')
    CityLabel = Label(frame2, text = "City: ", font = 'Helvetica -14')
    StateLabel = Label(frame2, text = "State: ", font = 'Helvetica -14')
    ZipLabel = Label(frame2, text = "Zip: ", font = 'Helvetica -14')

    PhoneLabel.grid(row = 0, column = 0)
    AddressLabel.grid(row = 1, column = 0)
    CityLabel.grid(row = 2, column = 0)
    StateLabel.grid(row = 3, column = 0)
    ZipLabel.grid(row = 4, column = 0)

    frame3 = Frame(info)
    frame3.pack(side = BOTTOM, fill = X)

    button1 = Button(frame3, text=" edit ", command = EditContacts)
    button2 = Button(frame3, text="delete")
    button1.pack(side = LEFT, fill = X, expand = YES)
    button2.pack(side = RIGHT, fill = X, expand = YES)

    info.mainloop()

def EditContacts():
    edit_UI.Edit()

