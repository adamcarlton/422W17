from Tkinter import *
import AddContact_UI
import ContactInfo_UI

class Main_Page:
    def __init__(self):
        MainPage = Tk()
        MainPage.title("address book")
        #MainPage.geometry('200x100')

        
        menubar = Menu(MainPage)
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "Import")
        filemenu.add_command(label = "Export")
        menubar.add_cascade(label = "File", menu = filemenu)
 
        MainPage.config(menu = menubar)

        # frame1 show the word "Contacts" and search button
        frame1 = Frame(MainPage, bg = 'white')
        frame1.pack(side = TOP, fill = X, expand = YES)
        label1 = Label(frame1, text = "Contacts", bg = 'white', fg = 'blue', font = 'Helvetica -18 bold')
        label2 = Label(frame1,text = "          ", bg = 'white')
        self.name = StringVar()
        entryName = Entry(frame1, textvariable = self.name, bg = 'white')
        SearchName = Button(frame1, text = "Search", bg = 'white')
        label3 = Label(frame1,text = "", bg = 'white')
        label4 = Label(frame1,text = "  ", bg = 'white')

        # grid the word "Contacts" and search button
        label1.grid(row = 0, column = 0)
        label2.grid(row = 0, column = 2)
        entryName.grid(row = 0, column = 3)
        SearchName.grid(row = 0, column = 4)
        label3.grid(row = 0, column = 5)
        label4.grid(row = 1, column = 0)

                          
        li = ['John','Peter','Trump','Wilson','Henry','Mary','Jiana','Police','Alex','Jack','Obama', 'Washinton','Sal','Gaga']

        # Setting the listbox of contacts and add a scrollbar
        frame2 = Frame(MainPage)
        frame2.pack(fill = BOTH, expand = YES)
        scrollbar = Scrollbar(frame2)
        scrollbar.pack(side = RIGHT, fill = Y)
    
        LB = Listbox(frame2, yscrollcommand=scrollbar.set)

        def ClickName(event):
            click_name = LB.get(LB.curselection())
            print(click_name)
            ContactInfo_UI.Info(click_name)

        # funciton of click the name of contact in the listbox
        LB.bind('<ButtonRelease-1>', ClickName)
        for item in li:
            LB.insert(END, item)

        # Grid the listbox of contacts and add a scrollbar
        LB.config(yscrollcommand = scrollbar.set)
        LB.pack(fill = BOTH, expand = YES)
        scrollbar.config(command = LB.yview)

        # Setting the button of "Add new contact"
        frame3 = Frame(MainPage)
        frame3.pack(side = BOTTOM, fill = X)
        button = Button(frame3, text="Add new contact", command = Main_Page.AddNewContacts)
        button.pack(fill = X)
        
        MainPage.mainloop()

    def AddNewContacts():
        name = ''
        AddContact_UI.add_contact(name)



Main_Page()
  


