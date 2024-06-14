import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv

class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.configure(bg="#f0f0f0")  # Background color

        # Application Image
        image = Image.open("data/logo.png")
        image = image.resize((150, 150), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(image)
        app_image = tk.Label(self, image=self.image, bg="#f0f0f0")
        app_image.place(relx=0.5, rely=0.3, anchor="center")

        # Define styles for labels and buttons
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
            foreground="#333333",
            font=("Arial", 12)
        )

        # Username Label and Entry
        username_label = ttk.Label(self, text="Username", style="TLabel")
        username_label.place(relx=0.32, rely=0.65, anchor="e")
        self.username_entry = ttk.Entry(self)
        self.username_entry.place(relx=0.35, rely=0.65, anchor="w")

        # Password Label and Entry
        password_label = ttk.Label(self, text="Password", style="TLabel")
        password_label.place(relx=0.32, rely=0.75, anchor="e")
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.place(relx=0.35, rely=0.75, anchor="w")

        # Login Button
        login_button = ttk.Button(self, text="Login", command=self.check_login, style="TButton")
        login_button.place(relx=0.5, rely=0.9, anchor="center")
        
        # Bind Enter key to the login button
        self.bind_all("<Return>", self.on_enter_key)

    def on_enter_key(self, event):
        self.check_login()

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # CSV Datei lesen und username-password checken
        with open("data/user_data.csv", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username and row['password'] == password:
                    self.controller.current_user = username
                    self.controller.show_frame("WelcomeScreen")
                    return

        # Falls username oder password falsch sind
        messagebox.showerror("Login Fehler", "Falscher Benutzername oder Passwort")
