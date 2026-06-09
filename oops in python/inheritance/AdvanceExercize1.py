class Robot:
    def move(self):
        print("Robot moving on ground")

    def stop(self):
        print("Robot stopped")

    def fly(self):
        print("This robot cannot fly")

    def swim(self):
        print("This robot cannot swim")


class FlyingRobot(Robot):
    def fly(self):
        print("Robot is flying in air")


class SwimmingRobot(Robot):
    def swim(self):
        print("Robot is swimming in water")


class HybridRobot(FlyingRobot, SwimmingRobot):
    pass


# runtime behaviour change (strategy style)
class FlyStrategy:
    def fly(self):
        print("Flying with jet boosters")

class SwimStrategy:
    def swim(self):
        print("Swimming with propellers")


class CustomRobot(Robot):
    def set_fly(self, fly_obj):
        self.fly = fly_obj.fly

    def set_swim(self, swim_obj):
        self.swim = swim_obj.swim


# test robots
r1 = Robot()
r1.move()
r1.fly()        # unsupported handled

print("------")

r2 = FlyingRobot()
r2.move()
r2.fly()

print("------")

r3 = HybridRobot()
r3.fly()
r3.swim()

print("------")

r4 = CustomRobot()
r4.move()
r4.fly()        # initially unsupported

r4.set_fly(FlyStrategy())   # add flying at runtime
r4.fly()

r4.set_swim(SwimStrategy()) # add swimming at runtime
r4.swim()