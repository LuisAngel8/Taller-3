#Librerías
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

#Función
def main():
  opc = 0
  while opc != 6:
    print("""
      1. Exportar el conjunto de datos 'gapminder.xlsx' (El 10% de los valores son NaN).
      2. Importar el conjunto de datos 'gapminder.xlsx'.
      3. Mostrar gráfica de dispersión (log(lifeExp), log(pop)).
      4. Mostrar gráfica de dispersión (log(gdpPercap), log(pop)).
      5. Mostrar diagrama de cajas de gdpPercap por continente (1990 - 2007).
      6. Salir
      """)
    opc = int(input("Ingrese el número de la opción que desee: "))
    
    if opc == 1:
      #Inciso A. Exportar el dataframe de gapminder en formato .xlsx con el 10%
      #de los valores reemplazados por NaN valores.
      gapmind = sm.datasets.get_rdataset("gapminder", "causaldata") #Sirve para cargar datasets de r.
      gapminder = pd.DataFrame(gapmind.data) #Se crea el dataframe.

      porcentaje = int(len(gapminder)*0.1) #Cantidad de datos a reemplazar.
      secuencia = range(len(gapminder)) #Longitud de los datos.
      columns = ['lifeExp', 'pop', 'gdpPercap'] #Columnas con valores a reemplazar.

      for i in columns:
          row = random.sample(secuencia, porcentaje)
          gapminder.loc[row, i] = np.NaN

      gapminder.to_excel('gapminder.xlsx') #Se exporta el conjunto de datos.
      print("El archivo 'gapminder.xlsx' ha sido exportado.")

    elif opc == 2:
      #Inciso B. Importar el archivo gapminder en formato .xlsx.
      fil = pd.read_excel('gapminder.xlsx')
      file = fil.drop("Unnamed: 0", axis=1)
      print("El archivo 'gapminder.xlsx' ha sido importado.")
      print(file)

      print("CANTIDAD DE VALORES NaN EN CADA COLUMNA")
      count = file.isna().sum()
      print(count) #Contador de NaN values.

    elif opc == 3:
      print("Se ha generado el diagrama de distribución: ")
      #Inciso C. Graficar el diagrama de dispersión de LifeExp vs pop.
      #Almacenamiento de las columnas para la generación de las gráficas.
      lifeExp = gapminder['lifeExp']
      gdpPercap = gapminder['gdpPercap']
      pop = gapminder['pop']

      plt.figure()
      sns.scatterplot(x=np.log(lifeExp), y=np.log(pop), hue = gapminder['continent'], alpha = 0.3)
      plt.title('log(lifeExp) vs log(pop)')
      plt.show()

    elif opc == 4:
      print("Se ha generado el diagrama de distribución: ")
      #Inciso D. Graficar el diagrama de dispersión de gdpPercap vs pop.
      lifeExp = gapminder['lifeExp']
      gdpPercap = gapminder['gdpPercap']
      pop = gapminder['pop']

      plt.figure()
      sns.scatterplot(x=np.log(gdpPercap), y=np.log(pop), hue = gapminder['continent'], alpha = 0.3)
      plt.title('log(gdpPercap) vs log(pop)')
      plt.show()

    elif opc == 5:
      print("Se ha generado el diagrama de cajas: ")
      #Inciso E Graficar diagrama de cajas de gdpPercap por continentes entre el
      #1990  y 2007.
      gapminder.query('year >= 1990')
      gdpPercap = gapminder['gdpPercap']

      plt.figure()
      sns.boxplot(x = gapminder['continent'], y = np.log(gdpPercap))
      plt.show()
    elif opc == 6:
      print("¡Hasta luego!")
      #break
    else:
      print("Opción inválida. Vuelve a intentarlo.")
  
main()