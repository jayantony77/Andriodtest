from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from SecondScreenpy import SecondScreen


Window.size = (330,600)

Builder.load_file("FirstScreen.kv")
Builder.load_file("SecondScreen.kv")


class FirstScreen(MDScreen):
    pass


class FirstScreen1(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='firstScreen'))
        sm.add_widget(SecondScreen(name='secondScreen'))
        return sm


    def on_press(self):
        print("clicking the listitems")


FirstScreen1().run()