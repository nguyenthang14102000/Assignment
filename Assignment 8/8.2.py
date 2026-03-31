class Elevator:
    def __init__(self, bottom, top):
        self.top = top
        self.bottom = bottom
        self.current_floor = bottom
    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")
    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")
    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()

class Building:
    def __init__(self,bottom,top,number_elevators):
        self.bottom = bottom
        self.top = top
        self.number_elevators = []
        for i in range(number_elevators):
            self.number_elevators.append(Elevator(bottom,top))
    def run_elevator(self,elevator_num,target):
        print(f"\nRunning elevator {elevator_num} to floor {target}")
        elevator = self.number_elevators[elevator_num - 1]
        elevator.go_to_floor(target)

#main programm
b = Building(1,10,5)
b.run_elevator(1, 5)
b.run_elevator(2, 7)






