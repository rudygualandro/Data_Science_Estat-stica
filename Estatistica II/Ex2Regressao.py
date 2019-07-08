import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm # cria modelos no python como se fosse R


base = pd.read_csv("mt_cars.csv")

base = base.drop(["Unnamed: 0"], axis = 1) 

X = base.iloc[:, 2].values

Y = base.iloc[:, 0].values

correlacao = np.corrcoef(X, Y)

X = X.reshape(-1, 1) # o -1 significa não mexer nas linhas, o 1 significa adicionar
# 1 coluna

modelo = LinearRegression()
modelo.fit(X, Y)

modelo.intercept_
modelo.coef_

modelo.score(X,Y) #mostra o quanto a var explicativa explica a var resposta
# é o r ao quadrado

previsoes = modelo.predict(X) #mostra os valores previstos para cada X, sendo que
# Y são os valores reais

modelo_ajustado = sm.ols(formula = 'mpg ~ disp', data = base) # faz o mesmo que
# .score, mas de maneira ajustada

modelo_treinado = modelo_ajustado.fit()

modelo_treinado.summary()

plt.scatter(X,Y)
plt.plot(X, previsoes, color = "red")

modelo.predict(200)


#segunda linha de regressão (múltipla)
X1 = base.iloc[:, 1:4].values
Y1 = base.iloc[:, 0].values

modelo2 = LinearRegression()
modelo2.fit(X1, Y1)

modelo2.score(X1, Y1)
modelo_ajustado2 = sm.ols(formula = 'mpg ~ cyl + disp + hp', data = base)
modelo_treinado2 = modelo_ajustado.fit()
modelo_treinado2.summary() #exibe varias caracteristicas da linha de regressao


# fazer previsao com base em determinado parametro
novo = np.array([4, 200, 100])
novo = novo.reshape(1, -1)

modelo2.predict(novo)


