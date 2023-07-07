
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self, name):
        if not self.open_Seats():
            return False
        else:
            self.passenger.append(name)
            return True

    def open_Seats(self):
        return self.capacity - len(self.passenger)
        
flight = Flight(3)

people = ["Rommer", "Corazon", "Peter", "Abigail", "John"]
for person in people:
    count = Flight.open_Seats(flight)
    success = flight.add_passenger(person)
    if success:
        print(f"We've added {person} to the flight successfully")
        # print(Flight.open_Seats(flight))
    else:
        print(f"{count} seats avaialable for {person}")