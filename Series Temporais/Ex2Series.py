import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from statsmodels.tsa.seasonal import seasonal_decompose

base = pd.read_csv('AirPassengers.csv')


dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)

ts = base['#Passengers']
          
plt.plot(ts)

decomposicao = seasonal_decompose(ts)
tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
aleatorio = decomposicao.resid #oq sobrou da tendencia e do sazonal

plt.plot(sazonal)
plt.plot(tendencia)
plt.plot(aleatorio)

plt.subplot(4,1,1) #os dois primeiros paramatros sao do tamanho de cada grafico
plt.plot(ts, label = 'Original') # o terceiro é o indice
plt.legend(loc = 'best')

plt.subplot(4,1,2)
plt.plot(tendencia, label = 'Tendência')
plt.legend(loc = 'best')

plt.subplot(4,1,3)
plt.plot(sazonal, label = 'Sazonalidade')
plt.legend(loc = 'best')

plt.subplot(4,1,4)
plt.plot(aleatorio, label = 'Aleatório')
plt.legend(loc = 'best')

plt.tight_layout() # da um espaço entre os graficos qd estao 
#amontoados