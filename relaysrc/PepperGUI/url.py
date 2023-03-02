import qi
from naoqi import ALProxy

import time

session = qi.Session()
session.connect("tcp://130.240.114.12:9559")

v = session.service("ALTabletService") 
v.enableWifi()

url = ("http://www.google.com")
v.showWebview(url)

v.showWebview("http://198.18.0.1/apps/boot-config/index.html")
v.showWebview("http://198.18.0.1/apps/boot-config/main.html")











