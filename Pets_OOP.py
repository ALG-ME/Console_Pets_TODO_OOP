class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        print("Гав")

    def bark(self):
        print("The dog is barking")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def make_sound(self):
        print("Мяу")

    def purr(self):
        print("The cat is purring")


# Создание объектов классов
animal = Animal("боря", "Cat")
dog = Dog("Рекс", "Labrador")
cat = Cat("Мурка", "Gray")

# Вызов методов для каждого объекта
animal.make_sound()  # Выведет: Some generic sound
dog.make_sound()     # Выведет: Гав
dog.bark()            # Выведет: The dog is barking
cat.make_sound()     # Выведет: Мяу
cat.purr()           # Выведет: The cat is purring
