class Animal:
    def __init__(self, name, species):
        self.nome = name
        self.especies = species

    def __repr__(self):
        return f"{self.nome} is a {self.especies}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    def __init__(self):
        super().__init__(name="anderson", species="cachorro")

    def say_hi(self):
        print(f"hi i am {self.nome}")

    def do(self):
        return f"{self.__repr__()} wil do something!!"


cachorro = Cat()
print(cachorro.do())