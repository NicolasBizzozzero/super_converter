import tkinter as tk

from .convertwidget import ConvertWidget


class SpeedWidget(ConvertWidget):
    """Widget used to convert weight and mass units

    Attributes:
        root          The Frame parent of the widget.
    """

    def __init__(self, root):
        super(SpeedWidget, self).__init__(root)
        self.root = root
        self._init_frames()
        self._init_binds()

    def _init_frames(self):
        # Creation of the main frame
        f_main = tk.Frame(self.root)
        f_main.pack(fill="both", expand="yes", side=tk.TOP)

    def _init_binds(self):
        pass


if __name__ == '__main__':
    pass
