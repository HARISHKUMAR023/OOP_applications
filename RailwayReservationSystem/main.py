class RailwayReservationSystem:
    def __init__(self):
        print(" ***==> Railway reservation system <==*** ")
        self.trains = {
            "kovai_express": {"from": "morappur", "to": "salem" , "ticketprice": 110 , "availableseats": 100},
            "chennai_express": {"from": "StationB", "to": "StationC","ticketprice": 120 , "availableseats": 100},
            "mumbai_express": {"from": "StationA", "to": "StationC","ticketprice": 130 , "availableseats": 100},
        }

    def find_station(self):
        self.startform = input(" Enter your station name: ")
        self.destination = input(" Enter your destination name: ")
        for train, route in self.trains.items():
            if route["from"] == self.startform and route["to"] == self.destination:
                print(f"{train} is available from {self.startform} to {self.destination}")
                print(f"Ticket price is {route['ticketprice']}")
                print(f"Available seats are {route['availableseats']}")
                break
            else:
                print(f"{train} is not available from {self.startform} to {self.destination}")
                break
            
    def booking(self):
        self.find_station()
        print("Ticket booking process is started")
        
        
        tickettotal = int(input("Enter the number of tickets you want to book: "))
        passername=[]
        for i in range(tickettotal):
            name = input(f"Enter the passenger name for ticket {i+1}: ")
            passername.append(name)
            print(f"Ticket {i+1}  is booked for {name}")
        for train, route in self.trains.items():
            if route["from"] == self.startform and route["to"] == self.destination:
                route["availableseats"] -= tickettotal
                print(f"Available seats are {route['availableseats']}")
                break
        print(f"Tickets are booked for {passername} for train {train} from {self.startform} to {self.destination}")
        print(f"Ticket price is {tickettotal} = {route['ticketprice']*tickettotal + 10} including GST")
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