# 跳过或者添加特定日期
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import Data as globaldata
from persondata import *
from ttkbootstrap.style import Bootstyle
def SkipDate(JoinDateTime:datetime):
    for date in globaldata.ContainInfoDate:
        if date == JoinDateTime:
            return False
    for date in globaldata.SkipInfoDate:
        if date == globaldata.SkipInfoDate:
            return True

    if JoinDateTime.weekday() == 6 or JoinDateTime.weekday() == 7:
        return True
    return False
class LeaveDataDialog(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.name = ttk.StringVar(value="")
        self.leavehours = ttk.IntVar(value=1)
        self.leavedata=1
        self.completedata=1
        self.leavereason=ttk.IntVar(value=1)

        # form header
        hdr_txt = "Please enter your contact information"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_Menubutton("假种", self.leavereason)
        self.create_form_entry("姓名", self.name)
        self.create_form_entry("请假小时数", self.leavehours)
        self.create_form_dateentry_leave("请假日期")
        self.create_form_dateentry_complete("补齐日期")
        self.create_buttonbox()

    def create_form_Menubutton(self,label,var):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)
        lists =[('病假',1),('事假',2),('年假',3)]
        for item, num in lists:
            ttk.Radiobutton(container,text=item,variable=var,value=num).pack()
        # menb = ttk.Menubutton(master=container)
        # menu = ttk.Menu(container)
        # for item in lists:
        #     menu.add_radiobutton(label=item, value=item, variable=var)
        # menb['menu'] = menu
        # menb.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_form_dateentry_complete(self,label):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ls = ttk.DateEntry(master=container)
        ls.pack(side=LEFT, padx=5, fill=X, expand=YES)
        self.completedata = ls.entry
    def create_form_dateentry_leave(self,label):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ls = ttk.DateEntry(master=container)
        ls.pack(side=LEFT, padx=5, fill=X, expand=YES)
        self.leavedata = ls.entry

    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()
        #
        # cnl_btn = ttk.Button(
        #     master=container,
        #     text="Cancel",
        #     command=self.on_cancel,
        #     bootstyle=DANGER,
        #     width=6,
        # )
        # cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        """Print the contents to console and return the values."""
        ledate = datetime.datetime.strptime(str(self.leavedata.get()), '%Y/%m/%d');
        comdate = datetime.datetime.strptime(str(self.completedata.get()), '%Y/%m/%d');
        match self.leavereason.get():
            case 1:
                globaldata.SickLeaveList.append(SickLeavaData(self.name.get(), ledate, comdate, self.leavehours))
            case 2:
                globaldata.PersonalLeaveList.append( PersonalLeaveData(self.name.get(), ledate, comdate, self.leavehours))
            case 3:
                globaldata.YearLeaveList.append(YearLeavaData(self.name.get(), ledate, comdate, self.leavehours))

class Calculator(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, padding=10, **kwargs)
        ttk.Style().configure("TButton", font="TkFixedFont 12")
        self.pack(fill=BOTH, expand=YES)
        self.digitsvar = ttk.StringVar(value=0)
        self.xnum = ttk.DoubleVar()
        self.ynum = ttk.DoubleVar()
        self.operator = ttk.StringVar(value="+")

        if "bootstyle" in kwargs:
            self.bootstyle = kwargs.pop("bootstyle")
        else:
            self.bootstyle = None
        self.create_num_display()
        self.create_num_pad()

    def create_num_display(self):
        container = ttk.Frame(master=self, padding=2, bootstyle=self.bootstyle)
        container.pack(fill=X, pady=20)
        digits = ttk.Label(
            master=container,
            font="TkFixedFont 14",
            textvariable=self.digitsvar,
            anchor=E,
        )
        digits.pack(fill=X)

    def create_num_pad(self):
        container = ttk.Frame(master=self, padding=2, bootstyle=self.bootstyle)
        container.pack(fill=BOTH, expand=YES)
        matrix = [
            ("%", "C", "CE", "/"),
            (7, 8, 9, "*"),
            (4, 5, 6, "-"),
            (1, 2, 3, "+"),
            ("±", 0, ".", "="),
        ]
        for i, row in enumerate(matrix):
            container.rowconfigure(i, weight=1)
            for j, num_txt in enumerate(row):
                container.columnconfigure(j, weight=1)
                btn = self.create_button(master=container, text=num_txt)
                btn.grid(row=i, column=j, sticky=NSEW, padx=1, pady=1)

    def create_button(self, master, text):
        if text == "=":
            bootstyle = SUCCESS
        elif not isinstance(text, int):
            bootstyle = SECONDARY
        else:
            bootstyle = PRIMARY
        return ttk.Button(
            master=master,
            text=text,
            command=lambda x=text: self.on_button_pressed(x),
            bootstyle=bootstyle,
            width=2,
            padding=10,
        )

    def reset_variables(self):
        self.xnum.set(value=0)
        self.ynum.set(value=0)
        self.operator.set("+")

    def on_button_pressed(self, txt):
        """Handles and routes all button press events."""
        display = self.digitsvar.get()

        # remove operator from screen after button is pressed
        if len(display) > 0:
            if display[0] in ["/", "*", "-", "+"]:
                display = display[1:]

        if txt in ["CE", "C"]:
            self.digitsvar.set("")
            self.reset_variables()
        elif isinstance(txt, int):
            self.press_number(display, txt)
        elif txt == "." and "." not in display:
            self.digitsvar.set(f"{display}{txt}")
        elif txt == "±":
            self.press_inverse(display)
        elif txt in ["/", "*", "-", "+"]:
            self.press_operator(txt)
        elif txt == "=":
            self.press_equals(display)

    def press_number(self, display, txt):
        """A digit button is pressed"""
        if display == "0":
            self.digitsvar.set(txt)
        else:
            self.digitsvar.set(f"{display}{txt}")

    def press_inverse(self, display):
        """The inverse number button is pressed"""
        if display.startswith("-"):
            if len(display) > 1:
                self.digitsvar.set(display[1:])
            else:
                self.digitsvar.set("")
        else:
            self.digitsvar.set(f"-{display}")

    def press_operator(self, txt):
        """An operator button is pressed"""
        self.operator.set(txt)
        display = float(self.digitsvar.get())
        if self.xnum.get() != 0:
            self.ynum.set(display)
        else:
            self.xnum.set(display)
        self.digitsvar.set(txt)

    def press_equals(self, display):
        """The equals button is pressed."""
        if self.xnum.get() != 0:
            self.ynum.set(display)
        else:
            self.xnum.set(display)
        x = self.xnum.get()
        y = self.ynum.get()
        op = self.operator.get()
        if all([x, y, op]):
            result = eval(f"{x}{op}{y}")
            self.digitsvar.set(result)
            self.reset_variables()

class CollapsingFrame(ttk.Frame):
    """A collapsible frame widget that opens and closes with a click."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0, weight=1)
        self.cumulative_rows = 0


    def add(self, child, title="", bootstyle=PRIMARY, **kwargs):
        """Add a child to the collapsible frame

        Parameters:

            child (Frame):
                The child frame to add to the widget.

            title (str):
                The title appearing on the collapsible section header.

            bootstyle (str):
                The style to apply to the collapsible section header.

            **kwargs (Dict):
                Other optional keyword arguments.
        """
        if child.winfo_class() != 'TFrame':
            return

        style_color = Bootstyle.ttkstyle_widget_color(bootstyle)
        frm = ttk.Frame(self, bootstyle=style_color)
        frm.grid(row=self.cumulative_rows, column=0, sticky=EW)

        # header title
        header = ttk.Label(
            master=frm,
            text=title,
            bootstyle=(style_color, INVERSE)
        )
        if kwargs.get('textvariable'):
            header.configure(textvariable=kwargs.get('textvariable'))
        header.pack(side=LEFT, fill=BOTH, padx=10)

        # header toggle button
        def _func(c=child): return self._toggle_open_close(c)
        btn = ttk.Button(
            master=frm,
            bootstyle=style_color,
            command=_func
        )
        btn.pack(side=RIGHT)

        # assign toggle button to child so that it can be toggled
        child.btn = btn
        child.grid(row=self.cumulative_rows + 1, column=0, sticky=NSEW)

        # increment the row assignment
        self.cumulative_rows += 2

    def _toggle_open_close(self, child):
        """Open or close the section and change the toggle button
        image accordingly.

        Parameters:

            child (Frame):
                The child element to add or remove from grid manager.
        """
        if child.winfo_viewable():
            child.grid_remove()
        else:
            child.grid()

