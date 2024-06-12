from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.py.LoginScreen import LoginScreen
from screens.py.WelcomeScreen import WelcomeScreen
from screens.py.PageOne import PageOne

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(PageOne(name='page one'))
        return sm

if __name__ == '__main__':
    MainApp().run()
