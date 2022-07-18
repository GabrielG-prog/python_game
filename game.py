from enemy import Enemy
from hero import Hero
import random
from utils import Utils


class Game:

    levels = (5, 15, 20)

    def __init__(self):
        self.nbr_encounters = 0
        self.hero = Hero()
        self.list_heroes = []
        self.list_enemies = []
        self.enemy = Enemy()

    def __create_heroes(self, list_heroes):
        for hero in list_heroes:
            # name, marbles, loss, gain, scream_war
            self.list_heroes.append(Hero(hero["name"], hero["marbles"], hero["loss"], hero["gain"], hero["scream_war"] ))

    # name, marbles, age
    def __create_enemies(self, list_enemies):
        for enemy in list_enemies:
            self.list_enemies.append(Enemy(enemy["name"], enemy["marbles"], enemy["age"]))


    def __present_the_heroes(self):

        for hero in self.list_heroes:
            hero.introduce()

        self.nbr_encounters = Game.levels[self.hero.chose_level_of_dificulty() - 1]
        print(f"You chose to fight {self.nbr_encounters} rounds !")

        self.hero.chose_skills()
        print(f"You chose to fight with {self.hero.name} ! ")

        self.__fights()


    def __handleFight(self):

        odd_or_even_answer = Utils.read_number("Does you enemy have an odd or even number of marbles in his hand? Press (1) for odd and (2) for even ", 1, 2)

        if odd_or_even_answer % 2 == self.enemy.marbles % 2:
            self.hero.marbles += (self.enemy.marbles + self.hero.gain)
            print(
                f"Congratulations, you won the fight, you have now {self.hero.marbles} ( {self.enemy.marbles} + {self.hero.gain} ) ")
        else:
            self.hero.marbles -= (self.enemy.marbles + self.hero.loss)
            print(
                f"HAHAHAHA, you lose the fight, you have now {self.hero.marbles} ( {self.enemy.marbles} + {self.hero.loss} ) ")


    def __fights(self):

        i = 0

        while self.hero.marbles > 0 and i < len(self.list_enemies):

            # je sélectionne aléatoirement un ennemie
            self.enemy = random.choice(self.list_enemies)
            print(
                f"You are fighting {self.enemy.name} with {self.hero.marbles} marbles in your hand, he has {self.enemy.marbles} marbles in his hand !")

            if self.enemy.age > 70:
                try:
                    cheat = Utils.read_number("Your enemy is very old, do you want to cheat on him ? Press (1) to remain loyal and (2) to cheat !", 1, 2)

                    if cheat == 2:
                        self.hero.marbles += self.enemy.marbles
                    elif cheat == 1:
                        print("Your are a good person, get ready for the fight !")
                        self.__handleFight()
                    else:
                        print("Press (1) to remain loyal and (2) to cheat !")

                except ValueError:
                    print("Press (1) to remain loyal and (2) to cheat !")

            else:
                self.__handleFight()

        else:

            if self.hero.marbles > 0:
                print("Congratulations, you won the game with 45,6 billions of south korean won !")
            else:
                print("HAHAHAHAHA, see you in hell !")


    @staticmethod
    def start(list_enemies, list_heroes):
        print("Game starting...")
        game = Game()
        game.__create_enemies(list_enemies)
        game.__create_heroes(list_heroes)
        game.__present_the_heroes()
        pass