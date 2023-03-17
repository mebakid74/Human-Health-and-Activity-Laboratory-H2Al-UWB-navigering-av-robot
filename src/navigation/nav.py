# -*- coding: utf-8 -*-
import qi
import argparse
import sys
import almath
import math
from time import sleep
from naoqi import ALProxy

#fromn comms.py: person pos[x,y,z] rot[x,y,z], robot pos[x,y,z] rot[x,y,z]

class Navigation():
        def __init__(self, motion, nav, posture, tts):
                self.motion = motion
                self.nav = nav
                self.posture = posture
                self.tts = tts

        def onFall(self, humanPos, robotPos):
                print("x:", robotPos[0] - humanPos[0])
                print("y:", robotPos[1] - humanPos[1])
                sleep(1)
                self.fallhandler.reset()
                self.move(humanPos, robotPos)
        def reset(self):
                pass

        def setFhCb(self, fh):
                self.fallhandler = fh


        def turn(self):
                goal= 0.0133
                current = self.motion.getRobotPosition(True)
                curZ = current[2]
                turn = curZ - goal

                if current < 0:
                   self.motion.moveTo(0.0, 0.0, turn)
                else:
                   self.motion.moveTo(0.0, 0.0, -turn)


        def move(self, humanPos, robotPos):
                self.motion.wakeUp()
                self.posture.goToPosture("StandInit", 0.5)

                disToHumanX = robotPos[0] - humanPos[0]
                disToHumanY = robotPos[1] - humanPos[1]

                if abs(disToHumanX) > 0.8 or abs(disToHumanY) > 0.8:
                   self.turn()
                   #print("Still going")
                   self.nav.navigateTo(disToHumanX, disToHumanY)
                else:
                   #print("At human","DisX= ",disToHumanX, "DisY= ",disToHumanY)
                   self.motion.angleInterpolationWithSpeed("HipPitch", -1.5, 0.1)
                   #self.tts.say("Calling caregiver")
                   self.fallhandler.suspend()
                
