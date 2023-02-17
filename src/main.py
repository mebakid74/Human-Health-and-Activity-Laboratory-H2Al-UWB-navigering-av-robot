from visual.gui import *
import notification.tts as tts
from notification.chatstream import *
from navigation.movementhandler import *
from fallhandler.signalr import *

class App:
    def __init__(self):
        self.fallhandler = Fallhandler()
        self.gui = Gui()

if __name__ == "__main__":
    App()
