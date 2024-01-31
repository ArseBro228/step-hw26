# class Book:
#     def __init__(self, name, year, publisher, genre, author, cost):
#         self.name = name
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.__author = author
#         self.cost = cost
#
#     @property
#     def author(self):
#         return self.__author
#
#     @author.setter
#     def author(self, new_author):
#         self.__author = new_author

# class Fraction:
#     def __init__(self, numerator, denominator):
#         if denominator == 0:
#             raise ValueError("Знаменатель не может быть равен нулю")
#         self.__numerator = numerator
#         self.__denominator = denominator
#         self.simplify()
#
#     def get_numerator(self):
#         return self.__numerator
#
#     def get_denominator(self):
#         return self.__denominator
#
#     def set_numerator(self, numerator):
#         self.__numerator = numerator
#         self.simplify()
#
#     def set_denominator(self, denominator):
#         if denominator == 0:
#             raise ValueError("Знаменатель не может быть равен нулю")
#         self.__denominator = denominator
#         self.simplify()
#
#     def display(self):
#         print(f"{self.__numerator}/{self.__denominator}")
#
#     def gcd(self, a, b):
#         while b:
#             a, b = b, a % b
#         return a
#
#     def simplify(self):
#         common_factor = self.gcd(self.__numerator, self.__denominator)
#         self.__numerator //= common_factor
#         self.__denominator //= common_factor
#
#     def add(self, other_fraction):
#         result_numerator = (self.__numerator * other_fraction.get_denominator()) + \
#                            (other_fraction.get_numerator() * self.__denominator)
#         result_denominator = self.__denominator * other_fraction.get_denominator()
#         result = Fraction(result_numerator, result_denominator)
#         return result
#
#     def subtract(self, other_fraction):
#         result_numerator = (self.__numerator * other_fraction.get_denominator()) - \
#                            (other_fraction.get_numerator() * self.__denominator)
#         result_denominator = self.__denominator * other_fraction.get_denominator()
#         result = Fraction(result_numerator, result_denominator)
#         return result
#
#     def multiply(self, other_fraction):
#         result_numerator = self.__numerator * other_fraction.get_numerator()
#         result_denominator = self.__denominator * other_fraction.get_denominator()
#         result = Fraction(result_numerator, result_denominator)
#         return result
#
#     def divide(self, other_fraction):
#         if other_fraction.get_numerator() == 0:
#             raise ValueError("Деление на ноль невозможно")
#         result_numerator = self.__numerator * other_fraction.get_denominator()
#         result_denominator = self.__denominator * other_fraction.get_numerator()
#         result = Fraction(result_numerator, result_denominator)
#         return result
#
#
# fraction1 = Fraction(1, 2)
# fraction2 = Fraction(3, 4)
#
# fraction1.display()
# fraction2.display()
#
# sum_result = fraction1.add(fraction2)
# sum_result.display()
#
# diff_result = fraction1.subtract(fraction2)
# diff_result.display()
#
# prod_result = fraction1.multiply(fraction2)
# prod_result.display()
#
# quot_result = fraction1.divide(fraction2)
# quot_result.display()

class GameCharacter:
    name: str
    level: int
    health: int
    damage: int
    defence: int
    experience: int

    def __init__(self, name, level, health, damage, defence, experience):
        self.name = name
        self.level = level
        self.health = health
        self.damage = damage
        self.defence = defence
        self.experience = experience

    def attack(self, target: 'GameCharacter'):
        target.health -= max(self.damage - target.defence, 0)
        if target.health > 0:
            print(f'{target.name} was attacked by {self.name};\n{target.name} has {target.health}hp.\n')
        else:
            self.experience += 90
            print(f'{target.name} was attacked by {self.name};\n{target.name} died.\n')
            if self.experience >= 100:
                self.level_up()

    def level_up(self):
        self.level += 1
        self.health = int(self.health * 1.1)
        self.damage = int(self.damage * 1.1)
        self.defence = int(self.defence * 1.1)
        self.experience -= 100
        print(f"{self.name} now has level {self.level}")
        self.display_stats()

    def display_stats(self):
        print(f'''stats of {self.name}:
level: {self.level}
health: {self.health}
damage: {self.damage}
defence: {self.defence}
experience: {self.experience}''')


a = GameCharacter(
    name='A',
    level=1,
    health=100,
    damage=10,
    defence=5,
    experience=30,
)
b = GameCharacter(
    name='B',
    level=1,
    health=100,
    damage=10,
    defence=5,
    experience=0,
)

while True:
    a.attack(b)
    if b.health <= 0:
        print(f'{a.name} is winner!')
        break
    b.attack(a)
    if a.health <= 0:
        print(f'{b.name} is winner!')
        break
