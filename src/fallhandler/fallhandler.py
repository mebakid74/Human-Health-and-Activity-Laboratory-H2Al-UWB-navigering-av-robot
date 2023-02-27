class FallHandler:
    
# constants
PERSON_DOWN = False
PERSON_UP = True    

class FallHandler:
    def __init__(self, nav):
        self.positionPacket = "POSITION"
        self.settings = {
            "down-time": 30,
            "y-min": 0.4
        }
        self.navigation = nav
        self.reset()
        
    def handlePositionalData(self, p):
        if (self.suspended): return
        posHuman = p[0:2]
        posRobot = p[3:5]
        print(pos)
        state = PERSON_DOWN if posHuman[self.indexHeight] < self.settings["y-min"] else PERSON_UP
        if state == PERSON_DOWN:
            self.stateCounter += 1
            if self.stateCounter > self.settings["down-time"]:
                self.suspend()
                print("suspended")

        else:
            self.reset()
                      
    # suspend positional tracking (robot is helping)
    def suspend(self):
        self.suspended = True

    # restart positional tracking (robot is reset by assistant)
    def reset(self):
        self.storedState = PERSON_UP
        self.stateCounter = 0
        self.storedTime = 0
        self.suspended = False
