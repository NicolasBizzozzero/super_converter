import tkinter as tk

from lib.gui.convertwidget.convertwidget import ConvertWidget
from lib.core.base import NumberWithBase, Base, int_to_base


class BaseWidget(ConvertWidget):
    """Widget used to change a number from one base to another.

    Attributes:
        parent          The Frame parent of the widget.
        base_src
        base_dest
        str_to_convert
        str_converted
    """

    def __init__(self, parent):
        super(BaseWidget, self).__init__(parent)
        self.parent = parent

        self._init_binds()
        self._init_frames()

    def _init_frames(self):
        # Creation of the main frame
        f_main = tk.Frame(self.parent)

        # Creation of the left labeled frame
        f_lf_left = tk.Frame(f_main, bd=6)
        lf_left = tk.LabelFrame(f_lf_left, text="  {}  ".format(_("Input")))

        # Creation of the right labeled frame
        f_lf_right = tk.Frame(f_main, bd=6)
        lf_right = tk.LabelFrame(f_lf_right, text="  {}  ".format(_("Output")))

        # Creation of the entry
        f_entry = tk.Frame(lf_left, bd=6)
        self.str_to_convert = tk.StringVar()
        entry_to_convert = tk.Entry(f_entry,
                                    textvariable=self.str_to_convert,
                                    exportselection=0)
        entry_to_convert.focus_set()

        # Creation of the choice of the bases
        f_bases = tk.Frame(lf_left, bd=0)
        # Source base
        f_left_base = tk.LabelFrame(f_bases, bd=2,
                                    text="  {}  ".format(_("From")),
                                    labelanchor="n")
        self.base_src = tk.IntVar()
        rb1_src_base = tk.Radiobutton(f_left_base,
                                      text=_("Binary"),
                                      variable=self.base_src, value=2)
        rb2_src_base = tk.Radiobutton(f_left_base,
                                      text=_("Decimal"),
                                      variable=self.base_src, value=10)
        rb3_src_base = tk.Radiobutton(f_left_base,
                                      text=_("Hexadecimal"),
                                      variable=self.base_src, value=16)
        self.base_src.set(10)    # Default value
        # Destination base
        f_right_base = tk.LabelFrame(f_bases, bd=2,
                                     text="  {}  ".format(_("To")),
                                     labelanchor="n")
        self.base_dest = tk.IntVar()
        rb1_dest_base = tk.Radiobutton(f_right_base,
                                       text=_("Binary"),
                                       variable=self.base_dest, value=2)
        rb2_dest_base = tk.Radiobutton(f_right_base,
                                       text=_("Decimal"),
                                       variable=self.base_dest, value=10)
        rb3_dest_base = tk.Radiobutton(f_right_base,
                                       text=_("Hexadecimal"),
                                       variable=self.base_dest, value=16)
        self.base_dest.set(2)    # Default value

        # Creation of the convert button
        f_convert_button = tk.Frame(lf_left, bd=6)
        button_convert = tk.Button(f_convert_button, text=_("Convert"),
                                   command=self.cmd_convert, width=20)

        # Creation of the label to display the conversion result
        f_label_result = tk.Frame(lf_right, bd=4)
        self.str_converted = tk.StringVar()
        label_result = tk.Label(f_label_result,
                                textvariable=self.str_converted,
                                width=16, anchor=tk.CENTER,
                                wraplength=150)

        # Pack all this stuff !
        f_main.pack(fill="both", expand="yes", side=tk.TOP)
        f_lf_left.pack(fill="both", expand="yes", side=tk.LEFT)
        lf_left.pack(fill="both", expand="yes")
        f_lf_right.pack(fill="both", expand="yes", side=tk.RIGHT)
        lf_right.pack(fill="both", expand="yes")
        f_entry.pack()
        entry_to_convert.pack()
        f_bases.pack(fill="x", expand="yes")
        f_left_base.pack(fill="y", expand="yes", side=tk.LEFT)
        rb1_src_base.pack(anchor=tk.W)
        rb2_src_base.pack(anchor=tk.W)
        rb3_src_base.pack(anchor=tk.W)
        f_right_base.pack(fill="y", expand="yes", side=tk.RIGHT)
        rb1_dest_base.pack(anchor=tk.W)
        rb2_dest_base.pack(anchor=tk.W)
        rb3_dest_base.pack(anchor=tk.W)
        f_convert_button.pack(expand="yes")
        button_convert.pack(expand="yes")
        f_label_result.pack(fill="both", expand="yes")
        label_result.pack(fill="both", expand="yes")

    def _init_binds(self):
        self.parent.root.bind('<Return>', self.cmd_bind_enter)

    def cmd_bind_enter(self, event):
        self.cmd_convert()

    def cmd_convert(self):
        number_w_base = NumberWithBase(self.str_to_convert.get(),
                                       int_to_base(self.base_src.get()))
        number_w_base.convert(int_to_base(self.base_dest.get()))
        self.str_converted.set(str(number_w_base))


if __name__ == '__main__':
    pass
