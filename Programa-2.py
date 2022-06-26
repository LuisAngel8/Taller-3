import statsmodels.api as sm
import scipy.stats as ss
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def diferencia():
    print("¿Que experimento quiere cargar?")
    print("1. Experimento A")
    print("2. Experimento B")

    pick = int(input("Seleccione una opcion: "))
    
    if pick == 1:
        Exp_A = pd.read_csv(r"ExpA.csv")
        a = Exp_A["Sepal.Length"][Exp_A["Species"] == "setosa"]
        aa = Exp_A["Sepal.Width"][Exp_A["Species"] == "setosa"]
        b = Exp_A["Sepal.Length"][Exp_A["Species"] == "versicolor"]
        bb = Exp_A["Sepal.Width"][Exp_A["Species"] == "versicolor"]

        print("1. Diferencia del largo de sepalos entre Setosa & Versicolor")
        print("2. Diferencia del ancho de sepalos entre Setosa & Versicolor")
        
        pick = int(input("Seleccione una opcion: "))

        if pick == 1:
            Ttest = ss.ttest_ind(a,b)
            print("T Test diferencia del el largo de sepalos entre Setosa & Versicolor\n", Ttest)

            print("Enseñar Boxplot")
            print("1. Si")
            print("2. No")

            pick = int(input("Seleccione una opcion: "))

            if pick == 1:
                plt.figure()
                sns.boxplot(x = Exp_A["Species"], y = Exp_A["Sepal.Length"]).set(title = "largo de sepalos por especie")
                plt.show()
            else:
                exit
        
        elif pick == 2:
            ttestaa = ss.ttest_ind(aa,bb)
            print("T Test diferencia del el ancho de sepalos entre Setosa & Versicolor\n", ttestaa)

            print("Enseñar Boxplot")
            print("1. Si")
            print("2. No")

            pick = int(input("Seleccione una opcion: "))

            if pick == 1:
                plt.figure()
                sns.boxplot(x = Exp_A["Species"], y = Exp_A["Sepal.Width"]).set(title = "Ancho de sepalos por especie")
                plt.show()
            else:
                exit

    elif pick == 2:
        Exp_B = pd.read_csv(r"ExpB.csv")
        c = Exp_B["Petal.Length"][Exp_B["Species"] == "setosa"]
        cc = Exp_B["Petal.Width"][Exp_B["Species"] == "setosa"]
        d = Exp_B["Petal.Length"][Exp_B["Species"] == "virginica"]
        dd = Exp_B["Petal.Width"][Exp_B["Species"] == "virginica"]

        print("1. Diferencia del largo de petalos entre Setosa & Virginica")
        print("2. Diferencia del ancho de petalos entre Setosa & Virginica")
        
        pick = int(input("Seleccione una opcion: "))

        if pick == 1:
            TtestB = ss.ttest_ind(c,d)
            print("T Test: diferencia entre el largo de petalos entre Setosa & Virginica\n", TtestB)

            print("Enseñar Boxplot")
            print("1. Si")
            print("2. No")
            
            pick = int(input("Seleccione una opcion: "))

            if pick == 1:
                plt.figure()
                sns.boxplot(x = Exp_B["Species"], y = Exp_B["Petal.Length"]).set(title = "largo de petalos por especie")
                plt.show()

            else:
                exit

        elif pick == 2:
            TtestBb = ss.ttest_ind(cc,dd)
            print("T Test: diferencia entre el ancho de petalos entre Setosa & Virginica\n", TtestBb)

            print("Enseñar Boxplot")
            print("1. Si")
            print("2. No")
            
            pick = int(input("Seleccione una opcion: "))

            if pick == 1:
                plt.figure()
                sns.boxplot(x = Exp_B["Species"], y = Exp_B["Petal.Width"]).set(title = "Ancho de petalos por especie")
                plt.show()
            
            else:
                exit

    main()

def correlacion():
    print("¿Que experimento quiere sacar la correlacion?")
    print("1. Experimento A")
    print("2. Experimento B")

    pick = int(input("Seleccione un experimento"))

    if pick == 1:
        Exp_A = pd.read_csv(r"ExpA.csv")
        a = Exp_A["Sepal.Length"][Exp_A["Species"] == "setosa"]
        aa = Exp_A["Sepal.Width"][Exp_A["Species"] == "setosa"]
        b = Exp_A["Sepal.Length"][Exp_A["Species"] == "versicolor"]
        bb = Exp_A["Sepal.Width"][Exp_A["Species"] == "versicolor"]

        print("1. Pearson y Spearman entre Setosa (Largo de sepalo y ancho de sepalo)")
        print("2. Pearson y Spearman entre Versicolor (Largo de sepalo y ancho de sepalo)")
        
        pick = int(input("Seleccione una opcion: "))

        if pick == 1:
            PearsonA = ss.pearsonr(a,b)
            print("Correlación Pearson Exp A\n", PearsonA)
            SpearmanA = ss.spearmanr(a,b)
            print("Correlación Spearman Exp A\n", SpearmanA)

        elif pick == 2:
            PearsonAA = ss.pearsonr(aa,bb)
            print("Correlación Pearson Exp A\n", PearsonAA)
            SpearmanAA = ss.spearmanr(aa,bb)
            print("Correlación Spearman Exp A\n", SpearmanAA)
        else:
            exit

    elif pick == 2:
        Exp_B = pd.read_csv(r"ExpB.csv")
        c = Exp_B["Petal.Length"][Exp_B["Species"] == "setosa"]
        cc = Exp_B["Petal.Width"][Exp_B["Species"] == "setosa"]
        d = Exp_B["Petal.Length"][Exp_B["Species"] == "virginica"]
        dd = Exp_B["Petal.Width"][Exp_B["Species"] == "virginica"]

        print("1. Pearson y Spearman entre Setosa (Largo de sepalo y ancho de Petalo)")
        print("2. Pearson y Spearman entre Versicolor (Largo de sepalo y ancho de Petalo)")
        
        pick = int(input("Seleccione una opcion: "))

        if pick == 1:
            PearsonB = ss.pearsonr(c,d)
            print("Correlación Pearson Exp B\n", PearsonB)
            SpearmanB = ss.spearmanr(c,d)
            print("Correlación Spearman Exp B\n", SpearmanB)

        elif pick == 2:
            PearsonBB = ss.pearsonr(cc,dd)
            print("Correlación Pearson Exp B\n", PearsonBB)
            SpearmanBB = ss.spearmanr(cc,dd)
            print("Correlación Spearman Exp B\n", SpearmanBB)
        else:
            exit

    main()

def grafica():
    print("¿Que experimento quiere graficar?")
    print("1. Experimento A")
    print("2. Experimento B")

    pick = int(input("Seleccione un experimento: "))

    if pick == 1:
        Exp_A = pd.read_csv(r"ExpA.csv")
        a = Exp_A["Sepal.Length"][Exp_A["Species"] == "setosa"]
        aa = Exp_A["Sepal.Width"][Exp_A["Species"] == "setosa"]
        b = Exp_A["Sepal.Length"][Exp_A["Species"] == "versicolor"]
        bb = Exp_A["Sepal.Width"][Exp_A["Species"] == "versicolor"]
    
        print("¿Que especie quiere graficar?")
        print("1. Setosa")
        print("2. Versicolor")

        pick = int(input("Seleccione una opcion: "))

        if pick == 1:
            plt.figure()
            sns.regplot(x = a, y = aa, ci = 68, color = "salmon").set(title = "largo del petalo vs ancho del sepalo\n Setosa")
            plt.show()

        elif pick == 2:
            plt.figure()
            sns.regplot(x = b, y = bb, ci = 68, color = "pink").set(title = "largo del petalo vs ancho del sepalo\n versicolor")
            plt.show()
        else: 
            exit
        
    elif pick == 2:
        Exp_B = pd.read_csv(r"ExpB.csv")
        c = Exp_B["Petal.Length"][Exp_B["Species"] == "setosa"]
        cc = Exp_B["Petal.Width"][Exp_B["Species"] == "setosa"]
        d = Exp_B["Petal.Length"][Exp_B["Species"] == "virginica"]
        dd = Exp_B["Petal.Width"][Exp_B["Species"] == "virginica"]

        print("¿Que especie quiere graficar?")
        print("1. Setosa")
        print("2. Virginica")

        pick = int(input("Seleccione una opcion: "))

        if pick == 1:
            plt.figure()
            sns.regplot(x = c, y = cc, ci = 68, color = "g").set(title = "largo del petalo vs ancho del petalo\n Setosa")
            plt.show()

        elif pick == 2:
            plt.figure()
            sns.regplot(x = d, y = dd, ci = 68, color = "r").set(title = "largo del petalo vs ancho del petalo\n Virginica")
            plt.show()
        else:
            exit
    
    main()
    
def main():
    #Creación los experimentos
    iris = sm.datasets.get_rdataset("iris", "datasets")
    iris = pd.DataFrame(iris.data)
    
    #Experimento A
    objA = pd.DataFrame(iris, columns = ["Sepal.Length", "Sepal.Width","Species"])
    opc_A = ["setosa", "versicolor"]
    Exp_A = objA.loc[objA["Species"].isin(opc_A)]
    Exp_A.to_csv(r"ExpA.csv", index = False, header= True)
    
    #Experimento B
    objB = pd.DataFrame(iris, columns = ["Petal.Length", "Petal.Width","Species"])
    opc_B = ["setosa", "virginica"]
    Exp_B = objB.loc[objB["Species"].isin(opc_B)]
    Exp_B.to_csv(r"ExpB.csv", index = False, header= True)

    print("Opciones")
    print("1. Diferencia estadistica significativa")
    print("2. Correlacion de Pearson/ Spearman")
    print("3. Diagrama de dispersion + linea de regresion")
    print("4. Salir")

    pick = int(input("Seleccione una opcion: "))
    if pick == 1:
        diferencia()
    elif pick == 2:
        correlacion()
    elif pick == 3:
        grafica()
    else:
        print("Entendido")
        exit

main()