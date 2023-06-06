class RabbitPair:
    ID = 0
    def __init__(self, m):
        self.age = 0
        self.children = 0
        self.max_age = m
        self.__class__.ID += 1

    def is_sexually_mature(self):
        return self.age > 0

    def is_old(self):
        return self.age == self.max_age

    def increment_age(self):
        self.age += 1

    def reproduce(self):
        if self.is_sexually_mature():
            self.children += 1
        return RabbitPair(self.max_age)

    # def __del__(self):
    #     print(f"Rabbit Pair {self.id} has passed away.")

    def __str__(self):
        return f"Rabbit Pair {self.ID}\nCurrent age: {self.age}\nNumber of children: {self.children}"

def simulate_population(n, m):
    """ Returns a list of RabbitPair objects after n generations. RabbitPairs live for m months and reaches sexual maturity after 1 month. """
    population = [RabbitPair(m)]
    for gen in range(2, n+1):
        print(f"Generating generation {gen}...")
        for rabbit in population:
            print(rabbit)
            if rabbit.is_old():
                population.pop(rabbit)
            else:
                rabbit.increment_age()
                if rabbit.is_sexually_mature():
                    progeny = rabbit.reproduce()
                    population.append(progeny)
    return population
