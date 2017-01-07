"""

"""

import tkinter as tk
import json

from super_converter.sconv.lib.gui.translation import Language, switch_language, str_to_language
from super_converter.sconv.lib.gui.gui import MainApplication

from super_converter.sconv.lib.gui.convertwidget.convertwidget import ConvertMode, int_to_mode


class Main():
    """Main class for the GUI of Super-Converter.

    Attributes:
        app    MainApplication instance.
        root   Window containing the app.
    """

    def __init__(self):
        pass

    def _run(self) -> None:
        """ Blocking fonction. Launch one instance of MainApplication and run it
            until _start_application terminate. After that, the function check
            a BooleanVar value set in app to know if another window needs to be
            created (i.e, if the language has been changed) and in this case,
            call itself recursively.
        """
        language = self._load_language(r"data/preferences.json")
        conv_widget = self._load_convwidget(r"data/preferences.json")
        self._start_application(conv_widget, language)
        if self.app.var_reload.get():
            self._run()

    def _start_application(self, convert_mode: ConvertMode,
                           language: Language) -> None:
        """ Blocking function. Create a Tk root object which will
            contains an instance of MainApplication.
        """
        self._init_language(language)
        self.root = tk.Tk()
        self.app = MainApplication(self.root, convert_mode, language)
        self.app.pack(side=tk.TOP, fill="both", expand=True)
        self.root.mainloop()

    def _load_language(self, filepath: str,
                       default: Language = Language.ENGLISH) -> Language:
        """ Retrieve a language stored in a preference file.
            Return default in case of error.
        """
        try:
            with open(filepath) as file:
                content = json.load(file)
            return str_to_language(content["language"])
        except Exception:
            return default

    def _load_convwidget(self, filepath: str,
                         default: ConvertMode = ConvertMode.BASE
                         ) -> ConvertMode:
        """ Retrieve a convert mode stored in a preference file.
            Return default in case of error.
        """
        try:
            with open(filepath) as file:
                content = json.load(file)
            return int_to_mode(content["convertwidget"])
        except Exception:
            return default

    def _init_language(self, language: Language):
        """ Need to be called once before starting the application to
            assign a language to the strings of the GUI.
        """
        switch_language(language)


def main():
    print("Bonjour GUI")
    Main()._run()


if __name__ == '__main__':
    main()
