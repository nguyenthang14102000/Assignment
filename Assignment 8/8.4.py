import random

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
            self.travelled_distance += self.current_speed * hours

class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.kilometers = kilometers
        self.car_list = car_list
    def hour_passes(self):
        for car in self.car_list:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)
    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Car':<10}{'Max Speed':<12}{'Current Speed':15}{'Distance':<12}")
        print("-" * 49)
        for car in self.car_list:
            print(f"{car.registration_number:<10}{car.maximum_speed:<12}{car.current_speed:<15}{int(car.travelled_distance)}")
    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.kilometers:
                return True
        return False


# main program
cars = []
for i in range(10):
    max_speed = random.randint(100, 200)
    car = Car(f"ABC-{i+1}", max_speed)
    cars.append(car)
race = Race("Grand Demolition Derby", 8000, cars)
hours = 0
while not race.race_finished():
    hours += 1
    race.hour_passes()
    if hours % 10 == 0:
        race.print_status()
race.print_status()