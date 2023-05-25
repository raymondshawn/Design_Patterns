from abc import  ABC,abstractmethod
class Recipe:
    def prepare(self):
        self.preheat_oven()
        self.mix_ingredients()
        self.bake()
        self.cool()
        self.decorate()

    def preheat_oven(self):
        print("Preheating oven...")

    def mix_ingredients(self):
        raise NotImplementedError("Subclasses must implement mix_ingredients method")

    def bake(self):
        raise NotImplementedError("Subclasses must implement bake method")

    def cool(self):
        print("Allowing to cool...")

    def decorate(self):
        raise NotImplementedError("Subclasses must implement decorate method")

class ChocolateCake(Recipe):
    def mix_ingredients(self):
        print("Mixing chocolate cake ingredients...")

    def bake(self):
        print("Baking the chocolate cake...")

    def decorate(self):
        print("Decorating the chocolate cake...")

class Pancakes(Recipe):
    def mix_ingredients(self):
        print("Mixing pancake ingredients...")

    def bake(self):
        print("Cooking the pancakes on a griddle...")

    def decorate(self):
        print("Adding syrup and toppings to the pancakes...")

# Usage
def main():
    chocolate_cake = ChocolateCake()
    chocolate_cake.prepare()

    print("-----")

    pancakes = Pancakes()
    pancakes.prepare()

if __name__ == '__main__':
    main()
