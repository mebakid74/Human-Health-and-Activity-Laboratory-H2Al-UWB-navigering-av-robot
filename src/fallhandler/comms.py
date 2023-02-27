import requests
import time

webServerUrl = "http://130.240.114.124:8081"

def makeRequest():
    return [float(x) for x in requests.get(webServerUrl).content.decode('utf-8').replace("[","").replace("]","").replace("'","").split(",")]

def commsLoop(fh):
    while 1:
        try:
            p = makeRequest()
            print(p)
            #fh.handlePositionalData()
        except Exception as e:
            print(e)
        time.sleep(0.1)

commsLoop(None)
