from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file('main.kv')

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

class WelcomeScreen(Screen):
    def on_enter(self):
        app = App.get_running_app()
        username = app.username
        welcome_message = self.get_welcome_message(username)
        self.ids.welcome_label.text = welcome_message

    def get_welcome_message(self, username):
        messages = {
            'leo': "Salut bg, bien de te retrouver !",
            'hannes': "Hallo du Schwuchtl, bis später !",
        }
        return messages.get(username, "Welcome!")

    def show_hannes_message(self):
        popup = Popup(title='Message', content=Label(text='Pedophile Sau'), size_hint=(None, None), size=(300, 200))
        popup.open()

    def show_leo_message(self):
        popup = Popup(title='Message', content=Label(text='Herscher der Welt'), size_hint=(None, None), size=(300, 200))
        popup.open()

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(WelcomeScreen(name='welcome'))
        return sm

if __name__ == '__main__':
    TestApp().run()
