from os import walk
import os.path
from tkinter import *
import ntpath
import pyperclip
import io
import sys

def fetch_lists(path):
    lists = {}
    for (dirpath, dirnames, filenames) in walk(path):
        for filename in filenames:
            file = os.path.join(dirpath, filename)
            f = io.open(file, 'r', encoding='utf-8')
            lists[file] = f.read()
            f.close()

    return lists

class Application(Frame):
    def __init__(self, master=None, path='../Lists'):
        Frame.__init__(self, master)
        self.master = master
        self.master.title('Skribbl List Creator')
        self.lists = fetch_lists(path)
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.list_selection_frame = LabelFrame(self, text='List Selection')
        self.list_selection_frame.grid(row=0, column=0, sticky='nesw')
        self.generated_list_frame = LabelFrame(self, text='Generated List')
        self.generated_list_frame.grid(row=0, column=1, sticky='nesw')
        
        self.list_select_all_widget = Checkbutton(self.list_selection_frame, text='All', command=self.select_all_cb)
        self.list_select_all_widget.val = IntVar()
        self.list_select_all_widget.config(variable=self.list_select_all_widget.val)
        self.list_select_all_widget.grid(row=0, sticky=W)
        
        self.list_selection_widgets = []
        for i, list_name in enumerate(self.lists.keys()):
            w = Checkbutton(self.list_selection_frame, text=ntpath.basename(list_name), command=self.select_list_cb)
            w.val = IntVar()
            w.config(variable=w.val)
            w.grid(row=i+1, sticky=W)
            w.list = list_name
            self.list_selection_widgets.append(w)
        
        self.create_list_widget = Button(self.list_selection_frame, text='Generate List', command=self.generate_list)
        self.create_list_widget.grid(row=(len(self.list_selection_widgets)+1))
        
        self.generated_list_scrollbar = Scrollbar(self.generated_list_frame)
        self.generated_list_scrollbar.grid(row=0, column=1, sticky='ns')
        self.generate_list_widget = Text(self.generated_list_frame)
        self.generate_list_widget.grid(row=0, column=0, sticky='nesw')
        self.generated_list_scrollbar.config(command=self.generate_list_widget.yview)
        self.generate_list_widget.config(yscrollcommand=self.generated_list_scrollbar.set)
        
        self.copy_list_widget = Button(self.generated_list_frame, text='Copy List to Clipboard', command=self.copy_generated_list)
        self.copy_list_widget.grid(row=1, columnspan=2, sticky='s')
    
    def select_all_cb(self):
        if self.list_select_all_widget.val.get():
            for w in self.list_selection_widgets:
                w.select()
        else:
            for w in self.list_selection_widgets:
                w.deselect()
    
    def select_list_cb(self):
        all_selected = True
        for w in self.list_selection_widgets:
            all_selected = all_selected and w.val.get()
        if all_selected:
            self.list_select_all_widget.val.set(1)
        else:
            self.list_select_all_widget.val.set(0)

    def generate_list(self):
        list = ''
        for w in self.list_selection_widgets:
            if w.val.get():
                list += self.lists[w.list]
        
        self.generate_list_widget.delete('1.0', END)
        self.generate_list_widget.insert(INSERT, list)
    
    def copy_generated_list(self):
        pyperclip.copy(self.generate_list_widget.get("1.0", END))
        

def main_loop(path):
    root = Tk()
    app = Application(master=root, path=path)
    while True:
        try:
            app.update_idletasks()
            app.update()
        except:
            break

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    else:
        path = '../Lists'
    
    try:
        main_loop(path)
    except KeyboardInterrupt:
        pass