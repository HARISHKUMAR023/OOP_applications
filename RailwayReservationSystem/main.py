class Railway:
    def __init__(self):
        print(" ***==> Railway reservation system <==*** ")
        self.startform = input("Enter your station name: ")
        self.destination = input("Enter your destination name: ")
        self.trains = {
            "Train1": {"from": "StationA", "to": "StationB"},
            "Train2": {"from": "StationB", "to": "StationC"},
            "Train3": {"from": "StationA", "to": "StationC"},
        }

    def find_station(self):
        for train, route in self.trains.items():
            if route["from"] == self.startform and route["to"] == self.destination:
                print(f"{train} is available from {self.startform} to {self.destination}")

p1 = Railway()
p1.find_station()