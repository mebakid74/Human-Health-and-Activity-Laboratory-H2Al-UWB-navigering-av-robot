import fallhandler.signalr as fh

class App:
    def __init__(self):
        self.fallhandler = new fh.Fallhandler()
        self.fallhandler.start()

if __name__ == "__main__":
    App()
