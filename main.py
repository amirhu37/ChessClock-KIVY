from kivy.app import App

from kivy.clock import Clock
import time

from kivy.uix.popup import Popup

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = ( 812 , 375 )


class Screen_Manager(ScreenManager): 
    pass

class Main_Screen(Screen):
    pass

class Play_ground(Screen):
    def toggle_staste(self):
        pass
    def white(self):
        print('White Taped')
    
    def Black(self):
        print('Black presssed')

        pass

class Timer_pop_up(Popup):
    pass



kv = Builder.load_file('ChessClock.kv')
class ChessClock(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return kv


if __name__=='__main__':
    ChessClock().run()




#"""     
#     self.modes = (
#         '%I:%m:%S',
#         '%H:%m:%S %P',
#         '%S:',
#     )
#     self.mode = 0
#     Clock.schedule_interval(self.timer, 0.01)
#     
#def timer(self, dt):
#       now = datetime.datetime.now()
#       self.button.text = now.strftime(self.modes[self.mode])
#       if self.mode == 2:
#           self.button.text += str(now.microsecond)[:3]
#
#"""           