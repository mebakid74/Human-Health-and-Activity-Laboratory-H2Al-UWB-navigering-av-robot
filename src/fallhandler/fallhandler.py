# constants
PERSON_DOWN = False
PERSON_UP = True

class FallHandler:
    def __init__(self, nav):
        self.positionPacket = "POSITION"
        self.settings = {
            "down-time": 2,
            "y-min": 0.4
        }
        self.navigation = nav
        self.reset()

    def handlePositionalData(self, p):
        if (self.suspended): return
        posHuman = p[0:3]
        posRobot = p[6:9]
        print(posHuman, posRobot)
        state = PERSON_DOWN if posHuman[2] < self.settings["y-min"] else PERSON_UP
        if state == PERSON_DOWN:
            self.stateCounter += 1
            print("down", self.stateCounter)
            if self.stateCounter > self.settings["down-time"]:
                self.suspend()
                print("suspended")
                self.navigation.onFall(posHuman, posRobot)

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
