from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class LoginScreen(BoxLayout):
	def __init__(self, **var_args):
		super(LoginScreen, self).__init__(**var_args)
		self.orientation = 'vertical'
		self.padding = [50, 50, 50, 50]
		self.spacing = 20
		self.size_hint = (None, None)
		self.width = 400
		self.height = 300
		self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

		# Change window color
		Window.clearcolor = (0.2, 0.2, 0.2, 1)

		# Grid layout for text and inputs
		grid_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
		grid_layout.bind(minimum_height=grid_layout.setter('height'))

		# User Name
		grid_layout.add_widget(Label(text='User Name', color=(1, 1, 1, 1), font_size=18, size_hint_y=None, height=30, width=150))
		self.username = TextInput(multiline=False, background_color=(0.3, 0.3, 0.3, 1), foreground_color=(1, 1, 1, 1), font_size=18, size_hint_y=None, height=40, width=200)
		grid_layout.add_widget(self.username)

		# Password
		grid_layout.add_widget(Label(text='Password', color=(1, 1, 1, 1), font_size=18, size_hint_y=None, height=30, width=150))
		self.password = TextInput(password=True, multiline=False, background_color=(0.3, 0.3, 0.3, 1), foreground_color=(1, 1, 1, 1), font_size=18, size_hint_y=None, height=40, width=200)
		grid_layout.add_widget(self.password)

		# Confirm Password
		grid_layout.add_widget(Label(text='Confirm Password', color=(1, 1, 1, 1), font_size=18, size_hint_y=None, height=30, width=150))
		self.confirm_password = TextInput(password=True, multiline=False, background_color=(0.3, 0.3, 0.3, 1), foreground_color=(1, 1, 1, 1), font_size=18, size_hint_y=None, height=40, width=200)
		grid_layout.add_widget(self.confirm_password)

		# Add grid layout to the main layout
		self.add_widget(grid_layout)

		# Empty space
		self.add_widget(BoxLayout(size_hint_y=None, height=20))

		# Submit button centered
		submit_btn = Button(text="Submit", size_hint=(None, None), width=200, height=50, background_color=(0.1, 0.5, 0.8, 1), font_size=18, color=(1, 1, 1, 1))
		submit_btn.bind(on_press=self.on_submit)
		self.add_widget(submit_btn)

	def on_submit(self, instance):
		app = App.get_running_app()
		app.root.current = 'welcome'

class WelcomeScreen(BoxLayout):
	def __init__(self, **var_args):
		super(WelcomeScreen, self).__init__(**var_args)
		self.orientation = 'vertical'
		self.add_widget(Label(text='Welcome!', font_size=50, size_hint=(None, None), height=100))
		self.padding = [50, 50, 50, 50]
		self.spacing = 20
		self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

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
