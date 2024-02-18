import tkinter as tk
from tkinter import ttk
from API import databaseAPI

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.db = databaseAPI()
        self.create_widgets()

    def create_widgets(self):
        self.row_count_button = tk.Button(self)
        self.row_count_button["text"] = "Get row count"
        self.row_count_button["command"] = self.update_row_count
        self.row_count_button.pack(side="top")

        self.row_count_label = tk.Label(self)
        self.row_count_label.pack(side="top")

        self.names_button = tk.Button(self)
        self.names_button["text"] = "Get names"
        self.names_button["command"] = self.update_names
        self.names_button.pack(side="top")

        self.tree = ttk.Treeview(self, show='headings', height=20)
        self.tree["columns"]=("zero", "one","two")
        self.tree.column("zero", width=50, stretch=tk.NO)
        self.tree.column("one", width=100, stretch=tk.NO)
        self.tree.column("two", width=100)
        self.tree.heading("zero", text="No.",anchor=tk.W)
        self.tree.heading("one", text="First name",anchor=tk.W)
        self.tree.heading("two", text="Last name",anchor=tk.W)
        self.tree.pack(side='left', fill='y')

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side='left', fill='y')

        self.tree.configure(yscrollcommand=self.scrollbar.set)

    def update_row_count(self):
        row_count = self.db.get_rows("in450a")
        self.row_count_label["text"] = f"Rows in in450a: {row_count}"

    def update_names(self):
        names = self.db.get_names("in450b")
        for i, (first_name, last_name) in enumerate(names):
            self.tree.insert("", "end", values=(i+1, first_name, last_name))

root = tk.Tk()
root.title("IN450")
root.geometry("500x600")
app = Application(master=root)
app.mainloop()