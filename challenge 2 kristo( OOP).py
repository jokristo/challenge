#coding: utf-8
from random import random

class ManySentences:
    def __init__(self):
        self.list_sujet = []
        self.list_verbs = []
        self.list_complements = []
        self.phrase = input("entrez votre phrase : ")

    def demander_info(self):
        i = 0
        while i <= 1 :
            sujet = input("entrer un autre sujet : ")
            verbe = input("entrer un autre verbe : ")
            complement = input("entrer un autre complement : ")
            self.list_sujet.append(sujet)
            self.list_verbs.append(verbe)
            self.list_complements.append(complement)
            i += 1
        print(self.phrase)
        print(self.list_sujet[0], self.list_verbs[1],  self.list_complements[0])
        print(self.list_sujet[1], self.list_verbs[0], self.list_complements[1])
        print(self.list_sujet[0], self.list_verbs[0], self.list_complements[0])




sentence = ManySentences()
sentence.demander_info()









