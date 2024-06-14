import tkinter as tk

class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.initUI()

    def initUI(self):
        # Welcome Label
        welcome_label = tk.Label(self, text="Welcome to the Application!", font=("Arial", 20))
        welcome_label.place(relx=0.5, rely=0.4, anchor="center")

        # Button to go to TaskScreen
        task_button = tk.Button(self, text="Go to Task Screen", command=lambda: self.controller.show_frame("TaskScreen"))
        task_button.place(relx=0.5, rely=0.6, anchor="center")
