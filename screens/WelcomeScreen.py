import tkinter as tk
from tkinter import ttk

class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.configure(bg="#f0f0f0")  # Background color

        # Welcome Label
        self.welcome_label = tk.Label(self, font=("Arial", 20), bg="#f0f0f0", fg="#333333")
        self.welcome_label.place(relx=0.5, rely=0.3, anchor="center")

        # Define a style for the buttons
        style = ttk.Style()
        style.configure(
            "TButton",
            foreground="white",
            font=("Arial", 12, "bold"),
            borderwidth=0
        )
        style.map(
            "TButton",
            background=[('active', '#A0522D')]  # Sienna active background color
        )

        # Button to go to TaskScreen
        task_button = ttk.Button(self, text="Go to Task Screen", command=lambda: self.controller.show_frame("TaskScreen"), style="TButton")
        task_button.place(relx=0.3, rely=0.6, anchor="center")
        
        # Button to go to Scores Screen
        score_page_button = ttk.Button(self, text="Go to Scores Screen", command=lambda: self.controller.show_frame("ScoreScreen"), style="TButton")
        score_page_button.place(relx=0.7, rely=0.6, anchor="center")

    def tkraise(self):
        self.welcome_label.config(text=f"Willkommen zurück {self.controller.current_user}!")
        super().tkraise()

