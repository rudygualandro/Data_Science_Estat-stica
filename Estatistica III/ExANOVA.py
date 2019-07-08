import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

#teste de hipotese para saber se a diferença entre os dois grupos observados eh
#significativa ou por acaso
# entre 2 grupos se usa o teste t de student
# mais de 2 grupos se usa o ANOVA

tratamento = pd.read_csv('anova.csv', sep = ';')

tratamento.boxplot(by = 'Remedio', grid = False) #tira as linhas de grade

modelo1 = ols('Horas ~ Remedio', data = tratamento).fit() #regressão com Horas como var resposta
# e Remedio como var explicativa

resultados1 = sm.stats.anova_lm(modelo1)

modelo2 = ols('Horas ~ Remedio * Sexo', data = tratamento).fit() 
resultados2 = sm.stats.anova_lm(modelo2)


#teste de tukey comparando cada grupo

mc = MultiComparison(tratamento['Horas'], tratamento['Remedio'])
resultado_teste = mc.tukeyhsd()
print(resultado_teste)

resultado_teste.plot_simultaneous()