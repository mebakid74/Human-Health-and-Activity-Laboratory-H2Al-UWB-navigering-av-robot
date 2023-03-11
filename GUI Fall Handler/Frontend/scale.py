from naoqi import qi

ip = "your_robot_ip_address"
port = 9559

session = qi.Session()
session.connect("tcp://" + ip + ":" + str(port))
tablet_service = session.service("ALTabletService")

scale_factor = 1.5 # set the scaling factor to 150%
tablet_service.setOnTouchWebviewScaleFactor(scale_factor)

def on_scale_factor_changed(scale_factor):
    print("Scaling factor changed to:", scale_factor)

tablet_service.setOnTouchWebviewScaleFactor(on_scale_factor_changed)

ALTabletService tabletService;
tabletService.setOnTouchWebviewScaleFactor(1.0);
