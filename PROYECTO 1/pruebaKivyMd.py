from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.font_definitions import theme_font_styles


#------Themes--------
#Red, Pink, Purple, DeepPurple, Indigo
#Blue, LightBlue, Cyan, Teal, Green
#LightGreen, Lime, Yellow, Amber, Orange,
#Brown, Gray, BlueGray

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file('textFieldEj.kv')    
    
    
MainApp().run()