from random import randint
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self._cords = [0,0,0]
        self.speed = speed
    def move(self, dx, dy, dz):
        self._cords[0] = (self.speed * dx)
        self._cords[1] = (self.speed * dy)
        if self.speed * dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = (self.speed * dz)

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f"Here are (is) {randint(1, 4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        dz = abs(dz)
        new_z = self._cords[2] - dz * (self.speed / 2)
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = int(new_z)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"



if __name__ == "__main__":
    db = Duckbill(10)
    print(Duckbill.mro())
    print(AquaticAnimal.mro())

    print(db.live)
    print(db.beak)

    db.speak()
    db.attack()

    db.move(1,2,3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()

    db.lay_eggs()




