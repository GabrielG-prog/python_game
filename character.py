from abc import ABC, abstractmethod
class Character:

    def __init__(self, name, marbles, dead = False):
        self.name = name
        self.marbles = marbles
        self.dead = dead

    @property
    def name(self):
        return self.__name

    @property
    def marbles(self):
        return self.__marbles

    @property
    def dead(self):
        return self.__dead

    @name.setter
    def name(self, name):
        self.__name = name

    @marbles.setter
    def marbles(self, marbles):
        self.__marbles = marbles

    @dead.setter
    def dead(self, dead):
        self.__dead = dead

    @abstractmethod
    def win(self):
        pass

    @abstractmethod
    def lose(self):
        pass