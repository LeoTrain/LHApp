import tkinter as tk
from screens.LoginScreen import LoginScreen
from screens.WelcomeScreen import WelcomeScreen
from screens.TaskScreen import TaskScreen
from screens.ScoreScreen import ScoreScreen

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Stacked Widget Example")
        self.geometry("1080x720")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        self.current_user = None

        self.frames = {}
        for F in (LoginScreen, WelcomeScreen, TaskScreen, ScoreScreen):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("LoginScreen")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
