# -*- coding: utf-8 -*-

class CharacterStorage():
    def createCharacter(self, pc):
        raise NotImplementedError

    def deleteCharacter(self, accountName, charName):
        raise NotImplementedError

    def storeCharacter(self, pc):
        raise NotImplementedError

    def loadCharacter(self, charName):
        raise NotImplementedError