import pandas as pd # importa la librería pandas y la asigna a la variable pd

datos_consumo = pd.read_excel('datos.xlsx') # indicamos el nombre de nuestro archivo a ser leído

print("--PRIMEROS 5 DATOS--")
print(datos_consumo.head())#MOSTRAR LOS PRIMEROS 5 DATOS


print("\n\n--Datos contados por MOMENTO--")
print(datos_consumo.groupby("Momento").count()) # con la función groupby agrupamos los datos de la columna Momento y con count() los contamos para obtener subtotales


print("\n\n--ESTADISTICA DESCRIPTIVA--")
print(datos_consumo.describe())#MOSTRAR ESTADISTICA DESCRITIVA


print("\n\n--DATOS A ANALIZAR--")
datos_seleccionados = datos_consumo.iloc[:,3:8] # : selecciona todas las filas y 3:8(-1) seleccion columnas de la 4 la 7
print(datos_seleccionados) # desplegamos el dataframe


print("\n\n--INFO DE LOS DATOS A ANALIZAR--")
datos_seleccionados.info()


print("\n\n--LIMPIANDO DATOS--")
datos_seleccionados.isnull().values.any() # buscamos valores nulos y obtenemos True o False dependiendo si hay o no
dataset = datos_seleccionados.dropna() # creamos un nuevo dataframe descartando los valores nulos o vacíos de nuestro dataframe datos_seleccionados
print(dataset.isnull().sum()) # validamos que no tenemos valores nulos en ninguna columna, todos deben dar cero


print("\n\n--PREPARADNO LOS DATOS--")
print(dataset.columns) # vemos los nombres de nuestras columnas para asignarlos a las variables
X = dataset[['Carbohidratos (g)', 'Lípidos/grasas (g)', 'Proteína (g)', 'Sodio (mg)']].values # variables independientes
y = dataset['Calorías (kcal)'].values # variable dependiente

from sklearn.model_selection import train_test_split # importamos la herramienta para dividir los datos de SciKit-Learn
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) # asignación de los datos 80% para entrenamiento y 20% para prueba


print("\n\n--MODELACION DE LOS DATOS--")
from sklearn.linear_model import LinearRegression # importamos la clase de regresión lineal
modelo_regresion = LinearRegression() # modelo de regresión

modelo_regresion.fit(X_train, y_train) # aprendizaje automático con base en nuestros datos

x_columns = ['Carbohidratos (g)', 'Lípidos/grasas (g)', 'Proteína (g)', 'Sodio (mg)']
coeff_df = pd.DataFrame(modelo_regresion.coef_, x_columns, columns=['Coeficientes'])
print(coeff_df) # despliega los coefientes y sus valores; por cada unidad del coeficente, su impacto en las calorías será igual a su valor

y_pred = modelo_regresion.predict(X_test) # probamos nuestro modelo con los valores de prueba


print("\n\n--PROBAMOS EL MODELO--")
validacion = pd.DataFrame({'Actual': y_test, 'Predicción': y_pred, 'Diferencia': y_test-y_pred }) # creamos un dataframe con los valores actuales y los de predicción

muestra_validacion = validacion.head(25) # elegimos una muestra con 25 valores 
print(muestra_validacion) # desplegamos esos 25 valores


print("\n\n--ESTADISTICA Y PRECISION DEL MODELO--")
print(validacion["Diferencia"].describe())
from sklearn import metrics # importamos las métricas
import numpy as np

print("\nRaíz de la desviación media al cuadrado:", np.sqrt(metrics.mean_squared_error(y_test, y_pred))) # imprimimos la raíz de la desviación media al cuadrado


print("-----------------------------------------------------------------------------")
import matplotlib.pyplot as plt # importamos la librería que nos permitirá graficar
muestra_validacion.plot.bar(rot=0)  # creamos un gráfico de barras con el dataframe que contiene nuestros datos actuales y de predicción
plt.title("Comparación de calorías actuales y de predicción") # indicamos el título del gráfico
plt.xlabel("Muestra de alimentos") # indicamos la etiqueta del eje de las x, los alimentos
plt.ylabel("Cantidad de calorías") # indicamos la etiqueta del eje de las y, la cantidad de calorías
plt.show() # desplegamos el gráfico