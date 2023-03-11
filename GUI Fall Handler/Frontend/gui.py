import qi
from naoqi import ALProxy

import time

#Establishing a connection to pepper robot 
session = qi.Session()
session.connect("tcp://130.240.114.12:9559")

#V as for creating a tablet service object & enable tablet's wifi
v = session.service("ALTabletService") 
v.enableWifi()

#Displaying a web page on the tablet
url = ("http://www.google.com")
v.showWebview(url)

#Displaying a gui fall handler web page
v.showWebview("http://198.18.0.1/apps/boot-config/index.html")
v.showWebview("http://198.18.0.1/apps/boot-config/main.html")










