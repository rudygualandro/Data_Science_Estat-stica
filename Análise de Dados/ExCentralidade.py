import numpy as np
from scipy import stats

jogadores = [10000, 40000, 20000, 55000, 13000, 33000, 36000, 25000, 80000]

np.mean(jogadores)

np.median(jogadores)

quartis = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1])

np.std(jogadores) #standard deviation

stats.describe(jogadores)

print(quartis)

ex1 = [1041, 881, 1007, 895, 761, 1036, 1114, 980, 970, 1062]

np.std(ex1)

quartis1 = np.quantile(ex1, [0, 0.25, 0.5, 0.75, 1])

print(quartis1)