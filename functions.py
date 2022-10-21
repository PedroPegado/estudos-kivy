from kivy.clock import Clock, mainthread
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable


def callbackregister(self, *args):
    MDApp.get_running_app().root.current = 'login'

def callbacklogin(self, *args):
  MDApp.get_running_app().root.current = 'dashboard'