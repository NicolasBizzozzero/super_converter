from tkinter import Tk, Frame, LabelFrame, Entry, Radiobutton, TOP, LEFT, \
    RIGHT, CENTER, StringVar, IntVar, W, Button, Label, Menu, messagebox
from lib.convertion_functions import convert
from sys import argv


def callback_convert() -> None:
    """ Wrap the convert function with its proper arguments. """
    global string_to_convert
    global string_converted
    global src_base
    global dest_base

    new_value = convert(string_to_convert.get(),
                        src_base.get(), dest_base.get())
    string_converted.set(new_value)


def callback_bind_enter(event) -> None:
    callback_convert()


def callback_about():
    messagebox.showinfo("About", "Super Converter Version 0.1")


def donothing():
    pass


def initialisation_of_the_menu(root: Tk) -> None:
    menubar = Menu(root)
    # File menu
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Close", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # Edit menu
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)
    menubar.add_cascade(label="Edit", menu=editmenu)

    # Language Menu
    language_menu = Menu(menubar, tearoff=0)
    language_menu.add_radiobutton()
    menubar.add_cascade(label="Language", menu=language_menu)

    # About menu
    about_menu = Menu(menubar, tearoff=0)
    about_menu.add_command(label="Help Index", command=donothing)
    about_menu.add_command(label="About", command=callback_about)
    menubar.add_cascade(label="Help", menu=about_menu)

    root.config(menu=menubar)


def initialisation_of_the_window() -> Tk:
    """ Return the properly initialized root of the windows. """
    global string_to_convert
    global string_converted
    global src_base
    global dest_base

    # Creation of the root
    root = Tk()
    path = argv[0][:-18] + r"res/icon.ico"
    root.iconbitmap(path)
    root.bind('<Return>', callback_bind_enter)

    # Initialisation of the menu
    initialisation_of_the_menu(root)

    # Creation of the main frame
    f_main = Frame(root)
    f_main.pack(fill="both", expand="yes", side=TOP)

    # Creation of the left labeled frame
    f_lf_left = Frame(f_main, bd=6)
    f_lf_left.pack(fill="both", expand="yes", side=LEFT)
    lf_left = LabelFrame(f_lf_left, text="  Input  ")
    lf_left.pack(fill="both", expand="yes")

    # Creation of the right labeled frame
    f_lf_right = Frame(f_main, bd=6)
    f_lf_right.pack(fill="both", expand="yes", side=RIGHT)
    lf_right = LabelFrame(f_lf_right, text="  Output  ")
    lf_right.pack(fill="both", expand="yes")

    # Creation of the entry
    f_entry = Frame(lf_left, bd=6)
    f_entry.pack()
    string_to_convert = StringVar()
    entry_to_convert = Entry(f_entry, textvariable=string_to_convert)
    entry_to_convert.focus_set()
    entry_to_convert.pack()

    # Creation of the choice of the bases
    f_bases = Frame(lf_left, bd=0)
    f_bases.pack(fill="x", expand="yes")
    # Source base
    f_left_base = LabelFrame(f_bases, bd=2, text="  From  ", labelanchor="n")
    f_left_base.pack(fill="y", expand="yes", side=LEFT)
    src_base = IntVar()
    rb1_src_base = Radiobutton(
        f_left_base, text="Binary", variable=src_base, value=2)
    rb1_src_base.pack(anchor=W)
    rb2_src_base = Radiobutton(
        f_left_base, text="Decimal", variable=src_base, value=10)
    rb2_src_base.pack(anchor=W)
    rb3_src_base = Radiobutton(
        f_left_base, text="Hexadecimal", variable=src_base, value=16)
    rb3_src_base.pack(anchor=W)
    src_base.set(10)    # Default value
    # Destination base
    f_right_base = LabelFrame(f_bases, bd=2, text="  To  ", labelanchor="n")
    f_right_base.pack(fill="y", expand="yes", side=RIGHT)
    dest_base = IntVar()
    rb1_dest_base = Radiobutton(
        f_right_base, text="Binary", variable=dest_base, value=2)
    rb1_dest_base.pack(anchor=W)
    rb2_dest_base = Radiobutton(
        f_right_base, text="Decimal", variable=dest_base, value=10)
    rb2_dest_base.pack(anchor=W)
    rb3_dest_base = Radiobutton(
        f_right_base, text="Hexadecimal", variable=dest_base, value=16)
    rb3_dest_base.pack(anchor=W)
    dest_base.set(2)    # Default value

    # Creation of the convert button
    f_convert_button = Frame(lf_left, bd=6)
    f_convert_button.pack()
    button_convert = Button(
        f_convert_button, text="Convert", command=callback_convert, width=20)
    button_convert.pack()

    # Creation of the label to display the conversion result
    f_laber_result = Frame(lf_right, bd=4)
    f_laber_result.pack(fill="both", expand="yes")
    string_converted = StringVar()
    label_result = Label(
        f_laber_result, textvariable=string_converted, width=16, anchor=CENTER,
        wraplength=150)
    label_result.pack(fill="both", expand="yes")

    root.geometry('{}x{}'.format(430, 200))
    root.resizable(width=False, height=False)
    root.wm_title("Super Converter")
    return root


if __name__ == '__main__':
    pass
