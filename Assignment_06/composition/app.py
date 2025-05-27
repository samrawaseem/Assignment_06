class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} horsepower is now running.")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Using composition: Car contains an Engine object

    def start_car(self):
        print(f"Starting the {self.brand} car...")
        self.engine.start()  # Invoking the Engine’s start method through Car

# Instantiate an Engine object
engine1 = Engine(150)

# Instantiate a Car object, passing the Engine object to it
car1 = Car("Toyota", engine1)

# Start the car, which triggers the engine to start as well
car1.start_car()
