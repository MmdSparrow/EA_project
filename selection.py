from individual import Individual


def select_two_individual_for_crossover(
    individual_list: list[Individual], population_size: int
) -> tuple[Individual, Individual]:
    # TODO: this method selects two individuals for the crossover algorithm
    pass


def next_generation_selection(
    individual_list: list[Individual], population_size: int
) -> list[Individual]:
    # TODO: this method selects a total of population_size individuals from the individual_list for the next generation
    # hint: individual_list might contain only the new generation (mu, landa) or the new generation along with the population (mu + landa)
    pass
