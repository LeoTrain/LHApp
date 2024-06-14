import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.initUI()

    def initUI(self):
        # Application Image
        image = Image.open("logo.png")
        image = image.resize((150, 150), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(image)
        app_image = tk.Label(self, image=self.image)
        app_image.place(relx=0.5, rely=0.3, anchor="center")

        # Username Label and Entry
        username_label = tk.Label(self, text="Username")
        username_label.place(relx=0.32, rely=0.65, anchor="e")
        self.username_entry = tk.Entry(self)
        self.username_entry.place(relx=0.35, rely=0.65, anchor="w")

        # Password Label and Entry
        password_label = tk.Label(self, text="Password")
        password_label.place(relx=0.32, rely=0.75, anchor="e")
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.place(relx=0.35, rely=0.75, anchor="w")

        # Login Button
        login_button = tk.Button(self, text="Login", command=self.check_login)
        login_button.place(relx=0.5, rely=0.9, anchor="center")

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "root":  # Replace with actual validation logic
            self.controller.current_user = username
            self.controller.show_frame("WelcomeScreen")
        else:
            messagebox.showerror("Login Error", "Incorrect Username or Password")
