import random
import string

def newChar():
    # ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    # ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # digits = '0123456789'
    # hexdigits = '0123456789abcdefABCDEF'
    # octdigits = '01234567'

    c = list(string.ascii_letters)
    # c = list(range(10))
    return random.choice(c)

class DNA:
    genes = list()
    fitness = 0
    
    def __init__(self, num):
        self.genes = [newChar() for i in range(num)]
        
    def getPhrase(self):
        return ''.join(self.genes)

    def calcFitness(self, target):
        score = 0
        for i in range(len(target)):
            if self.genes[i] == target[i]:
                score += 1
        
        self.fitness = score / len(target)

        return self.fitness

    def crossover(self, partner):
        child = DNA(len(self.genes))
        midpoint = random.randint(0, len(self.genes))

        for i in range(len(self.genes)):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        
        return child

    def mutate(self, mutationRate):
        for i in range(len(self.genes)):
            if random.random() < mutationRate:
                self.genes[i] = newChar()
