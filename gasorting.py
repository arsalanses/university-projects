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
        
        self.genes = sorted(random.sample(list(range(100)), self.num)) # list(range(self.maxNum))

    def calcFitness(self, target):
        score = 0
        
        for i in range(len(self.genes)):
            if self.genes[i] == target[i]:
                score += 1
                continue
            for j in range(i):
                if self.genes[i] < self.genes[j]:
                    break
            else:
                score += 0.01
        
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
            child.genes[i] = partnerB.genes[i]
        else:
            child.genes[i] = partnerA.genes[i]
    
    return child

def mutate(child):
    for i in range(len(child.genes)):
        if random.random() < mutationRate:
            child.genes[i] = random.choice(target)
    return child

def draw():
    global isFinished
    # calcFitness
    averageFitness = 0
    bestGenes = population[1]
    for i in range(len(population)):
        fitness = population[i].calcFitness(target)
        averageFitness += fitness
        if bestGenes.fitness < population[i].fitness:
            bestGenes = population[i]
    averageFitness = round(averageFitness / len(population), 2)
    print("Average fitness: {}".format(averageFitness), end=" ")
    print("Best phrase: {}{}".format(bestGenes.genes, round(bestGenes.fitness, 2)))

    if bestGenes.genes == target:
        isFinished = True

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

while(not isFinished):
    print(totalGeneration, end=". ")
    draw()
    totalGeneration += 1
    
print("Total generation: {}".format(totalGeneration-1))
print("Total population: {}".format(totalPopulation))
print("Mutation rate: {}%".format(int(mutationRate * 100)))
