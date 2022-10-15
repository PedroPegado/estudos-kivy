from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("screen.kv")

class SplashScreen(App):
    def build(self):
        return GUI


if __name__ == "__main__":
    SplashScreen().run()
