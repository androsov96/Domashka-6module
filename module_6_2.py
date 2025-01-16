class Vehicle:
    __COLOR_VARIANTS = ["blue", "red", "green", "black", "white"]
    def __init__(self, owner, model, engine_power, color):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)
    def get_model(self):
        print(f"Модель: {self.__model}")
    def get_horsepower(self):
        print(f"Мощность двигателя: {self.__engine_power} л.с.")
    def get_color(self):
        print(f"Цвет: {self.__color}")
    def print_info(self):
        return self.get_model(), self.get_horsepower(), self.get_color(), print(f"Владелец: {self.owner}")
    def set_color(self, new_color):
        self.new_color = new_color
        if new_color.lower() in (i.lower() for i in self.__COLOR_VARIANTS):
            self.__color = self.new_color
        else:
            print(f"Нельзя сменить цвет на {self.new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

if __name__ == "__main__":
    vehicle1 = Sedan("Александр", "Tayota Mark II", 200, "blue")
    vehicle1.print_info()

    vehicle1.set_color("Pink")
    vehicle1.set_color("BLACK")
    vehicle1.owner = "Denis"


    vehicle1.print_info()