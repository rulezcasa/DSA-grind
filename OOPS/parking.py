'''
We run parking lots for office buildings in downtown San Jose. Right now our client—a 10-story office building—wants software to manage their attached parking garage. 

- The garage has multiple levels and Each level has parking spots of different sizes: motorcycle, compact, and large (for SUVs/trucks). 
- A motorcycle can only park in a motorcycle spot. A compact car can park in a compact or large spot. A large vehicle needs a large spot.
- When a vehicle enters, it should be assigned the nearest available appropriately-sized spot. 
- When it leaves, that spot should become available again. 
- We also need to track how many spots are free on each level, and eventually generate a parking ticket with entry time (we'll add pricing later — not now, don't over-engineer for that yet).
- For v1, just get the core flow working: a vehicle enters, gets assigned a spot, and later exits and frees the spot. We'll extend it later, so keep it clean and extensible."
'''


from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime


'''
When this enum class is passed to an argument, it ensures that the arugment accepts only the specific entities. (VALIDATION)
'''
class SpotType(Enum):
    MOTORCYCLE = "motorcycle"
    COMPACT = "compact"
    LARGE = "large"



class Vehicle(ABC):
    def __init__(self, vehicle_number):
        self.vehicle_number=vehicle_number
    
    @abstractmethod #Using an abstract method here, as can_fit can be asked for multipel vehicle types (more added later), so this keeps the code clean and abstract
    def can_fit(self, spot_type: SpotType):
        pass

class Motorcycle(Vehicle):
    def can_fit(self, spot_type: SpotType):
        if spot_type==SpotType.MOTORCYCLE:
            return True
        else:
            return False

class Car(Vehicle):
    def can_fit(self, spot_type):
        if spot_type in (SpotType.COMPACT, SpotType.LARGE):
            return True
        else:
            return False

class Truck(Vehicle):
    def can_fit(self, spot_type):
        if spot_type==SpotType.LARGE:
            return True
        else:
            return False


class ParkingSpot():
    def __init__(self, level_number, spot_number, spot_type:SpotType):
        self.level_number = level_number
        self.spot_number = spot_number
        self.spot_type = spot_type
        self.vehicle = None # By deafult parking spot is empty

    def is_available(self):
        return self.vehicle is None
    
    def park(self, vehicle:Vehicle):

        self.vehicle=vehicle  # vehicle here is the object of Vehicle
        return True 
    
    def unpark(self):
        self.vehicle=None

    def __str__(self):
        return (
            f"Level {self.level_number} | "
            f"Spot {self.spot_number} | "
            f"{self.spot_type.value}"
        )

class ParkingLevel():
    def __init__(self, level_number):
        self.level_number=level_number
        self.spots=[]

    def add_spot(self, spot:ParkingSpot):
        self.spots.append(spot)
    
    def find_available_spot(self, vehicle:Vehicle):
        for spot in self.spots:
            if spot.is_available() and vehicle.can_fit(spot.spot_type):
                return spot 
        return None
    
    def free_spots(self):
        count=0
        for spot in self.spots:
            if spot.is_available():
                count+=1
        return count

class ParkingTicket:
    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()

    def __str__(self):
        return (
            f"Vehicle: {self.vehicle.vehicle_number}\n"
            f"Spot: {self.spot}\n"
            f"Entry Time: {self.entry_time}"
        )

class ParkingLot:
    def __init__(self):
        self.levels = []
        self.active_tickets = {}

    def add_level(self, level: ParkingLevel):
        self.levels.append(level)

    def park_vehicle(self, vehicle: Vehicle):

        for level in self.levels:

            spot = level.find_available_spot(vehicle)

            if spot:
                spot.park(vehicle)

                ticket = ParkingTicket(vehicle, spot)

                self.active_tickets[vehicle.license_plate] = ticket

                print(f"\nVehicle parked successfully.")
                print(ticket)

                return ticket

        print("\nNo parking spot available.")
        return None

    def exit_vehicle(self, license_plate):

        if license_plate not in self.active_tickets:
            print("Vehicle not found.")
            return

        ticket = self.active_tickets.pop(license_plate)

        ticket.spot.unpark()

        print(
            f"\nVehicle {license_plate} exited from "
            f"Level {ticket.spot.level_number}, "
            f"Spot {ticket.spot.spot_number}"
        )

    def display_availability(self):
        print("\nParking Availability")
        print("-" * 30)
        for level in self.levels:
            print(
                f"Level {level.level_number}: "
                f"{level.free_spots()} free spots"
            )


# =========================
# DRIVER CODE
# =========================

lot = ParkingLot()

# -------- Level 1 --------
level1 = ParkingLevel(1)

level1.add_spot(ParkingSpot(1, 1, SpotType.MOTORCYCLE))
level1.add_spot(ParkingSpot(1, 2, SpotType.COMPACT))
level1.add_spot(ParkingSpot(1, 3, SpotType.COMPACT))
level1.add_spot(ParkingSpot(1, 4, SpotType.LARGE))
level1.add_spot(ParkingSpot(1, 5, SpotType.LARGE))

lot.add_level(level1)

# -------- Level 2 --------
level2 = ParkingLevel(2)

level2.add_spot(ParkingSpot(2, 1, SpotType.MOTORCYCLE))
level2.add_spot(ParkingSpot(2, 2, SpotType.COMPACT))
level2.add_spot(ParkingSpot(2, 3, SpotType.LARGE))

lot.add_level(level2)


# =========================
# TEST
# =========================

bike = Motorcycle("BIKE-101")
car = Car("CAR-222")
truck = Truck("TRUCK-999")

lot.display_availability()

lot.park_vehicle(bike)
lot.park_vehicle(car)
lot.park_vehicle(truck)

lot.display_availability()

lot.exit_vehicle("CAR-222")

lot.display_availability()













    

        
    