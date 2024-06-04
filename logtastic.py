class Logtastic:
    def __init__(self):
        self.started = True
    
    def logger(self, message, type="info"):
        print(f"{type}: {message}")

def logger(message, type="info"):
    print(f"{type}: {message}")

def er(type="INFO", message=""):
    type = type.upper()
    print(f"{type}: {message}")