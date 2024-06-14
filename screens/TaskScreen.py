import tkinter as tk
from tkinter import ttk

class TaskScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.configure(bg="#f0f0f0")  # Background color

        # Define a style for labels and buttons
        style = ttk.Style()
        style.configure(
            "TButton",
            foreground="white",
            background="#8B4513",
            font=("Arial", 12, "bold"),
            borderwidth=0
        )
        style.map(
            "TButton",
            background=[('active', '#A0522D')]  # Sienna active background color
        )
        style.configure(
            "TLabel",
            background="#f0f0f0",
            foreground="#f0f0f0",
            font=("Arial", 20)
        )

        # Task Label
        task_label = ttk.Label(self, text="Aufgaben", style="TLabel")
        task_label.place(relx=0.5, rely=0.1, anchor="center")

        # Treeview for displaying tasks
        self.tree = ttk.Treeview(self, columns=("Task", "Status"), show="headings")
        self.tree.heading("Task", text="Aufgabe")
        self.tree.heading("Status", text="Status")
        self.tree.column("Task", width=200)
        self.tree.column("Status", width=100)
        self.tree.place(relx=0.5, rely=0.5, anchor="center", width=300, height=200)

        # Button to return to WelcomeScreen
        back_button = ttk.Button(self, text="Zurück zum Willkommen Bildschirm", command=lambda: self.controller.show_frame("WelcomeScreen"), style="TButton")
        back_button.place(relx=0.5, rely=0.9, anchor="center")

    def load_tasks(self):
        # Clear the current tasks
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Load tasks for the current user
        tasks = self.get_tasks_for_user(self.controller.current_user)
        for task, status in tasks:
            self.tree.insert("", "end", values=(task, status))

    def get_tasks_for_user(self, username):
        sample_tasks = {
            "admin": [("Task A", "Erledigt"), ("Task B", "Nicht Erledigt")],
            "ftleo": [("Task A", "Erledigt"), ("Task B", "Erledigt")],
            "hns_hpstr": [("Task A", "Nicht Erledigt"), ("Task B", "Nicht Erledigt")]
        }
        return sample_tasks.get(username, [])

    def tkraise(self):
        self.load_tasks()
        super().tkraise()

