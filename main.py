from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class LoginScreen(GridLayout):
	def __init__(self, **var_args):
		super(LoginScreen, self).__init__(**var_args)
		self.cols = 2
		self.padding = [50, 50, 50, 50]
		self.spacing = [20, 20]

		# Change window color
		Window.clearcolor = (0.2, 0.2, 0.2, 1)

		# User Name
		self.add_widget(Label(text='User Name', color=(1, 1, 1, 1), font_size=18, size_hint=(None, None), height=30, width=150))
		self.username = TextInput(multiline=False, background_color=(0.3, 0.3, 0.3, 1), foreground_color=(1, 1, 1, 1), font_size=18, height=30, size_hint=(None, None), width=200)
		self.add_widget(self.username)

		# Password
		self.add_widget(Label(text='Password', color=(1, 1, 1, 1), font_size=18, size_hint=(None, None), height=30, width=150))
		self.password = TextInput(password=True, multiline=False, background_color=(0.3, 0.3, 0.3, 1), foreground_color=(1, 1, 1, 1), font_size=18, height=30, size_hint=(None, None), width=200)
		self.add_widget(self.password)

		# Confirm Password
		self.add_widget(Label(text='Confirm Password', color=(1, 1, 1, 1), font_size=18, size_hint=(None, None), height=30, width=150))
		self.confirm_password = TextInput(password=True, multiline=False, background_color=(0.3, 0.3, 0.3, 1), foreground_color=(1, 1, 1, 1), font_size=18, height=30, size_hint=(None, None), width=200)
		self.add_widget(self.confirm_password)

		# Submit button
		submit_btn = Button(text="Submit", size_hint=(1, 0.5), background_color=(0.1, 0.5, 0.8, 1), font_size=18, color=(1, 1, 1, 1))
		submit_btn.bind(on_press=self.on_submit)
		self.add_widget(submit_btn)
		self.add_widget(Label())  # Empty label to fill the second column of the last row

	def on_submit(self, instance):
		app = App.get_running_app()
		app.root.current = 'welcome'

class WelcomeScreen(GridLayout):
	def __init__(self, **var_args):
		super(WelcomeScreen, self).__init__(**var_args)
		self.cols = 1
		self.add_widget(Label(text='Welcome!', font_size=50))

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
