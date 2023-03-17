# -*- coding: utf-8 -*-
import threading

import fallhandler.comms as comms
import fallhandler.fallhandler as fh
import navigation.nav as nav
from naoqi import ALProxy

relayUrl = "http://130.240.114.121:8081"
robotIp = "130.240.114.12"
robotPort = 9559

motionProxy =   ALProxy("ALMotion", robotIp, robotPort)
navProxy =      ALProxy("ALNavigation", robotIp, robotPort)
postureProxy =  ALProxy("ALRobotPosture", robotIp, robotPort)
ttsProxy =      ALProxy("ALTextToSpeech", robotIp, robotPort)
#tabletProxy =  ALProxy("ALTabletService", robotIp, robotPort)

navigation = nav.Navigation(motionProxy, navProxy, postureProxy, ttsProxy)
fallhandler = fh.FallHandler(navigation)
navigation.setFhCb(fallhandler)

def cb_onzoomdone(x, y):
        print(x, y)
        if x == "zoomreset":
                navigation.reset()

#tabletProxy.onTouchDown.connect(cb_onzoomdone)

threads = []
def addThread(t, args, **kwargs):
        threads.append(threading.Thread(target=t, args=args, kwargs=kwargs))

comms.commsLoop(fallhandler, relayUrl, 1)

addThread(comms.commsLoop, args=(fallhandler, relayUrl, 0.5, ))
for t in threads:
        pass #t.start()
