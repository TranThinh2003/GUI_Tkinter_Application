import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import  sleep       
import pickle

import random

import time

t = time.localtime()
current_time = time.strftime("[%H:%M]", t)


#===================================================================
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        "Display text in a tooltip window"
        if self.tip_window or not tip_text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")      # get size of widget
        x = x + self.widget.winfo_rootx() + 25          # calculate to display tooltip 
        y = y + cy + self.widget.winfo_rooty() + 25     # below and to the right
        self.tip_window = tw = tk.Toplevel(self.widget) # create new tooltip window
        tw.wm_overrideredirect(True)                    # remove all Window Manager (wm) decorations
#         tw.wm_overrideredirect(False)                 # uncomment to see the effect
        tw.wm_geometry("+%d+%d" % (x, y))               # create window size

        label = tk.Label(tw, text=tip_text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "10", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()
            
#===================================================================          
def create_ToolTip(widget, text):
    toolTip = ToolTip(widget)       # create instance of class
    def enter(event):
        toolTip.show_tip(text)
    def leave(event):
        toolTip.hide_tip()
    widget.bind('<Enter>', enter)   # bind mouse events
    widget.bind('<Leave>', leave)

#=================================================================== 
class OOP():
    def __init__(self):         # Initializer method
        # Create instance
        self.win = tk.Tk()   
        # create_ToolTip(self.win, 'Hello GUI')
        self.tasks = []
        self.cnt = 0
        self.cnt_add = 0
        # Add a title       
        self.win.title("TO_DO_LIST - TranHungThinh")      
        self.python_image = tk.PhotoImage('download.jpg')
        self.create_widgets()
        
                    
    # Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit() 

    def clear_listbox(self):
        self.lb_tasks.delete(0,"end")

    def clear_listbox_tab2(self):
        self.lb_tasks_tab2.delete(0,"end")

    def update_listbox(self):
        self.clear_listbox()
        for task in self.tasks:
            self.lb_tasks.insert("end", task)

    def add_task(self):
        task = self.txt_input.get()
        if task != '':
            if (self.input_day.get() != '' and int(self.input_day.get()) >= 1 and int(self.input_day.get()) <= 31) and self.number_month.get() != "" and self.input_year.get() != '' and self.number_hour.get() != '' and int(self.minute.get()) <= 60 and self.number_chosen.get() != '' : 
                self.cnt_add+=1
                self.tasks.append("{}/ [{}:{} {}][{}/{}/{}]  |  {}".format(self.cnt_add,self.number_hour.get(),self.minute.get(),self.number_chosen.get(),self.input_day.get(),self.number_month.get(),self.input_year.get(),task))
                self.display['text'] = "Task has added!"
                self.update_listbox()
                self.cnt+=1
                self.lb_tasks_tab2.insert('end',' {} ) {}  |  Task Added:  {}'.format(self.cnt,current_time,task))

            elif (self.input_day.get() != '' and int(self.input_day.get()) >= 1 and int(self.input_day.get()) <= 31) and self.number_month.get() != "" and self.input_year.get() != '' : 
                self.cnt_add+=1
                self.tasks.append("{}/ [{}/{}/{}]  |  {}".format(self.cnt_add,self.input_day.get(),self.number_month.get(),self.input_year.get(),task))
                self.display['text'] = "Task has added!"
                self.update_listbox()
                self.cnt+=1
                self.lb_tasks_tab2.insert('end',' {} ) {}  |  Task Added:  {}'.format(self.cnt,current_time,task))

            elif self.number_hour.get() != '' and int(self.minute.get()) <= 60 and self.number_chosen.get() != '' : 
                self.cnt_add+=1
                self.tasks.append("{}/ [{}:{} {}]  |  {}".format(self.cnt_add,self.number_hour.get(),self.minute.get(),self.number_chosen.get(),task))
                self.display['text'] = "Task has added!"
                self.update_listbox()
                self.cnt+=1
                self.lb_tasks_tab2.insert('end',' {} ) {}  |  Task Added:  {}'.format(self.cnt,current_time,task))
            
            else:
                self.cnt_add+=1
                self.tasks.append("{}/ [No Time][No Day]  |  {}".format(self.cnt_add,task))
                self.display['text'] = "Task has added!"
                self.update_listbox()
                self.cnt+=1
                self.lb_tasks_tab2.insert('end',' {} ) {}  |  Task Added:  {}'.format(self.cnt,current_time,task))
        else:
            self.display['text'] = "Please enter a task!"
        self.txt_input.delete(0,'end')

    

    def delete(self):
        task = self.lb_tasks.get('active')
        if task in self.tasks:
            self.tasks.remove(task)
        # Update list box
            self.update_listbox()
            self.cnt+=1
            self.lb_tasks_tab2.insert('end',' {} ) {}  |  Task Deleted:  {}'.format(self.cnt,current_time,task))
            self.display['text'] = "Task deleted!"
        else:
            msg.showwarning(title='Warning!!!',message='Not have task to delete')

    def delete_all(self):
        global tasks
        task = self.lb_tasks.get('active')                   
        if task in self.tasks:
            self.cnt+=1
            self.tasks = []
            self.update_listbox()
            self.lb_tasks_tab2.insert('end',' {} ) {}  |  Delete All Task'.format(self.cnt,current_time))
        else:
            msg.showwarning(title='Warning!!!',message='Not have task to delete')
        
    def choose_random(self):
        task = self.lb_tasks.get('active')                   
        if task in self.tasks:
            self.cnt+=1
            task = random.choice(self.tasks)
            self.display['text'] = task
            self.lb_tasks_tab2.insert('end',' {} ) {}  |  Choose_Random:  {}'.format(self.cnt,current_time,task))
        else:
            msg.showwarning(title='Warning!!!',message='Not have task to delete')

    def number_of_task(self):
        number_of_tasks = len(self.tasks)
        self.cnt+=1
        msg = "Number of tasks : %s" %number_of_tasks
        self.display['text'] = msg
        self.lb_tasks_tab2.insert('end',' {} ) {}  |  Current of task:  {}'.format(self.cnt,current_time,number_of_tasks))


    def load_task(self):
        try:
            tasks = pickle.load(open('data.dat','rb'))
            self.lb_tasks.delete(0,tk.END)
            for task in tasks:
                self.lb_tasks.insert(tk.END,task)
            self.display['text'] = "Task has loaded!"
        except:
            msg.showwarning(title='Warning!!!',message='Can not find tasks.dat')

    def save(self):
        tasks = self.lb_tasks.get(0,self.lb_tasks.size())
        pickle.dump(tasks,open("data.dat",'wb'))
        self.display['text'] = "Task has saved!"
        self.lb_tasks_tab2.insert('end',' {} ) {}  |  Tasks had saved '.format(self.cnt,current_time))


    #####################################################################################       
    def create_widgets(self):    
        tabControl = ttk.Notebook(self.win)          # Create Tab Control        
        tab1 = tk.Frame(tabControl,background='#3E3E40')            # Create a tab 
        tabControl.add(tab1, text='Main')      # Add the tab
        tab2 = tk.Frame(tabControl,background='#3E3E40')            # Add a second tab
        tabControl.add(tab2, text='History')      # Make second tab visible        
        tabControl.pack(expand=1, fill="both")  # Pack to make visible

        # LabelFrame using tab1 as the parent
        mighty = tk.LabelFrame(tab1, text=' To do List ',font=("Arial", 14))
        mighty.pack(padx=10,pady=10,fill=BOTH, expand=True)
        mighty.configure(foreground='#D94A56',background='#3E3E40')
        

        mighty3 = tk.LabelFrame(mighty,text='Function',font=("Arial", 14))
        mighty3.grid(column=0, row=0, padx=8, pady=4)
        mighty3.configure(foreground='#D94A56',background='#3E3E40')

        mighty10 = tk.LabelFrame(mighty,text='Display',font=("Arial", 14))
        mighty10.grid(column=1, row=0, padx=8, pady=4) 
        mighty10.configure(foreground='#D94A56',background='#3E3E40')

        mighty5 = tk.LabelFrame(mighty10,text='Input yout task',font=("Arial", 10))
        mighty5.grid(column=0, row=0, padx=10, pady=10)
        mighty5.configure(foreground='#D94A56',background='#3E3E40')

        mighty8 = tk.LabelFrame(mighty10,text='Input your time',font=("Arial", 10))
        mighty8.grid(column=0, row=1, padx=8, pady=4) 
        mighty8.configure(foreground='#D94A56',background='#3E3E40')

        mighty9 = tk.LabelFrame(mighty10,text='Input your day',font=("Arial", 10))
        mighty9.grid(column=0, row=2, padx=8, pady=4) 
        mighty9.configure(foreground='#D94A56',background='#3E3E40')

        mighty4 = tk.LabelFrame(mighty10,text='List to do',font=("Arial", 10))
        mighty4.grid(column=0, row=3, padx=8, pady=4) 
        mighty4.configure(foreground='#D94A56',background='#3E3E40')
        
        
        # Tab Control 2 ----------------------------------------------------------------------
        
        mighty2 = LabelFrame(tab2, text='History Operation',font=("Arial", 14))
        mighty2.pack(padx=10,pady=10,fill=BOTH, expand=True)
        mighty2.configure(foreground='#D94A56',background='#3E3E40')

        mighty7 = tk.LabelFrame(mighty2,text='Function',font=("Arial", 14))
        mighty7.grid(column=0, row=0, padx=8, pady=4)
        mighty7.configure(foreground='#D94A56',background='#3E3E40')


        mighty6 = tk.LabelFrame(mighty2,text='History',font=("Arial", 14))
        mighty6.grid(column=1, row=0, padx=8, pady=4)
        mighty6.configure(foreground='#D94A56',background='#3E3E40')
        

        # Creating a Menu Bar
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)
        
        # Add menu items
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        # Display a Message Box
        def _msgBox():
            msg.showinfo('Python Message Info Box', 'A Python GUI created by Tran Hung Thinh \n \tTo Do List - GUI')  
            
        # Add another Menu to the Menu Bar and an item
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=_msgBox)   # display messagebox when clicked
        menu_bar.add_cascade(label="Help", menu=help_menu)
        
        self.win.iconbitmap('todolist.ico')
                
        self.tasks = []

        self.txt_input = tk.Entry(mighty5, width=60)
        self.txt_input.grid(row=1,padx=5,pady=10)
        create_ToolTip(self.txt_input,'Input your task here')

        number_h = tk.StringVar()
        self.number_hour = ttk.Combobox(mighty8, width= 10,textvariable=number_h, state='readonly')
        self.number_hour['values'] = (1,2,3,4,5,6,7,8,9,10,11,12)
        self.number_hour.grid(row=2,column=0,padx=5,pady=10)
        self.number_hour.current(0)
        create_ToolTip(self.number_hour,'Choose hour')

        self.minute = tk.StringVar()
        self.txt_input_number_minute = tk.Entry(mighty8, width=14,textvariable=self.minute)
        self.txt_input_number_minute.grid(row=2,column=1,padx=5,pady=10)
        create_ToolTip(self.txt_input_number_minute,'Input minutes')
        
        number_ch = tk.StringVar()
        self.number_chosen = ttk.Combobox(mighty8, width=10, textvariable=number_ch, state='readonly')
        self.number_chosen['values'] = ('AM',"PM")
        self.number_chosen.grid(row=2,column=2,padx=5,pady=10)
        self.number_chosen.current(0)
        create_ToolTip(self.number_chosen,'Choose AM or PM')

        self.display = Label(mighty4, text = "", bg='white')
        self.display.grid(row=3,column=1,padx=10,pady=10)


        self.day = tk.StringVar()
        self.input_day = tk.Entry(mighty9, width=13,textvariable=self.day)
        self.input_day.grid(row=0,column=0,padx=5,pady=10)
        create_ToolTip(self.input_day,'Input day')

        number_m = tk.StringVar()
        self.number_month = ttk.Combobox(mighty9, width= 10,textvariable=number_m, state='readonly')
        self.number_month['values'] = (1,2,3,4,5,6,7,8,9,10,11,12)
        self.number_month.grid(row=0,column=1,padx=5,pady=10)
        self.number_month.current(0)
        create_ToolTip(self.number_month,'Choose month')

        self.year = tk.StringVar()
        self.input_year = tk.Entry(mighty9, width=13,textvariable=self.year)
        self.input_year.grid(row=0,column=2,padx=5,pady=10)
        create_ToolTip(self.input_year,'Input year')

        self.btn_add_task = tk.Button(mighty3, text = "[+]  |  Add Task", fg = 'black', bg = "Lightgreen",width=20, command = self.add_task)
        self.btn_add_task.grid(row=1,column=0,padx=5,pady=5)
        create_ToolTip(self.btn_add_task,'Input your task and click here to add list')


        self.btn_delete = tk.Button(mighty3, text = "[-]  |  Delete", fg = 'black', bg = "#D94A56", width=20,command = self.delete)
        self.btn_delete.grid(row=2,column=0,padx=5,pady=5)
        create_ToolTip(self.btn_delete,'Choose a task to delete and click here')

        self.btn_delete_all = tk.Button(mighty3, text = "[-]  |  Delete All", fg = 'black', bg = "#D94A56", width=20,command = self.delete_all)
        self.btn_delete_all.grid(row=3,column=0,padx=5,pady=5)
        create_ToolTip(self.btn_delete_all,'Delete all current task')


        self.btn_choose_random = tk.Button(mighty3, text = "[#]  |  Choose Random", fg = 'black', bg = "#f5af19", width=20, command = self.choose_random)
        self.btn_choose_random.grid(row=4,column=0,padx=5,pady=5)
        create_ToolTip(self.btn_choose_random,'Choose random your task')

        self.btn_number_of_task = tk.Button(mighty3, text = "[≣]  |  Number of Tasks", fg = 'black', bg = "#f5af19", width=20, command = self.number_of_task)
        self.btn_number_of_task.grid(row=5,column=0,padx=5,pady=5)
        create_ToolTip(self.btn_number_of_task,'Show your current number of task')

        self.btn_save = tk.Button(mighty3, text = "[✔]  |  Save tasks", fg = 'black', bg = "#00FFFF", width=20, command = self.save)
        self.btn_save.grid(row=6,column=0,padx=5,pady=5)
        create_ToolTip(self.btn_save,'Save your current tasks')

        self.btn_load = tk.Button(mighty3, text = "[⟳]  |  Load tasks", fg = 'black', bg = "#00FFFF", width=20, command = self.load_task)
        self.btn_load.grid(row=7,column=0,padx=5,pady=5)
        create_ToolTip(self.btn_load,'Load your tasks you had saved before')


        self.lb_tasks = tk.Listbox(mighty4,width=60,height=15)
        self.lb_tasks.grid(row=4,column=1,rowspan=7)
        

#####################

        self.btn_delete_all_tab2 = tk.Button(mighty7, text = "[-]  |  Delete All", fg = 'black', bg = "#D94A56", width= 20,command = self.clear_listbox_tab2)
        self.btn_delete_all_tab2.grid(row=3,column=0)
        create_ToolTip(self.btn_delete_all_tab2,'Delete all history of tasks')

        self.lb_tasks_tab2 = tk.Listbox(mighty6,width=70,height=15)
        self.lb_tasks_tab2.pack(padx=20,pady=20,fill=BOTH, expand=True)

         
#======================
# Start GUI
#======================
oop = OOP()
oop.win.mainloop()
