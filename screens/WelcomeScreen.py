import tkinter as tk

class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.initUI()

    def initUI(self):
        # Welcome Label
        self.welcome_label = tk.Label(self, font=("Arial", 20))
        self.welcome_label.place(relx=0.5, rely=0.4, anchor="center")

        # Button to go to TaskScreen
        task_button = tk.Button(self, text="Go to Task Screen", command=lambda: self.controller.show_frame("TaskScreen"))
        task_button.place(relx=0.2, rely=0.6, anchor="center")
        
        score_page_button = tk.Button(self, text="Go to Scores Screen", command=lambda:self.controller.show_frame("ScoreScreen"))
        score_page_button.place(relx=0.6, rely=0.6, anchor="center")

    def tkraise(self):
        self.welcome_label.config(text=f"Bienvenue {self.controller.current_user} dans l'application!")
        super().tkraise()