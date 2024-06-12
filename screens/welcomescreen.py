from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.app import App

class WelcomeScreen(BoxLayout):
	def __init__(self, **var_args):
		super(WelcomeScreen, self).__init__(**var_args)
		self.orientation = 'vertical'
		self.padding = [50, 50, 50, 50]
		self.spacing = 20
		self.size_hint = (None, None)
		self.width = 400
		self.height = 300
		self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		self.app = App.get_running_app()

		# Center content in the window
		content_layout = BoxLayout(orientation='vertical', size_hint=(None, None), width=400, height=300)
		content_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

		welcome_message = self.get_welcome_message()
		welcome_label = Label(text=welcome_message, size_hint=(None, None), height=50, width=400)
		content_layout.add_widget(welcome_label)
  
		# Buttons for Hannes and Leo
		button_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), height=60, width=400, spacing=20)
		hannes_btn = Button(text="Hannes", background_color=(1, 0.4, 0.7, 1), size_hint=(None, None), width=300, height=400)
		hannes_btn.bind(on_press=self.show_hannes_message)
		button_layout.add_widget(hannes_btn)

		leo_btn = Button(text="Leo", background_color=(0.4, 0.6, 1, 1), size_hint=(None, None), width=300, height=400)
		leo_btn.bind(on_press=self.show_leo_message)
		button_layout.add_widget(leo_btn)

		content_layout.add_widget(button_layout)
		self.add_widget(content_layout)

	def show_hannes_message(self, instance):
		popup = Popup(title='Message', content=Label(text='Pedophile Sau'), size_hint=(None, None), size=(300, 200))
		popup.open()

	def show_leo_message(self, instance):
		popup = Popup(title='Message', content=Label(text='Herscher der Welt'), size_hint=(None, None), size=(300, 200))
		popup.open()

	def get_welcome_message(self):
		username = self.app.username
		messages = {
				'user': "Welcome, User! Glad to see you again.",
				'user2': "Hello, User2! Welcome back.",
		}
		return messages.get(username, "Welcome!")