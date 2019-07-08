from scipy import stats
from scipy.stats import binom, norm, t
import matplotlib.pyplot as plt

#jogar a moeda 5 vezes e dar 3 caras

prob = binom.pmf(3, 5, 0.5) #(n de sucessos, n de tentativas, prob de sucesso)

binom.cdf(4, 5, 0.5) #probabilidade cumulativa

prob * 100 #mostrar em porcentagem

#DISTRIBUIÇAO NORMAL

#numa distribuicao normal, uma cesta de objetos de diversos pesos, com média 8
# e desvio padrao (standard deviation) 2, qual é a probabilidade de tirar um
# objeto com menos de 6 kg?

norm.cdf(6, 8, 2)

# mais de 6 kilos

norm.sf(6, 8, 2) #survival function

dados = norm.rvs(size = 100) #gera 100 elementos em distribuicao normal
stats.probplot(dados, plot = plt)

stats.shapiro(dados) #teste de shapiro

# t de student
#media de salarios dos cientistas é 75, com desvio 10. fazendo uma pesquisa com
# 9 cientistas, qual é a probabilidade de achar um com salario abaixo de 80

t.cdf(1.5, 8) #o 1.5 é tirado de uma tabela. O numero 8 é 9 -1, devido ao grau
# de liberdade

t.sf(1.5, 8)

ex2 = binom.pmf(4, 4, 0.5) 

print(ex2 * 2)

print(norm.cdf(6, 8, 4))

ex3 = binom.pmf(3, 6, 0.25)