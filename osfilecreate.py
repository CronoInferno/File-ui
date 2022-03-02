import os
import tkinter as tk

window = tk.Tk()
window.title("File creator")
window.geometry("400x300")

Frame = tk.Frame(window, bg="#6d6875")
Frame.place(relx=0.1,rely=0.1,relwidth=0.8, relheight=0.8)


#main Label
Label = tk.Label(
    Frame,
    text="File Creator",
    fg= "#e5989b",
    bg = "#6d6875",
    font="Couriernew"
    )
Label.place(
    relx= 0.005,
    rely=0.015,
    relheight=0.1,
    relwidth=0.4
    )


#file name label
Filenamelabel = tk.Label(Frame, text="File name", font= "Couriernew", bg ="#6d6875").place(relx=0.05, rely= 0.65)


#File name entry
filenamevar = tk.StringVar()

Filenameentry = tk.Entry(
    Frame,
    textvariable=filenamevar
    )

Filenameentry.place(
    relx=0.05,
    rely=0.85,
    relheight=0.08,
    relwidth=0.4
    )


#File extension label
fileextensionlabel = tk.Label(
    Frame,
    text="File extension",
    font= "Couriernew",
    bg ="#6d6875").place(relx=0.05,
    rely= 0.25
    )


#file extension entry
fileextensionvar = tk.StringVar()

fileextensionentry = tk.Entry(
    Frame,
    textvariable=fileextensionvar
    )

fileextensionentry.place(
    relx=0.05,
    rely=0.45,
    relheight=0.08,
    relwidth=0.4
    )

#Path Entry ~46 - 59
pathentryvar = tk.StringVar()

pathentry = tk.Entry(
    Frame,
    textvariable=pathentryvar
    )

pathentry.place(
    relx= 0.55,
    rely=0.45,
    relheight=0.08,
    relwidth=0.4
    )

filepathlabel = tk.Label(
    Frame,
    text="File path",
    font= "Couriernew",
    bg ="#6d6875").place(relx=0.55,
    rely= 0.25
    )

def filecreate():
    filename = str(filenamevar.get())
    fileextension = str(fileextensionvar.get())
    directory = str(pathentryvar.get())
    os.chdir(directory)
    with open(f'{filename}.{fileextension}', 'w') as fp:
        pass

filecreatebutton = tk.Button(
    Frame,
    text= "File Create",
    command=filecreate,
    bg="#b5838d"
    )
filecreatebutton.place(
    relx=0.55,
    rely=0.75,
    relheight=0.2,
    relwidth=0.4
    )



window.mainloop()