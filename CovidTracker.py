# Basic Imports
from covid import Covid
from tkinter import *

# Defining Tkinter
root = Tk()
root.geometry('800x800')
root.title = "COVID Tracker"
root.resizable(0,0)

covid = Covid()

nation = StringVar()

# Input Country Name
lbl = Label(root, text = "Enter Country Name :")
lbl.pack(side = LEFT)

# path Input
ent = Entry(root, bd = 5, textvariable = nation)
ent.pack(side = RIGHT)
ent.focus()

# tracker function
def tracker(nat= ent.get()):

    separate = f"#############{ent.get()}###############"

     # Country Name
    coun = f"Showing details of {ent.get()}"
    lbl = Label(root, text = coun)
    lbl.pack()

    try:
        data = covid.get_status_by_country_name(ent.get())

        # Separator
        lbl = Label(root, text = separate)
        lbl.pack()

        for key in data:
            note = f"{key} : {data[key]}"
            lbl = Label(root, text = note )
            lbl.pack()

        # End Separator
        lbl = Label(root, text = "###########################################################\n \n \n")
        lbl.pack()


    except ValueError:
        
        lbl = Label(root, text = "Country not found, please check your input!")
        lbl.pack()

# Track button
Find = Button(root , text = "Track!", command = tracker)
Find.pack()

root.mainloop()
