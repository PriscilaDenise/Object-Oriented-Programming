# class GameCharacter:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health

#     def attack(self):
#         raise NotImplementedError("Subclasses must implement attack()")

#     def defend(self):
#         raise NotImplementedError("Subclasses must implement defend()")

#     def interact_with_object(self, obj):
#         raise NotImplementedError("Subclasses must implement interact_with_object()")


# class Warrior(GameCharacter):
#     def __init__(self, name, health, strength):
#         super().__init__(name, health)
#         self.strength = strength

#     def attack(self):
#         print(f"{self.name} attacks with strength {self.strength}")

#     def defend(self):
#         print(f"{self.name} defends with a shield")

#     def interact_with_object(self, obj):
#         if isinstance(obj, Weapon):
#             print(f"{self.name} equips the weapon")
#         else:
#             print(f"{self.name} cannot interact with this object")


# class Mage(GameCharacter):
#     def __init__(self, name, health, mana):
#         super().__init__(name, health)
#         self.mana = mana

#     def attack(self):
#         print(f"{self.name} casts a spell with {self.mana} mana")

#     def defend(self):
#         print(f"{self.name} creates a magical shield")

#     def interact_with_object(self, obj):
#         if isinstance(obj, Potion):
#             print(f"{self.name} drinks the potion")
#         else:
#             print(f"{self.name} cannot interact with this object")


# class Weapon:
#     pass


# class Potion:
#     pass


# if __name__ == "__main__":
#     warrior = Warrior("Arthur", 100, 50)
#     mage = Mage("Merlin", 80, 100)

#     warrior.attack()
#     warrior.defend()
#     warrior.interact_with_object(Weapon())

#     mage.attack()
#     mage.defend()
#     mage.interact_with_object(Potion())



class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        raise NotImplementedError("Subclasses must implement attack()")

    def defend(self):
        raise NotImplementedError("Subclasses must implement defend()")

    def interact_with_object(self, obj):
        raise NotImplementedError("Subclasses must implement interact_with_object()")


class Warrior(GameCharacter):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength

    def attack(self):
        print(f"{self.name} swings a sword with strength {self.strength}")

    def defend(self):
        print(f"{self.name} blocks with a heavy shield")

    def interact_with_object(self, obj):
        if isinstance(obj, Weapon) and obj.type == "sword":
            print(f"{self.name} equips the sword with strength {obj.power}")
        else:
            print(f"{self.name} cannot use this object")


class Mage(GameCharacter):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def attack(self):
        print(f"{self.name} casts a powerful spell using {self.mana} mana")

    def defend(self):
        print(f"{self.name} conjures a mystical barrier")

    def interact_with_object(self, obj):
        if isinstance(obj, Potion) and obj.type == "mana":
            self.mana += obj.restore
            print(f"{self.name} drinks a mana potion and restores {obj.restore} mana")
        else:
            print(f"{self.name} cannot use this object")


class Archer(GameCharacter):
    def __init__(self, name, health, agility):
        super().__init__(name, health)
        self.agility = agility

    def attack(self):
        print(f"{self.name} shoots an arrow with agility {self.agility}")

    def defend(self):
        print(f"{self.name} dodges swiftly")

    def interact_with_object(self, obj):
        if isinstance(obj, Weapon) and obj.type == "bow":
            print(f"{self.name} equips a powerful bow with strength {obj.power}")
        else:
            print(f"{self.name} cannot use this object")


class Weapon:
    def __init__(self, type, power):
        self.type = type
        self.power = power


class Potion:
    def __init__(self, type, restore):
        self.type = type
        self.restore = restore


if __name__ == "__main__":
    warrior = Warrior("Arthur", 120, 40)
    mage = Mage("Merlin", 80, 100)
    archer = Archer("Robin", 90, 60)

    sword = Weapon("sword", 30)
    bow = Weapon("bow", 25)
    mana_potion = Potion("mana", 20)

    # Warrior interactions
    warrior.attack()
    warrior.defend()
    warrior.interact_with_object(sword)

    # Mage interactions
    mage.attack()
    mage.defend()
    mage.interact_with_object(mana_potion)

    # Archer interactions
    archer.attack()
    archer.defend()
    archer.interact_with_object(bow)
