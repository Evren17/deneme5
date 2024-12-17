from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    pass

Window.size = (450, 800) 

class Slope(MDApp):
    BPoppins = "app\ifont\poppins_bold.ttf"
    
    logo_image = "app\image\PickFlick.png"  
    kapak_image ="app\image\kapaks.png"    
       
    def build(self):
        Builder.load_file("app\iscreen\main.kv") 


        sm= ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.current = 'main'
        return sm


if __name__ =="__main__":
    Slope().run()
    