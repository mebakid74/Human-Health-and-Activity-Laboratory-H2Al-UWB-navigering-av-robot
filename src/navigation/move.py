
import qi
import argparse
import sys
import almath
import math
from naoqi import ALProxy


#från comms.py: person pos[x,y,z] rot[x,y,z], robot pos[x,y,z] rot[x,y,z]

def main(ip, port = 9559):
        type(p)

        ip = "130.240.114.12"

        motion  = ALProxy("ALMotion", ip, port)
        nav     = ALProxy("ALNavigation", ip, port)
        posture = ALProxy("ALRobotPosture", ip, port)
        tts     = ALProxy("ALTextToSpeech", ip, port)



        #Wake up pepper
        motion.wakeUp()

#navigateTo och moveTo funkar om vi använder getRobotPosition så kan vi kolla åt vilket håll pepper är riktad


def disToHuman():
    #värde från zerokey för pepper-värde för person

def move():
    x = disToHuman
    initPos = motion.getRobotPosition(True) #start pos med inbyggd positionering. (True=MRE sensor)
    targetDis = getParameter(x)

    #motion.MoveTo(#x, y, z)
    #motion.NavigateTo(#x, y)

    expectedEndPos = initPos * targetDis #kollar om pepper har nått sitt mål

    RealEndPos = motion.getRobotPosition(False)
    PosError = RealEndPos.diff(expectedEndPos)
    
    if(PosError =< PosThreshold):
        #starta countdown för ringa vårdare
        else:
            move(#nya värden)
         
