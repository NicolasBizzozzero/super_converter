import tkinter as tk
from enum import Enum


class ModeDoesNotExists(Exception):
    pass


class ConvertMode(Enum):
    NONE = 0
    BASE = 1
    WEIGHT_MASS = 2
    TEMPERATURE = 3
    DISTANCE = 4
    PRESSURE = 5
    CURRENCY = 6
    TIME = 7
    SPEED = 8
    ANGLE = 9


def int_to_mode(integer: int) -> ConvertMode:
    if integer == 1:
        return ConvertMode.BASE
    elif integer == 2:
        return ConvertMode.WEIGHT_MASS
    elif integer == 3:
        return ConvertMode.TEMPERATURE
    elif integer == 4:
        return ConvertMode.DISTANCE
    elif integer == 5:
        return ConvertMode.PRESSURE
    elif integer == 6:
        return ConvertMode.CURRENCY
    elif integer == 7:
        return ConvertMode.TIME
    elif integer == 8:
        return ConvertMode.SPEED
    elif integer == 9:
        return ConvertMode.ANGLE
    else:
        raise ModeDoesNotExists(("{} is currently not implemented."
                                 ).format(integer))


class ConvertWidget(tk.Frame):
    """Abstract class containing a widget associated with a conversion mode.

    Attributes:
        parent          The Frame parent of the widget.
    """

    def __init__(self, parent):
        super(ConvertWidget, self).__init__(parent)
        self.parent = parent

    def destroy_widget(self):
        self.pack_forget()  # Unmap the widget (still loaded)
        self.destroy()      # Destroy the widget


if __name__ == '__main__':
    pass
