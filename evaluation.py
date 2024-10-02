from individual import Individual


def evaluate_all(individual_list: list[Individual]):
    for individual in individual_list:
        evaluate(individual)


def evaluate(individual: Individual):
    # TODO: this method compute fitness (based on TSP problem) and update fitness attribute of input individual (individual.fitness=new_fitness)
    # hint: as dr.ebadzade said in the class you can use -c to reverse fitness value c
    pass
