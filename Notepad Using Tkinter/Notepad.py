from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# def for File Menu
def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    text_area.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

    if file == "":
        file = None

    else:
        root.title(os.path.basename(file) + "- Notepad")
        text_area.delete(1.0, END)
        f = open(file, "r")
        text_area.insert(1.0, f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files","*.*"),("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            # Saving a new file
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + "- Notepad")

    else:
        # Saving the current file
        f = open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()


# def for Edit Menu
def cut():
    text_area.event_generate(("<<Cut>>"))

def copy():
    text_area.event_generate(("<<Copy>>"))

def paste():
    text_area.event_generate(("<<Paste>>"))



# def for Help Menu
def about():
    tmsg.showinfo("About Notepad", "This Notepad is developed by Shubham Kashyap")


if __name__ == '__main__':
    root = Tk()
    root.title("New Text Document - Notepad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("600x400")

    # Text Area in Notepad
    text_area = Text(root, font="lucida 15")
    file = None
    text_area.pack(expand=True, fill=BOTH)

    # Creating Menu Bar
    menu_bar = Menu(root)

    # Creating File Menu
    file_menu = Menu(menu_bar, tearoff=0)
    # Adding New file
    file_menu.add_command(label="New", command=newfile)
    # To Open file
    file_menu.add_command(label="Open...", command=openfile)
    # To save the file
    file_menu.add_command(label="Save", command=savefile)
    file_menu.add_separator()
    # To exit command
    file_menu.add_command(label="Exit", command=quit)
    root.config(menu=menu_bar)
    menu_bar.add_cascade(label="File", menu=file_menu)



    # Creating Edit Menu
    edit_menu = Menu(menu_bar, tearoff=0)
    # Cut
    edit_menu.add_command(label="Cut", command=cut)
    # Copy
    edit_menu.add_command(label="Copy", command=copy)
    # Paste
    edit_menu.add_command(label="Paste", command=paste)
    # edit_menu.add_separator()
    root.config(menu=menu_bar)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)


    # Creating Help Menu
    help_menu = Menu(menu_bar, tearoff=0)
    # help_menu.add_command(label="View help", commnad=viewhelp)
    help_menu.add_command(label="About Notepad", command=about)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    root.config(menu=menu_bar)

    # Adding Scrollbar
    scrollbar = Scrollbar(text_area)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=text_area.yview)
    text_area.config(yscrollcommand=scrollbar.set)



    root.mainloop()

