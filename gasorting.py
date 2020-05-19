import random

user_list = random.sample(list(range(100)), 50)

target = sorted(user_list)

totalPopulation = 150

class DNA:
    genes = list()
    fitness = 0

    def __init__(self, num, maxNum):
        self.num = num
        self.maxNum = maxNum
        
        self.genes = random.sample(list(range(self.maxNum)), self.num)

    def calcFitness(self, target):
        score = 0
        
        for i in range(len(self.genes)):
            if self.genes[i] == target[i]:
                score += 1
        
        self.fitness = score / len(target)

        return self.fitness

population = list()

for i in range(totalPopulation):
    population.append(DNA(len(target), max(target)))

for i in range(len(population)):
    population[i].calcFitness(target)

for i in population:
    print(i.fitness)