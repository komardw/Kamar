import random
class Student:

    def __init__(self,name):
        self.name = name
        self.hapiness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.hapiness -= 3

    def to_sleep(self):
        print("Time to sleep")
        self.hapiness += 3

    def to_chill(self):
        print("Time to rest")
        self.hapiness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        elif self.hapiness <= 0:
            print("depression")
            self.alive = False
        elif self.progress > 5:
            print("Sigma")
            self.alive = False

    def end_of_day(self):
        print(f"Hapiness = {self.hapiness}")
        print(f"progress = {round(self.progress,2)}")

    def live(self,day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"day{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

Vasya_student = Student(name="Vasya")

for day in range(365):
    if Vasya_student.alive == False:
        break
    Vasya_student.live(day)

