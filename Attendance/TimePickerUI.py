import ttkbootstrap as ttk
from leaveutil import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.toast import ToastNotification
class AddDate(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.adddate(master)

    def AddToIgnore(self):
        time = self.GetDateTime().date()
        if time in globaldata.ContainInfoDate:
            ToastNotification(title="错误",message="在特别添加的工作表中已经有这天了").show_toast()
            return
        if time not in globaldata.SkipInfoDate:
            globaldata.SkipInfoDate.append(time)

    def EditIgnore(self):
        window = ttk.Toplevel(title="编辑")
        print(ShowData_SkipDate(window))
        window.mainloop()
    def AddToWork(self):
        time = self.GetDateTime().date()
        if time in globaldata.SkipInfoDate:
            ToastNotification(title="错误",message="在特别添加的休假表中已经有这天了").show_toast()
            return
        if time not in globaldata.ContainInfoDate:
            globaldata.ContainInfoDate.append(time)

    def EditWork(self):
        window = ttk.Toplevel(title="编辑")
        print(ShowData_Contain(window))
        window.mainloop()
    def AddToSpecialOnTime(self):
        time = self.GetDateTime()
        if any(time.date() == ontime.date() for ontime in globaldata.SpecialOnworkTime):
            pass
        else:
            globaldata.SpecialOnworkTime.append(time)

    def EditSpecialOnTime(self):
        window = ttk.Toplevel(title="特殊上班日期")
        print(ShowData_SpecialOnWork(window))
        window.mainloop()
    def AddToSpecialOffTime(self):
        time = self.GetDateTime()
        if any(time.date() == ontime.date() for ontime in globaldata.SpecialOffWorkTime):
            pass
        else:
            globaldata.SpecialOffWorkTime.append(time)
    def EditSPecialOffTime(self):
        window = ttk.Toplevel(title="特殊下班日期")
        print(ShowData_SpecialOffWork(window))
        window.mainloop()

    def GetDateTime(self):
        hour = self.hourentity.amountusedvar.get()
        minutes = self.minutesentity.amountusedvar.get()
        time = self.dateentity.entry.get()
        strtime = f"{str(time)}/{hour}/{minutes}"
        format = "%Y/%m/%d/%H/%M"
        resulttime = datetime.datetime.strptime(strtime, format)
        return resulttime

    def adddate(self, maser):
        self.dateentity = ttk.DateEntry(maser, startdate=datetime.datetime(2023, 11, 4))
        self.dateentity.grid(column=0, row=0)
        self.hourentity = ttk.Meter(maser, amounttotal=24, amountused=10, subtext="小时", interactive=True,
                                    meterthickness=15, stripethickness=15)
        self.hourentity.grid(column=1, row=0)
        self.minutesentity = ttk.Meter(maser, amounttotal=60, amountused=0, subtext="分钟", interactive=True,
                                       meterthickness=15)
        self.minutesentity.grid(column=2, row=0)
        self.addtoignore = ttk.Button(maser, command=self.AddToIgnore, text="添加到休息日")
        self.addtowork = ttk.Button(maser, command=self.AddToWork, text="添加到工作日")
        self.editignore = ttk.Button(maser, command=self.EditIgnore, text="编辑休息日")
        self.editwork = ttk.Button(maser, command=self.EditWork, text="编辑工作日")
        self.addtospecialontime = ttk.Button(maser, command=self.AddToSpecialOnTime, text="添加特别的上班日期")
        self.editspecialontime = ttk.Button(maser, command=self.EditSpecialOnTime, text="编辑特别的上班日期")
        self.addtospecialofftime = ttk.Button(maser, command=self.AddToSpecialOffTime, text="添加特别的下班日期")
        self.editspecialofftime = ttk.Button(maser, command=self.EditSPecialOffTime, text="编辑特别的下班日期")
        self.addtowork.grid(column=0, row=1, pady=3,padx=3)
        self.editwork.grid(column=1, row=1, pady=3,padx=3)
        self.addtoignore.grid(column=0, row=2, pady=3,padx=3)
        self.editignore.grid(column=1, row=2, pady=3,padx=3)
        self.addtospecialontime.grid(column=0, row=3, pady=3,padx=3)
        self.editspecialontime.grid(column=1, row=3, pady=3,padx=3)
        self.addtospecialofftime.grid(column=0, row=4, pady=3,padx=3)
        self.editspecialofftime.grid(column=1, row=4, pady=3,padx=3)


class ShowData_SpecialOnWork(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.interface(master, globaldata.SpecialOnworkTime)

    def DeleteSpecialOnTime(self):
        selected_rows = self.tree.get_rows(selected=True)
        for row in selected_rows:
            globaldata.SpecialOnworkTime.remove(row.values.pop())
            row.delete()
    def interface(self, master, reusltlist):
        coldate=[
            {"text": "特殊上班日期", "stretch": False},
        ]
        # 创建 Treeview 控件
        self.tree = Tableview(master,coldata=coldate,height=20)
        # 插入数据
        index = 0
        for data in reusltlist:
            self.tree.insert_row(values=[data])
            index += 1
        self.tree.grid(row=0, column=0)
        self.delbutton=ttk.Button(master,command=self.DeleteSpecialOnTime,text="删除")
        self.delbutton.grid(row = 1,column = 0)


class ShowData_SpecialOffWork(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.interface(master, globaldata.SpecialOffWorkTime)

    def DeleteSpecialOffTime(self):
        selected_rows = self.tree.get_rows(selected=True)
        for row in selected_rows:
            globaldata.SpecialOffWorkTime.remove(row.values.pop())
            row.delete()
    def interface(self, master, reusltlist):
        coldate=[
            {"text": "特殊下班日期", "stretch": False},
        ]
        # 创建 Treeview 控件
        self.tree = Tableview(master,coldata=coldate,height=20)

        # 插入数据
        index = 0
        for data in reusltlist:
            self.tree.insert_row(values=[data])
            index += 1
        self.tree.grid(row=0, column=0)
        self.delbutton=ttk.Button(master,command=self.DeleteSpecialOffTime,text="删除")
        self.delbutton.grid(row = 1,column = 0)


class ShowData_SkipDate(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.interface(master, globaldata.SkipInfoDate)

    def DeleteDate(self):
        selected_rows = self.tree.get_rows(selected=True)
        for row in selected_rows:
            globaldata.SkipInfoDate.remove(row.values.pop())
            row.delete()
    def interface(self, master, reusltlist):
        coldate=[
            {"text": "放假日期", "stretch": False},
        ]
        # 创建 Treeview 控件
        self.tree = Tableview(master,coldata=coldate,height=20)

        # 插入数据
        index = 0
        for data in reusltlist:
            self.tree.insert_row(values=[data])
            index += 1
        self.tree.grid(row=0, column=0)
        self.delbutton=ttk.Button(master,command=self.DeleteDate,text="删除")
        self.delbutton.grid(row = 1,column = 0)
class ShowData_Contain(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.interface(master, globaldata.ContainInfoDate)

    def DeleteDate(self):
        selected_rows = self.tree.get_rows(selected=True)
        for row in selected_rows:
            globaldata.ContainInfoDate.remove(row.values.pop())
            row.delete()
    def interface(self, master, reusltlist):
        coldate=[
            {"text": "上班日期", "stretch": False},
        ]
        # 创建 Treeview 控件
        self.tree = Tableview(master,coldata=coldate,height=20)

        # 插入数据
        index = 0
        for data in reusltlist:
            self.tree.insert_row(values=[data])
            index += 1
        self.tree.grid(row=0, column=0)
        self.delbutton=ttk.Button(master,command=self.DeleteDate,text="删除")
        self.delbutton.grid(row = 1,column = 0)
