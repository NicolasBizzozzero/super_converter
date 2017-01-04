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
    messagebox.showinfo(_("About"), "{} {}".format(
        _("Super Converter version"), __version__))


def callback_pass():
    pass


if __name__ == '__main__':
    pass
