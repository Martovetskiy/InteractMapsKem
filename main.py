from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from myFirebase import myFirebase
Window.size = (480, 800)
Window.clearcolor = (1, 1, 1, 1)



class ScreenManager(ScreenManager):
    pass

class LoginScreen(Screen):
    pass
class LoginScreen1(Screen):
    pass

class Mapsi(Screen):
    pass

class MainScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class main(App):
    def build(self):
        self.my_firebase = myFirebase()
        return ScreenManager()

if __name__ == '__main__':
    main().run()