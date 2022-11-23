import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def menu():
    print("\t<-------------------MENU------------------->")
    print("\t0. Mostrar csv")
    print("\t1. Reporte de hombres y mujeres vacunados")
    print("\t2. Reporte por grupo de edad vacunados")
    print("\t3. Busqueda por ubigeo del Reniec")
    print("\t4. Dividir por trimestre")
    print("\t5. Cantidad de hombres y mujeres vacunados por Diresa")
    print("\t6. Salir")

def csv_report(df):
    print(df)

def reporte_hombres_y_mujeres(df):
    print("\t<Cantidad de Hombres y Mujeres vacunados>")
    canti_f=len(df[df["Sexo"]=="F"])
    canti_m=len(df[df["Sexo"]=="M"])
    print(f"La cantidad de mujeres es {canti_f} mientras que la cantidad de hombres es {canti_m}")
    #grafica
    n=''
    print()
    while n=='':
        n=str(input("Desea ver la grafica [Si] [No]:> "))
    if n=='Si':
         # grafico torta
         sexo = ['Mujeres', 'Hombres']
         valores = [canti_f, canti_m]
         fig1, ax1 = plt.subplots()
         ax1.pie(valores, labels=sexo, autopct='%1.1f%%',
                 shadow=True, startangle=90)
         ax1.axis('equal')  
         ax1.set_title("Figura 1. Cantidad de hombres y mujeres vacunados \n respecto al total de dosis entre el 1/01/2022 - 30/09/2022")  
         ax1.legend(title='Sexo color')
         ax1.set_xlabel("Fuente: https://www.minsa.gob.pe/reunis/data/vacunas-covid19.asp")
         plt.show()
def menu_reporte_grupo_edad():
    print("<---Grupo de edad por Diresa--->")
    print("1. DIRIS Lima sur")
    print("2. DIRIS Lima norte")
    print("3. DIRIS Lima este")
    print("4. DIRIS Lima centro")
    print("5. DIRIS provincia")

def reporte_grupo_edad(df):
    #cantidad por age group
    #la clasificacion fue hecha por el REUNIS (repositorio unico nacional de informacion en salud)
    print("<Separacion por grupos de edad>")
    print("Total de grupos de edad :>  9 ")
    print("Personas en el grupo -1 :> ", len(df[df["Grupo Edad"]==-1]))
    print("Personas en el grupo  0 :> ", len(df[df["Grupo Edad"]==0]))
    print("Personas en el grupo  1 :> ", len(df[df["Grupo Edad"]==1]))
    print("Personas en el grupo  2 :> ", len(df[df["Grupo Edad"]==2]))
    print("Personas en el grupo  3 :> ", len(df[df["Grupo Edad"]==3]))
    print("Personas en el grupo  4 :> ", len(df[df["Grupo Edad"]==4]))
    print("Personas en el grupo  5 :> ", len(df[df["Grupo Edad"]==5]))
    print("Personas en el grupo  6 :> ", len(df[df["Grupo Edad"]==6]))
    print("Personas en el grupo  7 :> ", len(df[df["Grupo Edad"]==7]))
    print("Personas en el grupo  8 :> ", len(df[df["Grupo Edad"]==8]))
    print("Personas en el grupo  9 :> ", len(df[df["Grupo Edad"]==9]))
    #grafica
    plt.rcdefaults()
    fig, ax = plt.subplots()
    grupo_edad = ('6-11m', '01-04a', '05-11a', '12-17a', '18-29a', '30-39a', '40-49a', '50-59a', '60-69a', '70-79a', '80a>')
    y_pos = np.arange(len(grupo_edad))
    canti_grupo = [len(df[df["Grupo Edad"]==-1]), len(df[df["Grupo Edad"]==0]), len(df[df["Grupo Edad"]==1]), 
                                        len(df[df["Grupo Edad"]==2]), len(df[df["Grupo Edad"]==3]), 
                                        len(df[df["Grupo Edad"]==4]), len(df[df["Grupo Edad"]==5]), 
                                        len(df[df["Grupo Edad"]==6]), len(df[df["Grupo Edad"]==7]),
                                        len(df[df["Grupo Edad"]==8]), len(df[df["Grupo Edad"]==9])]
    hbr=ax.barh(y_pos, canti_grupo, align='center', color="skyblue")
    ax.set_yticks(y_pos, labels=grupo_edad)
    ax.invert_yaxis() 
    ax.bar_label(hbr,padding=3)
    ax.set_title('Figura 2. Cantidad de vacunados segun su grupo de edad')
    ax.set_xlabel("Cantidad de personas \n Fuente: https://www.minsa.gob.pe/reunis/data/vacunas-covid19.asp")
    plt.show()
    n=''
    print()
    while n=='':
        n=str(input("Deseas seguir filtrando? [Si] [No]:> "))
    if n=='Si':
        escoge=-1
        menu_reporte_grupo_edad()
        while escoge<=0:
            escoge=int(input("Escoge filtro por diresa:> "))
        if escoge==1:
            grup_6_11m=len(df[(df["Grupo Edad"]==-1) & (df.Diresa=="LIMA DIRIS SUR")])
            grup_1_4a=len(df[(df["Grupo Edad"]==0) & (df.Diresa=="LIMA DIRIS SUR")])
            grup_5_11a=len(df[(df["Grupo Edad"]==1) & (df.Diresa=="LIMA DIRIS SUR")])
            grup_12_17a=len(df[(df["Grupo Edad"]==2) & (df.Diresa=="LIMA DIRIS SUR")])
            grup_18_29a=len(df[(df["Grupo Edad"]==3) & (df.Diresa=="LIMA DIRIS SUR")])
            grup_30_39a=len(df[(df["Grupo Edad"]==4) & (df.Diresa=="LIMA DIRIS SUR")])
            grup_40_49a=len(df[(df["Grupo Edad"]==5) & (df.Diresa=="LIMA DIRIS SUR")])
            grup_50_59a=len(df[(df["Grupo Edad"]==6) & (df.Diresa=="LIMA DIRIS SUR")])
            grup_60_69a=len(df[(df["Grupo Edad"]==7) & (df.Diresa=="LIMA DIRIS SUR")])
            grup_70_79a=len(df[(df["Grupo Edad"]==8) & (df.Diresa=="LIMA DIRIS SUR")])
            grup_80mayora=len(df[(df["Grupo Edad"]==9) & (df.Diresa=="LIMA DIRIS SUR")])
            #grafica
            fig, ax = plt.subplots()
            grupos = ['6-11m', '01-04a', '05-11a','12-17a', '18-29a',
                     '30-39a', '40-49a', '50-59a', '60-69a', '70-79a', '80a>']
            valores = [grup_6_11m, grup_1_4a, grup_5_11a, grup_12_17a, grup_18_29a, grup_30_39a, 
                      grup_40_49a, grup_50_59a, grup_60_69a, grup_70_79a, grup_80mayora]
            azs=ax.bar(grupos, valores, color="Salmon")
            ax.bar_label(azs,padding=3)
            ax.set_ylabel('Cantidad de personas')
            ax.set_title('figura 2.1. Cantidad de personas por grupo de edad vacunados \n en la diresa Lima sur')
            ax.set_xlabel("Grupos de edad \n Fuente: https://www.minsa.gob.pe/reunis/data/vacunas-covid19.asp")
            plt.show()
        if escoge==2:
            grup_6_11m=len(df[(df["Grupo Edad"]==-1) & (df.Diresa=="LIMA DIRIS NORTE")])
            grup_1_4a=len(df[(df["Grupo Edad"]==0) & (df.Diresa=="LIMA DIRIS NORTE")])
            grup_5_11a=len(df[(df["Grupo Edad"]==1) & (df.Diresa=="LIMA DIRIS NORTE")])
            grup_12_17a=len(df[(df["Grupo Edad"]==2) & (df.Diresa=="LIMA DIRIS NORTE")])
            grup_18_29a=len(df[(df["Grupo Edad"]==3) & (df.Diresa=="LIMA DIRIS NORTE")])
            grup_30_39a=len(df[(df["Grupo Edad"]==4) & (df.Diresa=="LIMA DIRIS NORTE")])
            grup_40_49a=len(df[(df["Grupo Edad"]==5) & (df.Diresa=="LIMA DIRIS NORTE")])
            grup_50_59a=len(df[(df["Grupo Edad"]==6) & (df.Diresa=="LIMA DIRIS NORTE")])
            grup_60_69a=len(df[(df["Grupo Edad"]==7) & (df.Diresa=="LIMA DIRIS NORTE")])
            grup_70_79a=len(df[(df["Grupo Edad"]==8) & (df.Diresa=="LIMA DIRIS NORTE")])
            grup_80mayora=len(df[(df["Grupo Edad"]==9) & (df.Diresa=="LIMA DIRIS NORTE")])
            #grafica
            fig, ax = plt.subplots()
            grupos = ['6-11m', '01-04a', '05-11a','12-17a', '18-29a',
                     '30-39a', '40-49a', '50-59a', '60-69a', '70-79a', '80a>']
            valores = [grup_6_11m, grup_1_4a, grup_5_11a, grup_12_17a, grup_18_29a, grup_30_39a, 
                      grup_40_49a, grup_50_59a, grup_60_69a, grup_70_79a, grup_80mayora]
            azs=ax.bar(grupos, valores, color='violet')
            ax.bar_label(azs,padding=3)
            ax.set_ylabel('Cantidad de personas')
            ax.set_title('figura 2.2. Cantidad de personas por grupo de edad vacunados \n en la diresa Lima norte')
            ax.set_xlabel("Grupos de edad \n Fuente: https://www.minsa.gob.pe/reunis/data/vacunas-covid19.asp")
            plt.show()
        if escoge==3:
            grup_6_11m=len(df[(df["Grupo Edad"]==-1) & (df.Diresa=="LIMA DIRIS ESTE")])
            grup_1_4a=len(df[(df["Grupo Edad"]==0) & (df.Diresa=="LIMA DIRIS ESTE")])
            grup_5_11a=len(df[(df["Grupo Edad"]==1) & (df.Diresa=="LIMA DIRIS ESTE")])
            grup_12_17a=len(df[(df["Grupo Edad"]==2) & (df.Diresa=="LIMA DIRIS ESTE")])
            grup_18_29a=len(df[(df["Grupo Edad"]==3) & (df.Diresa=="LIMA DIRIS ESTE")])
            grup_30_39a=len(df[(df["Grupo Edad"]==4) & (df.Diresa=="LIMA DIRIS ESTE")])
            grup_40_49a=len(df[(df["Grupo Edad"]==5) & (df.Diresa=="LIMA DIRIS ESTE")])
            grup_50_59a=len(df[(df["Grupo Edad"]==6) & (df.Diresa=="LIMA DIRIS ESTE")])
            grup_60_69a=len(df[(df["Grupo Edad"]==7) & (df.Diresa=="LIMA DIRIS ESTE")])
            grup_70_79a=len(df[(df["Grupo Edad"]==8) & (df.Diresa=="LIMA DIRIS ESTE")])
            grup_80mayora=len(df[(df["Grupo Edad"]==9) & (df.Diresa=="LIMA DIRIS ESTE")])
            #grafica
            fig, ax = plt.subplots()
            grupos = ['6-11m', '01-04a', '05-11a','12-17a', '18-29a',
                     '30-39a', '40-49a', '50-59a', '60-69a', '70-79a', '80a>']
            valores = [grup_6_11m, grup_1_4a, grup_5_11a, grup_12_17a, grup_18_29a, grup_30_39a, 
                      grup_40_49a, grup_50_59a, grup_60_69a, grup_70_79a, grup_80mayora]
            azs=ax.bar(grupos, valores, color='lightgreen')
            ax.bar_label(azs,padding=3)
            ax.set_ylabel('Cantidad de personas')
            ax.set_title('figura 2.3. Cantidad de personas por grupo de edad vacunados \n en la diresa Lima este')
            ax.set_xlabel("Grupos de edad \n Fuente: https://www.minsa.gob.pe/reunis/data/vacunas-covid19.asp")
            plt.show()
        if escoge==4:
            grup_6_11m=len(df[(df["Grupo Edad"]==-1) & (df.Diresa=="LIMA DIRIS CENTRO")])
            grup_1_4a=len(df[(df["Grupo Edad"]==0) & (df.Diresa=="LIMA DIRIS CENTRO")])
            grup_5_11a=len(df[(df["Grupo Edad"]==1) & (df.Diresa=="LIMA DIRIS CENTRO")])
            grup_12_17a=len(df[(df["Grupo Edad"]==2) & (df.Diresa=="LIMA DIRIS CENTRO")])
            grup_18_29a=len(df[(df["Grupo Edad"]==3) & (df.Diresa=="LIMA DIRIS CENTRO")])
            grup_30_39a=len(df[(df["Grupo Edad"]==4) & (df.Diresa=="LIMA DIRIS CENTRO")])
            grup_40_49a=len(df[(df["Grupo Edad"]==5) & (df.Diresa=="LIMA DIRIS CENTRO")])
            grup_50_59a=len(df[(df["Grupo Edad"]==6) & (df.Diresa=="LIMA DIRIS CENTRO")])
            grup_60_69a=len(df[(df["Grupo Edad"]==7) & (df.Diresa=="LIMA DIRIS CENTRO")])
            grup_70_79a=len(df[(df["Grupo Edad"]==8) & (df.Diresa=="LIMA DIRIS CENTRO")])
            grup_80mayora=len(df[(df["Grupo Edad"]==9) & (df.Diresa=="LIMA DIRIS CENTRO")])
            #grafica
            fig, ax = plt.subplots()
            grupos = ['6-11m', '01-04a', '05-11a','12-17a', '18-29a',
                     '30-39a', '40-49a', '50-59a', '60-69a', '70-79a', '80a>']
            valores = [grup_6_11m, grup_1_4a, grup_5_11a, grup_12_17a, grup_18_29a, grup_30_39a, 
                      grup_40_49a, grup_50_59a, grup_60_69a, grup_70_79a, grup_80mayora]
            azs=ax.bar(grupos, valores, color='skyblue')
            ax.bar_label(azs,padding=3)
            ax.set_ylabel('Cantidad de personas')
            ax.set_title('figura 2.4. Cantidad de personas por grupo de edad vacunados \n en la diresa Lima centro')
            ax.set_xlabel("Grupos de edad \n Fuente: https://www.minsa.gob.pe/reunis/data/vacunas-covid19.asp")
            plt.show()
        if escoge==5:
            grup_6_11m=len(df[(df["Grupo Edad"]==-1) & (df.Diresa=="LIMA PROVINCIAS")])
            grup_1_4a=len(df[(df["Grupo Edad"]==0) & (df.Diresa=="LIMA PROVINCIAS")])
            grup_5_11a=len(df[(df["Grupo Edad"]==1) & (df.Diresa=="LIMA PROVINCIAS")])
            grup_12_17a=len(df[(df["Grupo Edad"]==2) & (df.Diresa=="LIMA PROVINCIAS")])
            grup_18_29a=len(df[(df["Grupo Edad"]==3) & (df.Diresa=="LIMA PROVINCIAS")])
            grup_30_39a=len(df[(df["Grupo Edad"]==4) & (df.Diresa=="LIMA PROVINCIAS")])
            grup_40_49a=len(df[(df["Grupo Edad"]==5) & (df.Diresa=="LIMA PROVINCIAS")])
            grup_50_59a=len(df[(df["Grupo Edad"]==6) & (df.Diresa=="LIMA PROVINCIAS")])
            grup_60_69a=len(df[(df["Grupo Edad"]==7) & (df.Diresa=="LIMA PROVINCIAS")])
            grup_70_79a=len(df[(df["Grupo Edad"]==8) & (df.Diresa=="LIMA PROVINCIAS")])
            grup_80mayora=len(df[(df["Grupo Edad"]==9) & (df.Diresa=="LIMA PROVINCIAS")])
            #grafica
            fig, ax = plt.subplots()
            grupos = ['6-11m', '01-04a', '05-11a','12-17a', '18-29a',
                     '30-39a', '40-49a', '50-59a', '60-69a', '70-79a', '80a>']
            valores = [grup_6_11m, grup_1_4a, grup_5_11a, grup_12_17a, grup_18_29a, grup_30_39a, 
                      grup_40_49a, grup_50_59a, grup_60_69a, grup_70_79a, grup_80mayora]
            azs=ax.bar(grupos, valores, color='orange')
            ax.bar_label(azs,padding=3)
            ax.set_ylabel('Cantidad de personas')
            ax.set_title('figura 2.5. Cantidad de personas por grupo de edad vacunados \n en la diresa Lima centro')
            ax.set_xlabel("Grupos de edad \n Fuente: https://www.minsa.gob.pe/reunis/data/vacunas-covid19.asp")
            plt.show()

def busqueda_ubigeo_reniec(df):
  n=0
  while n>999999 or n<100000:
    n=int(input("Ingrese el ubigeo segun RENIEC:> "))
  integrante=df[df['Ubigeo_Reniec']==n]
  if len(integrante)>0:
     print("Si hay registro del ubigeo ingresado")
     print(integrante)
  else:
     print("No hay registro del ubigeo ingresado")

def menu_de_la_funcion_trimestre():
  print("<---------TRIMESTRES--------->")
  print("1. I trimestre")
  print("2. II trimestre")
  print("3. III trimestre")
  print()

def divide_por_trimestre(df):
  menu_de_la_funcion_trimestre()
  n=-1
  while n<0 or n>3:
    n=int(input("Ingrese N:> "))
  print()
  trime1=df[(df.Fecha<="1/04/2022")]
  trime2=df[(df.Fecha>="1/04/2022") & (df.Fecha<="1/07/2022")]
  trime3=df[(df.Fecha>="1/07/2022") & (df.Fecha<="1/10/2022")]
  if n==1:
    print(trime1)
  elif n==2:
    print(trime2)
  elif n==3:
    print(trime3)
 
def diresas(df):
    print("<Cantidad de varones y mujeres vacunados por Diresa>")
   #valores hombres y mujeres en cada diresa
    di_sur_F=len(df[(df.Diresa=="LIMA DIRIS SUR") & (df.Sexo=="F")])
    di_sur_M=len(df[(df.Diresa=="LIMA DIRIS SUR") & (df.Sexo=="M")])
    di_cen_F=len(df[(df.Diresa=="LIMA DIRIS CENTRO") & (df.Sexo=="F")])
    di_cen_M=len(df[(df.Diresa=="LIMA DIRIS CENTRO") & (df.Sexo=="M")])
    di_nor_F=len(df[(df.Diresa=="LIMA DIRIS NORTE") & (df.Sexo=="F")])
    di_nor_M=len(df[(df.Diresa=="LIMA DIRIS NORTE") & (df.Sexo=="M")])
    di_es_F=len(df[(df.Diresa=="LIMA DIRIS ESTE") & (df.Sexo=="F")])
    di_es_M=len(df[(df.Diresa=="LIMA DIRIS ESTE") & (df.Sexo=="M")])
    di_prov_F=len(df[(df.Diresa=="LIMA PROVINCIAS") & (df.Sexo=="F")])
    di_prov_M=len(df[(df.Diresa=="LIMA PROVINCIAS") & (df.Sexo=="M")])
    #grafica
    diresas=['Lima sur','Lima centro', 'Lima norte', 'Lima este', 'Lima provincias']
    valores_hombres=[di_sur_M, di_cen_M, di_nor_M, di_es_M, di_prov_M]
    valores_mujeres=[di_sur_F, di_cen_F, di_nor_F, di_es_F, di_prov_F]
    x = np.arange(len(diresas))
    width=0.35
    fig,ax = plt.subplots()
    label_hombres= ax.bar(x-width/2,valores_hombres,width,label='Hombres', color="skyblue")
    label_mujeres= ax.bar(x+width/2,valores_mujeres,width,label='Mujeres',color="pink")
    ax.set_ylabel('Asistencia')
    ax.set_title('Figura 3. Cantidad de hombres y mujeres vacunados por Diresa')
    ax.set_xticks(x)
    ax.set_xticklabels(diresas)
    ax.legend()
    ax.bar_label(label_hombres,padding=3)
    ax.bar_label(label_mujeres,padding=3)
    ax.set_xlabel("Diresas \n Fuente: https://www.minsa.gob.pe/reunis/data/vacunas-covid19.asp")
    fig.tight_layout()
    plt.show()
menu()
df=pd.read_csv("Vacunas (1).csv",delimiter=';')
q=-1
while q<0:
    print()
    n=int(input("Ingrese accion:> "))
    print()
    if n==0:
       csv_report(df) 
    elif n==1:
       reporte_hombres_y_mujeres(df)
    elif n==2:
       reporte_grupo_edad(df)
    elif n==3:
        busqueda_ubigeo_reniec(df)
    elif n==4:
        divide_por_trimestre(df)
    elif n==5:
        diresas(df)
    elif n==6:
        print("Gracias por usar esta aplicacion!!!")
        break
