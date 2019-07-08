import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

base = pd.read_csv("cars.csv")

base = base.drop(["Unnamed: 0"], axis = 1) #o axis=1 quer dizer apagar a coluna
#Unnamed

X = base.iloc[:,1].values #transforma no formato numpy array, oq será necessário
# para aplicar a funcao fit

X = X.reshape(-1, 1) #transforma em formato de matriz para a funçao fit, para fazer
#a regressao linear

Y = base.iloc[:,0].values #é a variável resposta

correlacao = np.corrcoef(X, Y) #para executar esse comando, os dados nao podem 
#estar no formato do reshape (matriz), mas sim no formato original

modelo = LinearRegression()#instancia um objeto LinearRegression
modelo.fit(X, Y)#encaixa os dados de x e y no modelo; faz o treinamento do modelo

modelo.intercept_ #indica onde a linha de regressao intercepta o eixo Y

modelo.coef_ #indica a inclinação da linha

plt.scatter(X,Y)
plt.plot(X, modelo.predict(X), color = "red")#o método predict traz os dados que 
# o algoritmo previu a partir dos dados reais de X

# prever  a velocidade para o valor distancia = 22 pés. tem duas formas:
modelo.intercept_ + modelo.coef_ * 22

# ou de modo mais direto:


modelo.predict(22)

# residuos da linha de regressao:

modelo._residues


#outra forma de visualizar pela biblioteca Yellowbrick

visualizador = ResidualsPlot(modelo) #cria objeto ResidualsPlot
visualizador.fit(X,Y)
visualizador.poof()
