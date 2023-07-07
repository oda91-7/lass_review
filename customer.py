class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif 75 <= self.age:
            return 500
        else:
            return 1200
    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    def tab(self):
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.tab())

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.tab())

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.tab())
