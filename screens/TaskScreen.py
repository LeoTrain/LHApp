import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox

class TaskScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.user_tasks = "data/user_tasks.txt"
        self.completed_tasks = "data/completed_tasks.txt"
        self.initUI()

    def initUI(self):
        self.configure(bg="#f0f0f0")

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
            background=[('active', '#A0522D')]
        )
        style.configure(
            "TLabel",
            background="#f0f0f0",
            foreground="#8B4513",
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
        self.tree.bind("<Button-1>", self.on_treeview_click)

        new_task_button = ttk.Button(self, text="Neue Aufgabe", command=self.create_new_task, style="TButton")
        new_task_button.place(relx=0.3, rely=0.9, anchor="center")
        
        back_button = ttk.Button(self, text="Zurück zum Willkommen Bildschirm", command=lambda: self.controller.show_frame("WelcomeScreen"), style="TButton")
        back_button.place(relx=0.7, rely=0.9, anchor="center")

    def create_new_task(self):
        new_task = simpledialog.askstring("Input", "Neue Aufgabe:", parent=self.controller)
        point_amount = simpledialog.askinteger("Input", "Punkteanzahl:", parent=self.controller)

        if new_task and point_amount is not None:
            with open(self.user_tasks, 'r') as file:
                lines = file.readlines()

            username_found = False
            for i, line in enumerate(lines):
                if self.controller.current_user in line:
                    lines[i] = line.strip() + f", {new_task}|{point_amount}\n"
                    username_found = True
                    break

            if not username_found:
                lines.append(f"{self.controller.current_user}: {new_task}|{point_amount}\n")

            with open(self.user_tasks, 'w') as file:
                file.writelines(lines)

            messagebox.showinfo("Success", "Aufgabe hinzugefügt")
            self.load_tasks()


    def load_tasks(self):
        self.tree.delete(*self.tree.get_children())
        try:
            with open(self.user_tasks, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            lines = []

        for line in lines:
            if ": " in line:
                username, tasks_str = line.split(": ", 1)
                if username == self.controller.current_user:
                    tasks = tasks_str.strip().split(", ")
                    for task_entry in tasks:
                        if "|" in task_entry:
                            task, points = task_entry.split("|")
                            if task.strip():
                                self.tree.insert("", "end", values=(task, " ", points))
                        else:
                            if task_entry.strip():
                                self.tree.insert("", "end", values=(task_entry, " ", "1"))


    def tkraise(self):
        self.load_tasks()
        super().tkraise()

    def on_treeview_click(self, event):
        region = self.tree.identify("region", event.x, event.y)
        if region == "cell":
            column = self.tree.identify_column(event.x)
            if column == "#2":
                item = self.tree.identify_row(event.y)
                self.toggle_task_status(item)
                self.load_tasks()

    def toggle_task_status(self, item):
        # Get current values
        current_values = self.tree.item(item, "values")
        task, status, points = current_values

        # Toggle status
        new_status = "\u2713" if status != "\u2713" else " "
        
        # Update the item in the treeview
        self.tree.item(item, values=(task, new_status, points))
        
        with open(self.user_tasks, 'r') as file:
            lines = file.readlines()
        
        with open(self.user_tasks, 'w') as file:
            for line in lines:
                if self.controller.current_user in line:
                    username, tasks_str = line.split(": ", 1)
                    tasks = tasks_str.strip().split(", ")
                    if task in tasks:
                        tasks.remove(task)
                    if tasks:  # If there are still tasks left
                        new_line = f"{self.controller.current_user}: {', '.join(tasks).strip()}\n"
                        file.write(new_line)
                    else:  # No tasks left, remove the line entirely
                        continue
                else:
                    file.write(line)
        
        if new_status == "\u2713":
            with open(self.completed_tasks, 'a') as file:
                file.write(f"{self.controller.current_user}: {task}\n")
        else:
            with open(self.completed_tasks, 'r') as file:
                lines = file.readlines()
            
            with open(self.completed_tasks, 'w') as file:
                for line in lines:
                    if f"{self.controller.current_user}: {task}" not in line:
                        file.write(line)


