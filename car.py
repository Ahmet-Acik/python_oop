class Car:
    def __init__(self, make, model, year, for_sale):
        self.make = make
        self.model = model
        self.year = year
        self.for_sale = False
        self.odometer_reading = 0

    def start(self):
        print("Car is started")

    def stop(self):
        print("Car is stopped")

    def accelerate(self):
        print("Car is accelerating")

    def brake(self):
        print("Car is braking")

    def descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_car = Car('audi', 'A6', 2025, False)
print(my_car.descriptive_name())
