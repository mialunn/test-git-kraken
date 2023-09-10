import json

class Target:

    def __init__(self, ip_address: str, port_start: int, port_end: int) -> None:
        self.ip_address = ip_address
        self.port_start = port_start
        self.port_end = port_end
    

    def print_information(self) -> None:
        result: str = json.dumps(self.__dict__)
        print(result)

