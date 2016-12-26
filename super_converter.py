from lib.gui import initialisation_of_the_window
from lib.translation_functions import Language, switch_language


string_to_convert = None
string_converted = None
src_base = None
dest_base = None
var_language = None
root = None


def main():
    global root

    switch_language(Language.ENGLISH)
    root = initialisation_of_the_window()
    root.mainloop()


if __name__ == '__main__':
    main()
