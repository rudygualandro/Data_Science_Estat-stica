import numpy as np
from scipy.stats import chi2_contingency

# o objetivo do quiquadrado é dizer se, em determinados daods,
# a diferenca entre homens e mulheres que
#assistem novela eh significativa ou se soh obra do acaso, com base na proporcao
#encontrada e na proporcao esperada
# é um tipo de teste de hipótese

novela = np.array([[19,6], [43,32]])

chi2_contingency(novela)

#no resultado, oq interesse é o segundo parametro, que eh o valor de P
# neste caso deu 0.15 é maior q o alpha de 0.05, então nao podemos rejeitar a
#hipotese nula, ou seja, nao ha diferenca significativa alem do acaso