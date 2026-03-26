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

#main programm
#Car
import random
cars = []
result = []
for i in range(10):
    max_speed = random.randint(150, 200)
    n = Car(f"(ABC-{i+1})", max_speed)
    cars.append(n)

#Loop
result = False
hour = 0
while result == False:
    hour += 1
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)
    if car.travelled_distance >= 10000:
        result = True
        break
print("RACE RESULT")
for car in cars:
    print(f"{car.registration_number} {car.maximum_speed} {car.current_speed} {int(car.travelled_distance)}")




