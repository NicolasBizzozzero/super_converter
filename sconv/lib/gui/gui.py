import tkinter as tk
from tkinter import messagebox
from sys import argv
import json

from lib.gui.translation import Language
from lib.gui.convertwidget.convertwidget import ConvertMode, int_to_mode
from lib.gui.convertwidget.base import *
from lib.gui.convertwidget.temperature import *
from lib.gui.convertwidget.weight_mass import *
from lib.tools.switchcase import switch


class MainApplication(tk.Frame):
    """The main window of the sconv Application.

    Attributes:
        root          The Frame parent of the current Window.
        convert_mode  An enum describing what the window currently allow to
                      convert.
        language      An enum describing the language in which the window
                      is currently displayed.
        menubar       A MenuBar, never change even if the convert mode
                      change.
        convertwidget A widget associated with a conversion mode.
        var_reload      A BooleanVar indicating if the window needs to be
                        reloaded.
    """

    def __init__(self, root, convert_mode: ConvertMode, language: Language):
        super(MainApplication, self).__init__()
        self.convert_mode = convert_mode
        self.language = language
        self.var_reload = tk.BooleanVar()
        self.var_reload.set(False)

        self.init_root(root)
        self.init_menubar()
        self.init_convertwidget()
        self.pack_all()

    def init_root(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        path = "{}{}".format(argv[0][:-13], r"/res/icon.ico")
        self.root.iconbitmap(path)
        self.root.geometry('{}x{}'.format(430, 220))
        self.root.resizable(width=False, height=False)
        self.root.wm_title("Super Converter")

    def init_menubar(self):
        self.menubar = MenuBar(self.root, self, self.convert_mode,
                               self.language)

    def init_convertwidget(self):
        for case in switch(self.convert_mode):
            if case(ConvertMode.BASE):
                self.convertwidget = BaseWidget(self)
            if case(ConvertMode.WEIGHT_MASS):
                self.convertwidget = WeightMass(self)
            if case(ConvertMode.TEMPERATURE):
                self.convertwidget = Temperature(self)

    def pack_all(self):
        self.convertwidget.pack(fill=tk.BOTH, expand=True)
        self.pack(fill=tk.BOTH, expand=True)


class MenuBar(tk.Menu):
    """The MenuBar of the Main Application.

    Attributes:
        root            The parent windows in which the menu bar is.
        app
        var_mode        An Intvar containing the mode of the main widget.
        var_language    A StringVar containing the language in which the window
                        is currently displayed.
        mode_menu       A menu containing the differents modes availables.
        language_menu   A menu containing the differents languages availables.
        about_menu      A menu containing informations about the GUI software.
    """

    def __init__(self, root, app, convert_mode: ConvertMode,
                 language: Language):
        super(MenuBar, self).__init__(root)
        self.root = root
        self.app = app

        self.init_mode_menu(convert_mode)
        self.init_language_menu(language)
        self.init_about_menu()

        self.root.config(menu=self)

    def init_mode_menu(self, mode: ConvertMode):
        self.var_mode = tk.IntVar()
        self.var_mode.set(mode.value)

        self.mode_menu = tk.Menu(self, tearoff=0)
        self.mode_menu.add_radiobutton(label="Base",
                                       value=ConvertMode.BASE.value,
                                       command=self.cmd_switch_mode,
                                       variable=self.var_mode)
        self.mode_menu.add_radiobutton(label="Temperature",
                                       value=ConvertMode.TEMPERATURE.value,
                                       command=self.cmd_switch_mode,
                                       variable=self.var_mode)
        self.mode_menu.add_radiobutton(label="Weight/Mass",
                                       value=ConvertMode.WEIGHT_MASS.value,
                                       command=self.cmd_switch_mode,
                                       variable=self.var_mode)
        self.add_cascade(label="Mode", menu=self.mode_menu)

    def init_language_menu(self, language: Language):
        self.var_language = tk.StringVar()
        self.var_language.set(language.value)

        self.language_menu = tk.Menu(self, tearoff=0)
        self.language_menu.add_radiobutton(label="Français", value="fr",
                                           command=self.cmd_switch_language,
                                           variable=self.var_language)
        self.language_menu.add_radiobutton(label="English", value="en",
                                           command=self.cmd_switch_language,
                                           variable=self.var_language)
        self.language_menu.add_radiobutton(label="Español", value="es",
                                           command=self.cmd_switch_language,
                                           variable=self.var_language)
        self.add_cascade(label=_("Language"), menu=self.language_menu)

    def init_about_menu(self):
        self.about_menu = tk.Menu(self, tearoff=0)
        self.about_menu.add_command(label=_("About"), command=self.cmd_about)
        self.add_cascade(label=_("Help"), menu=self.about_menu)

    def cmd_switch_language(self):
        # Switch language
        filepath = r"data/preferences.json"
        with open(filepath) as file:
            filecontent = json.load(file)
            filecontent['language'] = self.var_language.get()
        with open(filepath, 'w') as file:
            file.write(json.dumps(filecontent))

        # Destroy the window
        self.root.destroy()
        self.root.quit()

        # Reload the window
        self.app.var_reload.set(True)

    def cmd_switch_mode(self):
        # Switch mode
        filepath = r"data/preferences.json"
        with open(filepath) as file:
            filecontent = json.load(file)
            filecontent['convertwidget'] = self.var_mode.get()
        with open(filepath, 'w') as file:
            file.write(json.dumps(filecontent))

        # Change widget
        self.app.convert_mode = int_to_mode(self.var_mode.get())
        self.app.init_convertwidget()

    def cmd_about(self):
        from pkg_resources import get_distribution

        messagebox.showinfo(_("About"), "{} {}".format(
            _("Super Converter version"),
            get_distribution('sconv').version))
