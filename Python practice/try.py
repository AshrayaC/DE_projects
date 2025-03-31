# Defining a class named Car
class Car:
    # Constructor method to initialize attributes
    def __init__(self, brand, fuel_type) -> None:
        self.brand = brand  # Assign brand to the instance
        self.fuel_type = fuel_type  # Assign fuel type to the instance


    # Method to simulate driving the car
    def drive(self, distance):
        print(f"Driving {self.brand} for {distance} miles.")  # Print the driving message
    
    def __str__(self) -> str:
        print(f"{self.brand},{self.fuel_type}")
        return(f'{self.brand},{self.fuel_type}')
    

# Creating an instance (object) of the Car class
car1 = Car("Volvo", "oil")
print(car1)

# Accessing and printing object attributes
#print(car1.brand)      # Output: Volvo
#print(car1.fuel_type)  # Output: oil

# Calling the drive method with a distance of 20 miles
#car1.drive(20)  # Output: Driving Volvo for 20 miles.