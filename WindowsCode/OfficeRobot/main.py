import threading
import kivy
from kivy.app import App
from kivy.metrics import dp
from kivy.graphics import Rectangle, Line
from kivy.graphics import Ellipse
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.config import Config

from SSHCommunication import SSHCommunication
import threading


Config.set('graphics', 'resizable', True)

class Canvas(Widget):



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.color_b = Color(0,0,0,1)
            Line(points=[980, 470, 980, 900], width=1.7, Color=self.color_b)
            Line(points=[99.5,300,99.5,200],width=1.7)
            Line(points=[1005, 130, 825, 130], width=1.7)
            Line(points=[670, 130, 720, 130], width=1.7)
            Line(points=[720, 130, 720, 80], width=1.7)
            Line(circle=(720, 130, 50, 90, 180),width=1.7)
            Line(circle=(823, 130, 50, 180, 270), width=1.7)
            Line(points=[825, 130, 825, 80], width=1.7)
            Line(points=[1150, 796, 1180, 796], width=2)
            Line(points=[1150, 860, 1180, 860], width=2)

            self.color_w = Color(1,1,1,1)
            #self.img = Image(source = "officeLayout.PNG", size=(1000,1000), pos=(300,-80))
            self.ellipse = Ellipse(pos=(100,240), size=(30,30), Color = self.color_w)
            Ellipse(pos=(650, 734), size=(30, 30), Color=self.color_w)

            self.color_g = Color(0.4,1,0,1)
            Ellipse(pos=(650,785),size=(30,30),Color=self.color_g)

            self.color_r = Color(0.6, 0.1, 0, 1)
            Ellipse(pos=(650, 683), size=(30, 30), Color=self.color_r)

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
            
            # self.host = "gajavegr-pi.wlan.rose-hulman.edu"
            # self.port = 22
            # self.username = "pi"
            # self.password = "password"
            # self.sshConn = SSHCommunication(username=self.username,password=self.password,host=self.host,port=self.port)
            self.sshConn = SSHCommunication()


    def goTo272(self):
        newX = 190
        newY = 300
        self.ellipse.pos = (newX,newY)
        print("Go to interview room 272")
        self.communicateDestination(newX,newY)
        # t1 = threading.Thread(target=self.communicateDestination, args=(newX,newY,))
        # t1.start()
        # t1.join()

    def goTo273(self):
        newX = 420
        newY = 300
        self.ellipse.pos = (newX,newY)
        print("Go to office 273")
        self.communicateDestination(newX,newY)
        # t2 = threading.Thread(target=self.communicateDestination, args=(newX,newY,))
        # t2.start()
        # t2.join()

    def goTo266A(self):
        newX = 640
        newY = 260
        self.ellipse.pos = (newX,newY)
        print("Go to work station 266A")
        self.communicateDestination(newX,newY)

    def goTo266B(self):
        newX = 990
        newY = 450
        self.ellipse.pos = (newX,newY)
        print("Go to work roon 266B")
        self.communicateDestination(newX,newY)

    def goTo271(self):
        newX = 190
        newY = 170
        self.ellipse.pos = (newX,newY)
        print("Go to interview room 271")
        self.communicateDestination(newX,newY)

    def goTo270(self):
        newX = 330
        newY = 170
        self.ellipse.pos = (newX,newY)
        print("Go to interview room 270")
        self.communicateDestination(newX,newY)

    def goTo268(self):
        newX = 493
        newY = 190
        self.ellipse.pos = (newX,newY)
        print("Go to office 268")
        self.communicateDestination(newX,newY)

    def goTo269(self):
        newX = 370
        newY = 170
        self.ellipse.pos = (newX,newY)
        print("Go to interview room 269")
        self.communicateDestination(newX,newY)

    def goTo274(self):
        newX = 1150
        newY = 170
        self.ellipse.pos = (newX,newY)
        print("Go to office 274")
        self.communicateDestination(newX,newY)

    def goTo275(self):
        newX = 1150
        newY = 203
        self.ellipse.pos = (newX,newY)
        print("Go to office 275")
        self.communicateDestination(newX,newY)

    def goTo276(self):
        newX = 1150
        newY = 416
        self.ellipse.pos = (newX,newY)
        print("Go to office 276")
        self.communicateDestination(newX,newY)

    def goTo277(self):
        newX = 1150
        newY = 450
        self.ellipse.pos = (newX,newY)
        print("Go to office 277")
        self.communicateDestination(newX,newY)

    def goTo278(self):
        newX = 1150
        newY = 655
        self.ellipse.pos = (newX,newY)
        print("Go to office 278")
        self.communicateDestination(newX,newY)

    def goTo262(self):
        newX = 1120
        newY = 810
        self.ellipse.pos = (newX,newY)
        print("Go to conference room 262")
        self.communicateDestination(newX,newY)


    def press(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'a':
            x, y = self.ellipse.pos
            w, h = self.ellipse.size
            inc = dp(10)
            diff = self.width - (x + w)
            if diff < inc:
                inc = diff
            if(y>=200 and y<=270 and x>100 and x<=670): x-=inc
            if (y >= 130 and y <= 270 and x >670 and x <= 1120): x -= inc
            if(y>270 and y<=830 and x>980):x-=inc

            self.ellipse.pos = (x, y)
            print("X is: ",x)

        if keycode[1] == 'd':
            x, y = self.ellipse.pos
            w, h = self.ellipse.size
            inc = dp(3)
            diff = self.width - (x + w)
            if diff < inc:
                inc = diff
            if (x>=100 and x <460 and y>=200 and y<=270): x += inc
            if (x>=460 and x<670 and y>=220 and y<=270): x+=inc
            if (x>=670 and x<1120 and y>=130 and y<=270): x+=inc
            if (x<1120 and y>=130 and y<=970): x+=inc

            self.ellipse.pos = (x, y)
            print("X is: ", x)

        if keycode[1] == 'w':
            x, y = self.ellipse.pos
            x=int(x)
            y=int(y)
            w, h = self.ellipse.size
            inc = dp(10)
            diff = self.width - (x + w)
            if diff < inc:
                inc = diff
            if (y<=260 and x<=970 and x>=100):
                y+=inc
                self.ellipse.pos = (x, y)

            if (y<830 and x>970 and x<=1120):
                y+=inc
                self.ellipse.pos = (x, y)

            print("Y is: ", y)

        if keycode[1] == 's':
            x, y = self.ellipse.pos
            w, h = self.ellipse.size
            inc = dp(10)
            diff = self.width - (x + w)
            if diff < inc:
                inc = diff

            if (y>=210 and x<490):
                y-=inc
                self.ellipse.pos = (x, y)

            if (y>=230 and x>=490 and x<670):
                y-=inc
                self.ellipse.pos = (x, y)

            if (y>130 and x>=670 and x<=1120):
                y-=inc
                self.ellipse.pos = (x, y)
            
            print("Y is: ", y)

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

    # def runThread(self,handler):
    #     t = threading.Thread(target=handler)
    #     # set daemon to true so the thread dies when app is closed
    #     t.daemon = True
    #     t.start()


    def communicateDestination(self,newX,newY):
        # print(self.sshConn.executeCommand("python3 MDS\ Robot\ Project/PiCode/KeyboardControl/termiosKeyboard.py"))
        print("in communicate destination")
        command = f"python3 MDS\ Robot\ Project/PiCode/SerialCommunicate.py {newX} {newY} -u"

        [print(str(line)) for line in self.sshConn.executeCommand(command)]

class MyApp(App):

    def build(self):
        Window.clearcolor = (0.7,0.7,0.7,1)
        # Window.fullscreen = 'auto'
        return Canvas()

if __name__ == "__main__":
    MyApp().run()

