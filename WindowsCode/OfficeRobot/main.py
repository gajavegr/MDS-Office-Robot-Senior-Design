import kivy
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.graphics import Ellipse
from kivy.graphics import RoundedRectangle
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.config import Config
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.config import Config
Config.set('graphics', 'resizable', True)


class Canvas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            #self.img = Image(source = "officeLayout.PNG", size=(1000,1000), pos=(300,-80))
            self.ellipse = Ellipse(pos=(200,500), size=(30,30), background_color='black')
            """
            self.button_up = Button(size=(50,50),
                                    pos=(50,100),
                                    text="Up",
                                    background_color = 'white')
            self.button_down = Button(size=(50, 50),
                                    pos=(50, 0),
                                    text="Down",
                                    background_color='white')
            self.button_left = Button(size=(50, 50),
                                      pos=(0, 50),
                                      text="Left",
                                      background_color='white')
            self.button_right = Button(size=(50, 50),
                                      pos=(100, 50),
                                      text="Right",
                                      background_color='white')
            """
            self._keyboard = Window.request_keyboard(self.press, self)
            self._keyboard.bind(on_key_down=self.press)
            #self.roomLabel_1 = Label(text="Interview Room \n272", font_size ='20sp',pos = (200,600),color = 'black')



    def goTo272(self):
        self.ellipse.pos = (500,500)
        print("Go to office 272")

    def press(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            x, y = self.ellipse.pos
            w, h = self.ellipse.size
            inc = dp(10)
            diff = self.width - (x + w)
            if diff < inc:
                inc = diff
            if(x>=200): x-=inc
            self.ellipse.pos = (x, y)

        if keycode[1] == 'right':
            x, y = self.ellipse.pos
            w, h = self.ellipse.size
            inc = dp(10)
            diff = self.width - (x + w)
            if diff < inc:
                inc = diff
            if (x <= 1300): x += inc
            self.ellipse.pos = (x, y)

        if keycode[1] == 'up':
            x, y = self.ellipse.pos
            w, h = self.ellipse.size
            inc = dp(10)
            diff = self.width - (x + w)
            if diff < inc:
                inc = diff
            if (y <= 700): y+=inc
            print("up has been pressed")
            print(y)
            self.ellipse.pos = (x, y)
        if keycode[1] == 'down':
            x, y = self.ellipse.pos
            w, h = self.ellipse.size
            inc = dp(10)
            diff = self.width - (x + w)
            if diff < inc:
                inc = diff
            if (y >= 100): y -= inc
            print("up has been pressed")
            print(y)
            self.ellipse.pos = (x, y)
            # print(self.y);
        return True

    def on_button_a_click(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        diff = self.width - (x + w)
        if diff < inc:
            inc = diff
        x += inc
        self.rect.pos = (x, y)


class MyApp(App):
    def build(self):
        Window.clearcolor = (0.7,0.7,0.7,1)
        Window.fullscreen = 'auto'
        return Canvas()

if __name__ == "__main__":
        MyApp().run()

