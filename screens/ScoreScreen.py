import csv
import tkinter as tk
from tkinter import ttk

class ScoreScreen(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.initUI()

  def initUI(self):
    self.configure(bg="#f0f0f0")  # Background color

    # Title Label
    title_label = ttk.Label(self, text="Benutzer-Scores", font=("Arial", 20), background="#f0f0f0", foreground="#333333")
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # Style for Treeview
    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Arial', 11))  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Arial', 13, 'bold'))  # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove borders

    # Treeview for displaying user scores
    self.tree = ttk.Treeview(self, columns=("Nutzer", "Score"), show="headings", style="mystyle.Treeview")
    self.tree.heading("Nutzer", text="Nutzer")
    self.tree.heading("Score", text="Score")

    # Adjust the column widths
    self.tree.column("Nutzer", width=200)
    self.tree.column("Score", width=50)

    self.tree.place(relx=0.5, rely=0.5, anchor="center", width=300, height=200)

    # Load data from CSV
    self.load_data()

    # Button to return to WelcomeScreen
    back_button = ttk.Button(self, text="Zurück zum Willkommen Bildschirm", command=lambda: self.controller.show_frame("WelcomeScreen"))
    back_button.place(relx=0.5, rely=0.9, anchor="center")

  def load_data(self):
    with open("data/user_data.csv", newline='') as file:
        reader = csv.DictReader(file)
        users_scores = [(row['username'], int(row['score'])) for row in reader]

    for user, score in users_scores:
        self.tree.insert("", "end", values=(user, score))