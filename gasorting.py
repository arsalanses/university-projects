import random
import math

# user_list = random.sample(list(range(100)), 50)
user_list = range(10)

target = sorted(user_list)

totalPopulation = 150
mutationRate = 0.01

population = list()

isFinished = False
totalGeneration = 1

class DNA:
    genes = list()
    fitness = 0

    def __init__(self, num, maxNum):
        self.num = num
        self.maxNum = maxNum if maxNum >= num else num
        
        self.genes = random.sample(list(range(self.maxNum)), self.num)

    def calcFitness(self, target):
        score = 0
        
        for i in range(len(self.genes)):
            if self.genes[i] == target[i]:
                score += 1
        
        self.fitness = score / len(target)

        return self.fitness

def setup():
    for i in range(totalPopulation):
        population.append(DNA(len(target), max(target)))

def crossover(partnerA, partnerB):
    child = DNA(len(target), max(target))

    midpoint = random.randint(0, len(partnerA.genes))

    for i in range(len(partnerA.genes)):
        if i > midpoint:
            child.genes[i] = partnerA.genes[i]
        else:
            child.genes[i] = partnerB.genes[i]
    
    return child

def mutate(child):
    for i in range(len(child.genes)):
        if random.random() < mutationRate:
            child.genes[i] = random.choice(target)
    return child

def draw():
    # calcFitness
    averageFitness = list()
    for i in range(len(population)):
        averageFitness.append(population[i].calcFitness(target))
    averageFitness = round(sum(averageFitness) / len(averageFitness), 2)
    print("Average fitness: {}".format(averageFitness))

    # matingPool
    matingPool = list()
    for i in range(len(population)):
        n = math.floor(population[i].fitness * 100)
        for j in range(n):
            matingPool.append(population[i])

    for i in range(len(population)):
        partnerA = random.choice(matingPool)
        partnerB = random.choice(matingPool)
        child = crossover(partnerA, partnerB)
        child = mutate(child)
        population[i] = child

print("Target: {}".format(target))

setup()

counter = 1
while(not isFinished):
    print(counter, end=". ")
    draw()

    for i in population:
        if i.genes == target:
            isFinished = True
            print("Best phrase: {}".format(i.genes))
            break
    else:
        totalGeneration += 1
    
    counter += 1

print("Total generation: {}".format(totalGeneration))
