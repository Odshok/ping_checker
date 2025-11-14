class Point:
    def __init__(self, addr: str,available: bool,
                 information: str = ""):
        self.addr = addr
        self.available = available
        self.information = information