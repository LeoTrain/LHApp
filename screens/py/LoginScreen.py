from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder

Builder.load_file('screens/kv/LoginScreen.kv')

class LoginScreen(Screen):
    def on_submit(self, username, password):
        if self.check_credentials(username=username, password=password):
            app = App.get_running_app()
            app.username = username
            self.manager.current = 'welcome'
        else:
            popup = Popup(title='Error', content=Label(text='Wrong username or password, try again.'), size_hint=(None, None), size=(300, 200))
            popup.open()

    def check_credentials(self, username, password):
        credentials = self.load_credentials("data/credentials.txt")
        return credentials.get(username) == password
    
    def load_credentials(self, file_path):
        credentials = {}
        with open(file_path, 'r') as file:
            for line in file:
                user, pwd = line.strip().split(',')
                credentials[user] = pwd
        return credentials