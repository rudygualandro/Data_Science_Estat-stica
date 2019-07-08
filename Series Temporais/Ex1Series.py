import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime

base = pd.read_csv('AirPassengers.csv')

#os dados da base contem os passageiros como inteiro e os Month como
# "object". Esse object deve ser convertido em tipo data:

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)

#os indices de cada dado passa a ser uma data

base.index

ts = base['#Passengers'] #os dados dessa var sao do tipo series
 
#formas de chamar os dados pelo indice          
ts[1]
ts['1949-02']
ts[datetime(1949,2,1)]
ts['1950-01-01': '1950-07-31']
ts[:'1950-07-31']
ts['1950']

#achar o maior e o menor valor
ts.index.max()
ts.index.min()

plt.plot(ts)

#agrupamento por ano. O 'A' é um parametro do resample
# quer significa ano

ts_ano = ts.resample('A').sum()

plt.plot(ts_ano)

#por mes
ts_mes = ts.groupby([lambda x: x.month]).sum()
plt.plot(ts_mes)

#por datas

ts_datas = ts['1960-01-01': '1960-12-01']
plt.plot(ts_datas)







