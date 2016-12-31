from tkinter import Tk, Frame, LabelFrame, Entry, Radiobutton, TOP, LEFT, \
    RIGHT, CENTER, StringVar, IntVar, W, Button, Label, Menu, messagebox
from lib.convertion_functions import convert
from lib.translation_functions import str_to_language, switch_language
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


def callback_switch_language() -> None:
    """ Wrap the convert function with its proper arguments. """
    global var_language
    global root

    # Switch language
    language_string = var_language.get()
    language_enum = str_to_language(language_string)
    switch_language(language_enum)

    # Recreate the window
    root.destroy()
    root = initialisation_of_the_window()
    var_language.set(language_string)
    root.mainloop()


def callback_bind_enter(event) -> None:
    callback_convert()


def callback_about():
    global VERSION
    messagebox.showinfo(_("About"), "{} {}".format(
        _("Super Converter version"), VERSION))


def donothing():
    pass


def initialisation_of_the_menu() -> None:
    global var_language
    global root

    menubar = Menu(root)

    # Language Menu
    var_language = StringVar()
    language_menu = Menu(menubar, tearoff=0)
    language_menu.add_radiobutton(
        label="Français", value="fr", command=callback_switch_language, variable=var_language)
    language_menu.add_radiobutton(
        label="English", value="en", command=callback_switch_language, variable=var_language)
    language_menu.add_radiobutton(
        label="Español", value="es", command=callback_switch_language, variable=var_language)
    menubar.add_cascade(label=_("Language"), menu=language_menu)
    var_language.set("en")

    # About menu
    about_menu = Menu(menubar, tearoff=0)
    about_menu.add_command(label=_("About"), command=callback_about)
    menubar.add_cascade(label=_("Help"), menu=about_menu)

    root.config(menu=menubar)


def initialisation_of_the_window() -> Tk:
    """ Return the properly initialized root of the windows. """
    global string_to_convert
    global string_converted
    global src_base
    global dest_base
    global var_language
    global root

    # Creation of the root
    root = Tk()
    path = argv[0][:-18] + r"res/icon.ico"
    root.iconbitmap(path)
    root.bind('<Return>', callback_bind_enter)

    # Initialisation of the menu
    initialisation_of_the_menu()

    # Creation of the main frame
    f_main = Frame(root)
    f_main.pack(fill="both", expand="yes", side=TOP)

    # Creation of the left labeled frame
    f_lf_left = Frame(f_main, bd=6)
    f_lf_left.pack(fill="both", expand="yes", side=LEFT)
    lf_left = LabelFrame(f_lf_left, text="  {}  ".format(_("Input")))
    lf_left.pack(fill="both", expand="yes")

    # Creation of the right labeled frame
    f_lf_right = Frame(f_main, bd=6)
    f_lf_right.pack(fill="both", expand="yes", side=RIGHT)
    lf_right = LabelFrame(f_lf_right, text="  {}  ".format(_("Output")))
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
    f_left_base = LabelFrame(
        f_bases, bd=2, text="  {}  ".format(_("From")), labelanchor="n")
    f_left_base.pack(fill="y", expand="yes", side=LEFT)
    src_base = IntVar()
    rb1_src_base = Radiobutton(
        f_left_base, text=_("Binary"), variable=src_base, value=2)
    rb1_src_base.pack(anchor=W)
    rb2_src_base = Radiobutton(
        f_left_base, text=_("Decimal"), variable=src_base, value=10)
    rb2_src_base.pack(anchor=W)
    rb3_src_base = Radiobutton(
        f_left_base, text=_("Hexadecimal"), variable=src_base, value=16)
    rb3_src_base.pack(anchor=W)
    src_base.set(10)    # Default value
    # Destination base
    f_right_base = LabelFrame(
        f_bases, bd=2, text="  {}  ".format(_("To")), labelanchor="n")
    f_right_base.pack(fill="y", expand="yes", side=RIGHT)
    dest_base = IntVar()
    rb1_dest_base = Radiobutton(
        f_right_base, text=_("Binary"), variable=dest_base, value=2)
    rb1_dest_base.pack(anchor=W)
    rb2_dest_base = Radiobutton(
        f_right_base, text=_("Decimal"), variable=dest_base, value=10)
    rb2_dest_base.pack(anchor=W)
    rb3_dest_base = Radiobutton(
        f_right_base, text=_("Hexadecimal"), variable=dest_base, value=16)
    rb3_dest_base.pack(anchor=W)
    dest_base.set(2)    # Default value

    # Creation of the convert button
    f_convert_button = Frame(lf_left, bd=6)
    f_convert_button.pack()
    button_convert = Button(
        f_convert_button, text=_("Convert"), command=callback_convert, width=20)
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
