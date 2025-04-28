# Defining a class of the name "car"
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
    
    def drive(self):
        print(f"The {self.color} car is driving at {self.speed} km/h.")
    
    def stop(self):
        print(f"The {self.color} car has stopped.")

# Example

my_car = Car("red", 100)
my_car.drive()
my_car.stop()


# An example of sub-classing 
class ElectricCar(Car):
    def __init__(self, color, speed, battery_capacity):
        super().__init__(color, speed)  # Call the parent class constructor
        self.battery_capacity = battery_capacity  # New attribute specific to ElectricCar
    
    def charge(self):
        print(f"Charging the car to {self.battery_capacity} kWh.")

    def drive(self):  # Override the drive method
        print(f"The {self.color} electric car is silently driving at {self.speed} km/h.")

# Example explaining the sub-class
my_electric_car = ElectricCar("blue", 120, 85)
my_electric_car.drive()      # Uses overridden drive
my_electric_car.charge()     # New method
my_electric_car.stop()       # Inherited from Car



