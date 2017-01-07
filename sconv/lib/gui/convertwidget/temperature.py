import tkinter as tk
import tkinter.ttk as ttk

from super_converter.sconv.lib.gui.convertwidget.convertwidget import ConvertWidget


class Temperature(ConvertWidget):
    """Widget used to convert weight and mass units

    Attributes:
        root          The Frame parent of the widget.
        str_to_convert
        str_converted
        scale_src
        scale_dest
    """

    def __init__(self, root):
        super(Temperature, self).__init__(root)
        self.root = root
        self._init_frames()
        self._init_binds()

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

        # Creation of the choice of the scales
        f_scales = tk.Frame(lf_left, bd=0)
        # Source scale
        f_left_scale = tk.LabelFrame(f_scales, bd=2,
                                    text="  {}  ".format(_("From")),
                                    labelanchor="n")
        self.scale_src = tk.StringVar()
        ############## COMBOBOX
        cbb_scale_src = ttk.Combobox(f_left_scale, textvariable=self.scale_src, width=11)
        cbb_scale_src['values'] = ("Celsius", "Delisle", "Fahrenheit", "Kelvin",
                                   "Newton", "Rankine", "Réaumur", "Rømer")
        cbb_scale_src.bind("<<ComboboxSelected>>", self._switch_scale_src)
        cbb_scale_src.current(0)
        #self.scale_src.set(0)    # Default value
        ############## END COMBOBOX
        # Destination scale
        f_right_scale = tk.LabelFrame(f_scales, bd=2,
                                     text="  {}  ".format(_("To")),
                                     labelanchor="n")
        self.scale_dest = tk.StringVar()
        ############## COMBOBOX
        cbb_scale_dest = ttk.Combobox(f_right_scale, textvariable=self.scale_dest, width=11)
        cbb_scale_dest['values'] = ("Celsius", "Delisle", "Fahrenheit", "Kelvin",
                                    "Newton", "Rankine", "Réaumur", "Rømer")
        cbb_scale_dest.bind("<<ComboboxSelected>>", self._switch_scale_dest)
        # previous : rb3_src_base = tk.Radiobutton(f_left_scale,text=_("Hexadecimal"),variable=self.scale_src, value=16)
        cbb_scale_dest.current(2)

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
        f_scales.pack(fill="x", expand="yes")
        f_left_scale.pack(fill="y", expand="yes", side=tk.LEFT, padx=5, pady=24)
        cbb_scale_src.pack(anchor=tk.W, padx=7, pady=5)
        f_right_scale.pack(fill="y", expand="yes", side=tk.RIGHT, padx=5, pady=24)
        cbb_scale_dest.pack(anchor=tk.W, padx=7, pady=5)
        f_convert_button.pack(expand="yes")
        button_convert.pack(expand="yes")
        f_label_result.pack(fill="both", expand="yes")
        label_result.pack(fill="both", expand="yes")

    def _init_binds(self):
        pass

    def _switch_scale_src(self, event):
        pass

    def _switch_scale_dest(self, event):
        pass

    def cmd_convert(self):
        pass


if __name__ == '__main__':
    pass
