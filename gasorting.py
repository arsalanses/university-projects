from DNA import *
import random
import math

totalPopulation = 150
mutationRate = 0.01

# target = sorted(range(10))
target = 'arsalan'
population = list()

finished = False
totalGeneration = 0

def setup():
    for i in range(totalPopulation):
        population.append(DNA(len(target)))

def draw():
    global finished

    averageFitness = 0
    best = population[1]
    for i in range(len(population)):
        fitness = population[i].calcFitness(target)
        averageFitness += fitness
        if fitness > best.fitness:
            best = population[i]
    
    averageFitness = round(averageFitness / len(population), 2)
    print("{}. Average fitness: {}".format(totalGeneration, averageFitness), end=" ")
    print("Best phrase: {} {}".format(best.genes, round(best.fitness, 2)))

    finished = True if best.fitness == 1 else False

    # matingPool
    matingPool = list()
    for i in range(len(population)):
        n = math.floor(population[i].fitness * 100)
        for j in range(n):
            matingPool.append(population[i])

    for i in range(len(population)):
        partnerA = random.choice(matingPool)
        partnerB = random.choice(matingPool)
        child = partnerA.crossover(partnerB)
        child.mutate(mutationRate)
        population[i] = child

def main():
    global totalGeneration
    
    print("Target: {}".format(target))

    setup()

    while(not finished):
        draw()
        totalGeneration += 1

    print("Total generations: {}".format(totalGeneration))
    print("Total population: {}".format(totalPopulation))
    print("Mutation rate: {}%".format(math.floor(mutationRate * 100)))

if __name__ == '__main__':
    main()
