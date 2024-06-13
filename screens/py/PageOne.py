from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label

Builder.load_file('screens/kv/PageOne.kv')

class PageOne(Screen):
    window_width = NumericProperty(Window.width)
    window_height = NumericProperty(Window.height)

    def add_task(self):
        task_name = self.ids.task_input.text
        if task_name:
            task = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
            task.add_widget(Label(text=task_name))
            remove_button = Button(text='Remove', size_hint_y=None, height=50, size_hint_x=None, width=100)
            remove_button.bind(on_release=lambda x: self.remove_task(task))
            task.add_widget(remove_button)
            self.ids.task_list.add_widget(task)
            self.ids.task_list.height = self.ids.task_list.minimum_height
            self.ids.task_input.text = ''

    def remove_task(self, task):
        self.ids.task_list.remove_widget(task)
        self.ids.task_list.height = self.ids.task_list.minimum_height
