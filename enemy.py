from character import Character


class Enemy(Character):

    nbr_enemy_created = 0

    def __init__(self, name="", marbles = 0, age = 0):
        super().__init__(name, marbles)
        self.age = age
        Enemy.nbr_enemy_created += 1
        print(f"Enemy n°{Enemy.nbr_enemy_created} created ! ")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def win(self):
        pass

    def lose(self):
        pass