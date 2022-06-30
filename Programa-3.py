# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 13:08:00 2022

@author: USUARIO
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats        

def main():
    val = 0
    while val !=5 :
        #Aqui se muestra la interfaz inicial del programa
      print("1. Graficar la funcion de densidad de una distribucion uniforme")
      print("2. Graficar la funcion de densidad de una distribucion Bernoulli (Binomial)")
      print("3. Graficar la funcion de densidad de una distribucion Poisson")
      print("4. Graficar la funcion de densidad de una distribucion Exponencial")
      print("5. SALIR DEL PROGRAMA")
      print("AVISO : Los valores a graficar vendran de forma predeterminada para algunas distribuciones")
      #Este comando le permite al usuario elegir que grafica desea visualizar
      val = int(input("Ingrese un valor: "))
      
      if val == 1:
        #Grafica funcion de distribucion Uniforme ( )
        #pdf(x, loc=0, scale=1)
            print("Usted selecciono graficar una funcion de densidad de una distribucion uniforme") 
            x1 = np.arange(-8, 8, 0.1)
            minimo = int(input("Ingrese el valor minimo de la distribucion: "))
            maximo = int(input("Ingrese el valor maximo de la distribucion: "))
            #Si el valor minimo es mayor al valor maximo el programa le pedira al usuario de nuevo los valores
            while (minimo > maximo):
              print("Los valores de minimos no deben ser mayores a los maximos")
              minimo = int(input("Ingrese el valor minimo de la distribucion: "))
              maximo = int(input("Ingrese el valor maximo de la distribucion: "))
            #Se realizan los calculos de la funcion 
            a = stats.uniform.pdf(x1, minimo, maximo-minimo)
            a
            #Se realiza la grafica de la distribucion uniforme
            plt.plot(x1,a)
            plt.title('Distribución Uniforme')
            plt.ylabel('probabilidad')
            plt.xlabel('valores')
            plt.show()
              
      elif val == 2:
        #Grafica funcion de distribucion Bernoulli ()
          #pmf(k, p, loc=0)
              print("Usted selecciono graficar una funcion de densidad de una distribucion Bernoulli (Binomial)")
              #Valor predeterminado de X
              x2= np.arange(10)
              PROB1 = int(input("Ingrese la probabilidad de exito (%): "))
              PROB2 = PROB1/100
              print(PROB2)
              while (PROB2 < 0 or PROB2 > 1):
                print("Ingrese una probabilidad de exito correcta")
                PROB1 = int(input("Ingrese la probabilidad de exito (%): "))
                PROB2 = PROB1/100
              #Se realizan los calculos de la funcion 
              b= stats.bernoulli.pmf(x2, PROB2)
              b
              #Se realiza la grafica de la distribucion de Bernoulli
              plt.plot(x2, b)
              plt.show()
    
      elif val == 3:
        #Grafica funcion de distribucion Poisson (poisson)
             #pmf(k, mu, loc=0)
             print("Usted selecciono graficar una funcion de densidad de una distribucion Poisson")
             #Valor predeterminado de X 
             x3 = np.arange(0,50)
             LAMBDA = int(input("Ingrese el numero medio esperado de eventos (lambda): "))
             while (LAMBDA < 0):
               print("Ingrese un numero correcto de eventos esperados")
               LAMBDA = int(input("Ingrese el numero medio esperado de eventos (lambda): "))
             #Se realizan los calculos de la funcion 
             c= stats.poisson.pmf(x3, LAMBDA)
             c
             #se realiza la grafica de la distribucion de Poisson
             plt.plot(x3, c)
             plt.title('Distribución Poisson')
             plt.ylabel('probabilidad')
             plt.xlabel('valores')
             plt.show()
    
      elif val == 4:
        #Grafica funcion de deistribucion Exponencial (expon)
          #pdf(x, loc=0, scale=1)
          print("Usted selecciono graficar una funcion de densidad de una distribucion Exponencial")
          #Valor predeterminado de X
          x4= np.arange(0,20)
          #Se realizan los calculos de la funcion 
          d= stats.expon.pdf(x4)
          d
          #Se realiza la grafica de la distribucion exponencial
          plt.plot(x4,d)
          plt.title('Distribución Exponencial')
          plt.ylabel('probabilidad')
          plt.xlabel('valores')
          plt.show()
         