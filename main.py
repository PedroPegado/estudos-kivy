#from kivy.app import App
#from kivy.lang import Builder

#GUI = Builder.load_file("screen.#kv")

#class SplashScreen(App):
#    def build(self):
#        return GUI


#if __name__ == "__main__":
#    SplashScreen().run()
from kivymd.app import MDApp
from kivy.lang import Builder

GUI = Builder.load_file("screen.kv")

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.title = 'Appzinho Pika'
        return GUI

MyApp().run()
