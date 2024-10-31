import random

from individual import Individual
from evaluation import evaluate, evaluate_all
from selection import next_generation_selection


def run_algorithm(
    distance_matrix,
    population_size=20,
    generation_size=30,
):
    MUTATION_RATE = 0.3
    genome_size = len(distance_matrix)

    # create primary population
    population = primary_population_creator(population_size, genome_size)

    while True:
        # cross over
        generated_individuals = []
        for _ in range(int(generation_size / 2)):
            # TODO
            pass

        # mutation
        for individual in generated_individuals:
            # TODO: by using a random number and 'MUTATION_RATE', decide whether to mutate the individual or not    
            pass

        # TODO: evaluate generated_individuals

        # TODO: select next generation by use of 'next_generation_selection' method

        # TODO: check termination condition on generated individuals

        # TODO: redefine 'population' for the next iteration

        random.shuffle(population)


def primary_population_creator(
    population_size: int, genome_size: int
) -> list[Individual]:
    # TODO: this method create primary individual based on input population size and return them as list of individuals
    pass
