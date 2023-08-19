from tkinter import *
from tkinter import ttk
import csv
from tkinter import filedialog



root = Tk()
root.title("Enter Application Title Here.")

def writeToFile():
        directory = filedialog.asksaveasfilename(defaultextension="csv", filetypes=[("Comma Separated File", "csv")])
        with open(directory, 'w') as f:
            w=csv.writer(f, quoting=csv.QUOTE_ALL)
            w.writerow(["one","two","three"])
            w.writerow(["1","2","3"])

def openNewWindow(*args):
    sequence=seq.get() 
    lt = lowThresh.get()
    ht = highThresh.get()
    print(sequence, lt, ht)
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text =sequence).pack()
    Label(newWindow,
          text =lt).pack()
    Label(newWindow,
          text =ht).pack()
    ttk.Button(newWindow, text="Download", command=writeToFile).pack()
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

seq = StringVar()
seq_entry = ttk.Entry(mainframe, width=7, textvariable=seq)
seq_entry.grid(column=3, row=1, sticky=(W, E))

lowThresh = IntVar(value=30)
lowThresh_entry = ttk.Entry(mainframe, width=7, textvariable=lowThresh)
lowThresh_entry.grid(column=3, row=2, sticky=(W, E))

highThresh = IntVar(value=70)
highThresh_entry = ttk.Entry(mainframe, width=7, textvariable=highThresh)
highThresh_entry.grid(column=3, row=3, sticky=(W, E))


#meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Submit", command=openNewWindow).grid(column=3, row=4, sticky=W)

# ttk.Button(mainframe, text="Download", command=writeToFile).grid(column=1, row=4, sticky=W)

ttk.Label(mainframe, text="Input sequence").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Low threshold").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="High threshold").grid(column=1, row=3, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

seq_entry.focus()
root.bind("<Return>", openNewWindow)

root.mainloop()