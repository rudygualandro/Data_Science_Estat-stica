import matplotlib.pyplot as plt
import pandas as pd
from pyod.models.knn import KNN

#ver biblioteca PyOD para deteccao de outliers

iris = pd.read_csv('iris.csv')

plt.boxplot(iris.iloc[:,1]) #os outliers aparecem no grafico
# boxplot, neste caso analisando a coluna "sepal width"

plt.boxplot(iris.iloc[:,1], showfliers = False) #boxplot sem os
#outliers

outliers = iris[(iris['sepal width'] > 4.0) | (iris['sepal width'] < 2.1)]
# busca os outliers

sepal_width = iris.iloc[:,1]
sepal_width = sepal_width.values.reshape(-1,1)
detector = KNN()
detector.fit(sepal_width)

previsoes = detector.labels_ #no resultado, os valores 1 são considerados outliers