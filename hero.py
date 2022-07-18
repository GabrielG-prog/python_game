from character import Character
from utils import Utils

from data import heros

class Hero(Character):

    nrb_hero_created = 0

    def __init__(self, name = "", marbles = 0, loss = 0, gain = 0, scream_war = ""):
        super().__init__(name, marbles)
        self.loss = loss
        self.gain = gain
        self.scream_war = scream_war
        Hero.nrb_hero_created += 1
        print(f"Hero n°{Hero.nrb_hero_created} created ! ")

    @property
    def loss(self):
        return self.__loss

    @property
    def gain(self):
        return self.__gain

    @property
    def scream_war(self):
        return self.__scream_war

    @loss.setter
    def loss(self, loss):
        self.__loss = loss

    @gain.setter
    def gain(self, gain):
        self.__gain = gain

    @scream_war.setter
    def scream_war(self, scream_war):
        self.__scream_war = scream_war

    def introduce(self):
        print(f"{self.name} will start the game with {self.marbles} marbles, "
              f"a bonus of {self.gain} marbles and a malus of {self.loss} marbles")
        pass

    def chose_skills(self):

        msg = ""
        for idx, hero in enumerate(heros):
            msg += f"Press ({idx + 1}) for {hero['name']} "

        hero_choice = Utils.read_number(msg, 1, 3)

        self.name = heros[hero_choice - 1]["name"]
        self.marbles = heros[hero_choice - 1]["marbles"]
        self.loss = heros[hero_choice - 1]["loss"]
        self.gain = heros[hero_choice - 1]["gain"]
        self.scream_war = heros[hero_choice - 1]["scream_war"]

    def chose_level_of_dificulty(self):

        msg = "Please chose a level of dificulty \n " \
              "(1) - easy\n " \
              "(2) - Hard \n " \
              "(3) - Impossible"

        return Utils.read_number(msg, 1, 3)

    def cheat(self):
        pass

    def chose_odd_or_even(self):
        pass

    def win(self):
        pass

    def lose(self):
        pass

    def scream(self):
        pass