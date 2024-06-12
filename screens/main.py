from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from loginscreen import LoginScreen
from welcomescreen import WelcomeScreen

class MyApp(App):
	def build(self):
		sm = ScreenManager()
		login_screen = Screen(name='login')
		login_screen.add_widget(LoginScreen())
		sm.add_widget(login_screen)

		welcome_screen = Screen(name='welcome')
		welcome_screen.add_widget(WelcomeScreen())
		sm.add_widget(welcome_screen)

		return sm
if __name__ == '__main__':
	MyApp().run()
