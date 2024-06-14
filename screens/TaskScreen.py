import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import csv

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
        self.tree = ttk.Treeview(self, columns=("Task", "Status", "Points"), show="headings")
        self.tree.heading("Task", text="Aufgabe")
        self.tree.heading("Status", text="Erledigt")
        self.tree.heading("Points", text="Punkte")
        self.tree.column("Task", width=100, anchor="center")
        self.tree.column("Status", width=50, anchor="center")
        self.tree.column("Points", width=50, anchor="center")
        
        self.tree.place(relx=0.5, rely=0.5, anchor="center", width=250, height=200)

        new_task_button = ttk.Button(self, text="Neue Aufgabe", command=lambda: self.create_new_task(), style="TButton")
        new_task_button.place(relx=0.3, rely=0.9, anchor="center")
        
        # Button to return to WelcomeScreen
        back_button = ttk.Button(self, text="Zurück zum Willkommen Bildschirm", command=lambda: self.controller.show_frame("WelcomeScreen"), style="TButton")
        back_button.place(relx=0.7, rely=0.9, anchor="center")

        self.file_path = "data/user_tasks.txt"
        
    def create_new_task(self):
        new_task = simpledialog.askstring("Input", "Neue Aufgabe:",
                                    parent=self.controller)
        
        if new_task:            
            with open(self.file_path, 'r') as file:
                lines = file.readlines()

            username_found = False
            for i, line in enumerate(lines):
                if self.controller.current_user in line:
                    lines[i] = line.strip() + f", {new_task}\n"
                    username_found = True
                    break
            
            if not username_found:
                lines.append(f"{self.controller.current_user}: {new_task}\n")
            
            with open(self.file_path, 'w') as file:
                file.writelines(lines)
            
            messagebox.showinfo("Success", "Aufgabe hinzugefügt")

            self.load_tasks()

    def load_tasks(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            if line.startswith(f"{self.controller.current_user}:"):
                tasks = line.split(": ")[1].strip().split(", ")
                for task in tasks:
                    self.tree.insert("", "end", values=(task, "\u2713", "1"))

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

