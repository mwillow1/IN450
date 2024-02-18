import tkinter as tk
from tkinter import ttk, messagebox
from API import databaseAPI

class LoginPage(tk.Frame):
    def __init__(self, master=None, login_callback=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack(side="top")

        self.username_entry = tk.Entry(self)
        self.username_entry.pack(side="top")

        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack(side="top")

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(side="top")

        self.login_button = tk.Button(self)
        self.login_button["text"] = "Login"
        self.login_button["command"] = self.login
        self.login_button.pack(side="top")

        self.login_callback = login_callback

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.login_callback:
            success, db = self.login_callback(username, password)
            if success:
                self.master.db = db
                self.pack_forget()
                app = Application(master=self.master)
                app.pack()
            else:
                messagebox.showerror("Login failed", "Invalid username or password")

def login(username, password):
    db = databaseAPI(username, password)
    success = db.check_credentials(username, password)
    return success, db

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.db = master.db
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
        if row_count is None:
            self.row_count_label["text"] = "Unable to view data"
        else:
            self.row_count_label["text"] = f"Rows in in450a: {row_count}"

    def update_names(self):
        names = self.db.get_names("in450b")
        if names is None:
            messagebox.showerror("Error", "Unable to view data")
        else:
            for i, (first_name, last_name) in enumerate(names):
                self.tree.insert("", "end", values=(i+1, first_name, last_name))

root = tk.Tk()
root.title("Login")
root.geometry("800x800")
login_page = LoginPage(master=root, login_callback=login)
login_page.pack()
root.mainloop()