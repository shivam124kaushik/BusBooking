 class BusBookingSystem:
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.bookedSeats = {}

    def displayAvailableSeats(self):
        print("Available Bus Seats:")
        for destination, seats in self.availableSeats.items():
            print(f"{destination}: {seats}")

    def bookSeat(self, user, destination, seatNumber):
        if destination in self.availableSeats and seatNumber in self.availableSeats[destination]:
            self.availableSeats[destination].remove(seatNumber)
            self.bookedSeats.setdefault(user, []).append({"destination": destination, "seatNumber": seatNumber})
            print(f"Booking successful! Seat {seatNumber} for {destination} booked for {user}.")
        else:
            print("Invalid destination or seat number. Please try again.")

    def displayBookedSeats(self, user):
        if user in self.bookedSeats and self.bookedSeats[user]:
            print(f"Booked seats for {user}:")
            for booking in self.bookedSeats[user]:
                print(f"- {booking['destination']}: Seat {booking['seatNumber']}")
        else:
            print(f"No bookings found for {user}.")

class Passenger:
    def requestSeat(self):
        destination = input("Enter the destination: ")
        seatNumber = int(input("Enter the seat number you want to book: "))
        return destination, seatNumber

if __name__ == "__main__":
    busSystem = BusBookingSystem({
        "indore to bhopal": list(range(1, 16)),"indore to dewas": list(range(1, 11)),"indore to ujjain": list(range(1, 21))})

    passenger = Passenger()

    while True:
        welcomeMsg = '''\n ====== Welcome to Bus Booking System ======
        Please choose an option:
        1. Available seats in bus
        2. Book a seat
        3. View booked seats
        4. Exit
        '''
        print(welcomeMsg)
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                busSystem.displayAvailableSeats()
            elif choice == 2:
                destination, seatNumber = passenger.requestSeat()
                busSystem.bookSeat("Passenger", destination, seatNumber)
            elif choice == 3:
                busSystem.displayBookedSeats("Passenger")
            elif choice == 4:
                print("Thank you for using the Bus Booking System.")
            else:
                print("Invalid choice. Please try again.")
        except:
            print("invalid input")
        
