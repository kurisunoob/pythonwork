# 跳过或者添加特定日期
import sys
from time import strptime

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from persondata import *
from ttkbootstrap.style import Bootstyle
from leaveutil import *


class LeaveDataDialog(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.name = ttk.StringVar(value="")
        self.leavehours = ttk.IntVar(value=1)
        self.leavedata = 1
        self.completedata = 1
        self.leavereason = ttk.IntVar(value=1)

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

    def create_form_Menubutton(self, label, var):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)
        lists = [('病假', 1), ('事假', 2), ('年假', 3)]
        for item, num in lists:
            ttk.Radiobutton(container, text=item, variable=var, value=num).pack()
        # menb = ttk.Menubutton(master=container)
        # menu = ttk.Menu(container)
        # for item in lists:
        #     menu.add_radiobutton(label=item, value=item, variable=var)
        # menb['menu'] = menu
        # menb.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_form_dateentry_complete(self, label):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ls = ttk.DateEntry(master=container, dateformat="%x")
        ls.pack(side=LEFT, padx=5, fill=X, expand=YES)
        self.completedata = ls.entry

    def create_form_dateentry_leave(self, label):
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
            text="记录",
            command=self.on_submit,
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
        if sys.platform == 'win32':
            ledate = datetime.datetime.strptime(str(self.leavedata.get()), '%Y/%m/%d')
            comdate = datetime.datetime.strptime(str(self.completedata.get()), '%Y/%m/%d')
        else:
            ledate = datetime.datetime.strptime(str(self.leavedata.get()), '%Y年%m月%d日')
            comdate = datetime.datetime.strptime(str(self.completedata.get()), '%Y年%m月%d日')
        match self.leavereason.get():
            case 1:
                persondata = SickLeavaData(self.name.get(), ledate, comdate, self.leavehours.get())
                if not bContainPersonData(globaldata.SickLeaveList, persondata):
                    globaldata.SickLeaveList.append(persondata)
            case 2:
                persondata = PersonalLeaveData(self.name.get(), ledate, comdate, self.leavehours.get())
                if not bContainPersonData(globaldata.PersonalLeaveList, persondata):
                    globaldata.PersonalLeaveList.append(persondata)
            case 3:
                persondata = YearLeavaData(self.name.get(), ledate, comdate, self.leavehours.get())
                if not bContainPersonData(globaldata.YearLeaveList, persondata):
                    globaldata.YearLeaveList.append(persondata)


class Calculator(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, padding=10, **kwargs)
        ttk.Style().configure("TButton", font="TkFixedFont 12")
        self.pack(fill=BOTH, expand=YES)
        self.digitsvar = ttk.StringVar(value="")
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
        container = ttk.Frame(master=self, padding=2)
        container.pack(fill=X, pady=20)
        digits = ttk.Label(
            master=container,
            font="TkFixedFont 14",
            textvariable=self.digitsvar,
            anchor=E,
        )
        digits.pack(fill=X)

    def create_num_pad(self):
        container = ttk.Frame(master=self, padding=2)
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
        if child.winfo_class() != 'TFrame':
            return

        style_color = Bootstyle.ttkstyle_widget_color(bootstyle)
        frm = ttk.Frame(self)
        frm.grid(row=self.cumulative_rows, column=0, sticky=EW)

        # header title
        header = ttk.Label(
            master=frm,
            text=title
        )
        if kwargs.get('textvariable'):
            header.configure(textvariable=kwargs.get('textvariable'))
        header.pack(side=LEFT, fill=BOTH, padx=10)

        # header toggle button
        def _func(c=child):
            return self._toggle_open_close(c)

        btn = ttk.Button(
            master=frm,
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


def bContainPersonData(_list: list, person):
    for item in _list:
        if item == person:
            return True
    return False


def show_message(str):
    root = ttk.Toplevel()
    root.title = "提示"
    labels = ttk.Label(root, text=str)
    labels.pack()
    root.mainloop()


class ShowData(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.interface(master, globaldata.ResultList)

    def interface(self, master, reusltlist):
        globaldata.ResultList.clear()
        # 创建 Treeview 控件
        self.tree = ttk.Treeview(master, columns=('Name', 'Date', 'OnTime', 'OffTime'), height=20)

        # 定义列名
        self.tree.heading('#0', text='序号')
        self.tree.heading('Name', text='姓名')
        self.tree.heading('Date', text='记录日期')
        self.tree.heading('OnTime', text='上班时间')
        self.tree.heading('OffTime', text='下班时间')

        # 设置列宽度
        self.tree.column('#0', width=50)
        self.tree.column('Name', width=100)
        self.tree.column('Date', width=90)
        self.tree.column('OnTime', width=150)
        self.tree.column('OffTime', width=150)

        def getresult(time):
            if type(time) == type(''):
                return "-"
            else:
                return time.strftime("%H:%M:%S")

        # 插入数据
        NormalDateFilter()
        index = 0
        for data in reusltlist:
            self.tree.insert('', ttk.END, text=str(index), values=(
                data.Name, data.JoinDateTime, getresult(data.OnWorkTime), getresult(data.OffWorkTime)))
            index += 1
        vbar = ttk.Scrollbar(master, orient=ttk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=vbar.set)
        # 显示 Treeview 控件
        self.tree.grid(row=0, column=0, sticky=ttk.NSEW)
        vbar.grid(row=0, column=1, sticky=ttk.NS)


class AddDate(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.adddate(master)

    def AddToIgnore(self):
        time = self.GetDateTime().date()
        if time not in globaldata.SkipInfoDate:
            globaldata.SkipInfoDate.append(time.date)

    def AddToWork(self):
        time = self.GetDateTime().date()
        if time not in globaldata.ContainInfoDate:
            globaldata.ContainInfoDate.append(time)

    def AddToSpecialOnTime(self):
        time = self.GetDateTime()
        if time not in globaldata.SpecialOnworkTime:
            globaldata.SpecialOnworkTime.append(time)

    def AddToSpecialOffTime(self):
        time = self.GetDateTime()
        if time not in globaldata.SpecialOffWorkTime:
            globaldata.SpecialOffWorkTime.append(time)

    def GetDateTime(self):
        hour=self.hourentity.amountusedvar.get()
        minutes = self.minutesentity.amountusedvar.get()
        time = self.dateentity.entry.get()
        strtime=f"{str(time)}/{hour}/{minutes}"
        format="%Y/%m/%d/%H/%M"
        resulttime = datetime.datetime.strptime(strtime,format)
        return resulttime
    def adddate(self, maser):
        self.dateentity = ttk.DateEntry(maser,startdate=datetime.datetime(2023,11,4))
        self.dateentity.grid(column=0, row=0)
        self.hourentity = ttk.Meter(maser, amounttotal=24, amountused=10, subtext="小时", interactive=True,
                                    meterthickness=15, stripethickness=15)
        self.hourentity.grid(column=1, row=0)
        self.minutesentity = ttk.Meter(maser, amounttotal=60, amountused=0, subtext="分钟", interactive=True,
                                       meterthickness=15)
        self.minutesentity.grid(column=2, row=0)
        self.addtoignore = ttk.Button(maser, command=self.AddToIgnore, text="添加到休息日")
        self.addtowork = ttk.Button(maser, command=self.AddToWork, text="添加到工作日")
        self.addtospecialontime = ttk.Button(maser, command=self.AddToSpecialOnTime, text="添加特别的上班日期")
        self.addtospecialofftime = ttk.Button(maser, command=self.AddToSpecialOffTime, text="添加特别的下班日期")
        self.addtowork.grid(column=0, row=1, pady=3)
        self.addtoignore.grid(column=0, row=2, pady=3)
        self.addtospecialontime.grid(column=0, row=3, pady=3)
        self.addtospecialofftime.grid(column=0, row=4, pady=3)
