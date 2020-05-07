import numpy as np

def weighted_lottery(options):
    container_list = []

    for (name, weight) in options.items():
        for _ in range(weight):
            container_list.append(name)

    return np.random.choice(container_list)

options = {
    'green': 1,
    'yellow': 2,
    'red': 3,
}

print(weighted_lottery(options))