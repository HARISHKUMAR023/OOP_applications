class RailwayReservationSystem:
    def __init__(self):
        print(" ***==> Railway reservation system <==*** ")
        self.trains = {
            "Train1": {"from": "morappur", "to": "salem"},
            "Train2": {"from": "StationB", "to": "StationC"},
            "Train3": {"from": "StationA", "to": "StationC"},
        }

    def find_station(self):
        self.startform = input(" Enter your station name: ")
        self.destination = input(" Enter your destination name: ")
        for train, route in self.trains.items():
            if route["from"] == self.startform and route["to"] == self.destination:
                print(f"{train} is available from {self.startform} to {self.destination}")
            else:
                print(f"{train} is not available from {self.startform} to {self.destination}")
                break
    def booking(self):
        tickettotal = int(input("Enter the number of tickets you want to book: "))
        passername=[]
        for i in range(tickettotal):
            name = input(f"Enter the passenger name for ticket {i+1}: ")
            passername.append(name)
            print(f"Ticket {i+1}  is booked for {name}")
        print(f"Tickets are booked for {passername}")
        print("Thank you for booking with us")
    def option(self):
        while True:  # Start of the loop
            print("*** You need to choose the option below ***")
            print("1 => Train available check")
            print("2 => Train Ticket Booking")
            print("3 => Exit")
            op = input("Choose your option: ")
            if op == "1":
                self.find_station()
            elif op == "2":
                
                self.booking()
            elif op == "3":
                print("Exiting the program. Thank you!")
                break  # Exit the loop
            else:
                print("Invalid option. Please try again")

# Create an instance of the RailwayReservationSystem and call the option method to start the program
if __name__ == "__main__":
    rrs = RailwayReservationSystem()
    rrs.option()
    # rrs.booking()