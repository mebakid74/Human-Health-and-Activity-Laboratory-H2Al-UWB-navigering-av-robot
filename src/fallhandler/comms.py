import requests
import time

def makeRequest(url):
    return [float(x) for x in requests.get(url).content.decode('utf-8').replace("[","").replace("]","").replace("'","")$

def commsLoop(fh, url, delay):
    print("starting relay reading")
    while True:
        try:
            p = makeRequest(url)
            fh.handlePositionalData(p)
        except Exception as e:
            print(e)
        time.sleep(delay)
