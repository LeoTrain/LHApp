from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder

Builder.load_file('screens/kv/WelcomeScreen.kv')

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
        
    def go_to_page(self):
        app = App.get_running_app()
        self.manager.current = 'page one'
    
