import tkinter as tk

class TaskScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.initUI()

    def initUI(self):
        # Task Label
        task_label = tk.Label(self, text="Tasks", font=("Arial", 20))
        task_label.place(relx=0.5, rely=0.4, anchor="center")

        # Button to return to WelcomeScreen
        back_button = tk.Button(self, text="Back to Welcome Screen", command=lambda: self.controller.show_frame("WelcomeScreen"))
        back_button.place(relx=0.5, rely=0.6, anchor="center")
