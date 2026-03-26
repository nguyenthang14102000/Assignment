class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        if hours > 0:
            self.travelled_distance += (hours * self.current_speed)
        else:
            print("Hours must be positive")

car = Car("ABC-123", 200)
car.accelerate(60)
print("Current speed:", car.current_speed, "km/h")
car.drive(1.5)
print("Travelled distance:", car.travelled_distance, "km")