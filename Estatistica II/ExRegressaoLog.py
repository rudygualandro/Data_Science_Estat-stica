
#este ex é para ver a probalidade de um candidato ser eleito com base no inves-
#mento de campanha 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

base = pd.read_csv('Eleicao.csv', sep = ';') # o parametro sep =';' deve ser colocado
#pq no arquivo csv as informacoes estao separadas por ; e nao virgula

plt.scatter(base.DESPESAS, base.SITUACAO) #base.DESPESAS acessa diretamente a
#coluna do csv sem precisar do iloc. Mostra os candidatos que foram e nao foram
#eleitos

base.describe() #mostra algumas informacoes dos dados

np.corrcoef(base.DESPESAS, base.SITUACAO)

X = base.iloc[:,2].values
X = X[:, np.newaxis] #outra forma de fazer o reshape e colocar outra coluna

Y = base.iloc[:,1].values

modelo = LogisticRegression()
modelo.fit(X,Y)

modelo.coef_
modelo.intercept_

plt.scatter(X,Y)

X_teste = np.linspace(10, 3000, 100)

def model(x): # retorna funcao sigmoide
    
    return 1 / (1 + np.exp(-x))

r = model(X_teste * modelo.coef_ + modelo.intercept_).ravel() #o ravel transforma
# o array em formato de vetor. Esta funcao calcula o erro que o modelo gera e será
# usado para plotar o grafico
plt.plot(X_teste, r, color = 'red')


# com base no modelo, fazer previsao para novos candidatos:
base_previsoes = pd.read_csv('NovosCandidatos.csv', sep = ';')
despesas = base_previsoes.iloc[:, 1].values
despesas = despesas.reshape(-1,1)
previsoes_teste = modelo.predict(despesas)

#para concatenar os dados do valor investido e se o candidato
#vai ou nao ganhar. 
base_previsoes = np.column_stack((base_previsoes, previsoes_teste)) # digitar
# base_previsoes diretamente no console caso de erro no spyder

print(base_previsoes)

