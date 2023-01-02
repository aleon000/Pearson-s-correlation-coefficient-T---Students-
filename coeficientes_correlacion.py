import csv
import pandas as pd
import os


#Definicion de directorios
cdir = os.getcwd()
path_datos = cdir + '\datos.csv'
path_tstud = cdir + '\\t-students.csv'


#Extraccion datos .csv y tabla t-students
mydata = pd.read_csv(path_datos, delimiter=('\\n'))
t_stud_table = pd.read_csv(path_tstud, delimiter=(';'))

values = mydata['column'].tolist()


#Cantidad de items en values dividido entre dos debido que hay dos columnas
#Calculo de grados de libertad
n_values = int(len(values)/2)
free_deg = n_values - 2


#Creacion de columnas x,y
x = []
y = []

for n in values[:n_values]:
    x.append(n)

for i in values[n_values:]:
    y.append(i)
    

#Creacion de medias aritmeticas
x_media = (sum(x)/n_values)
y_media = (sum(y)/n_values)


#Calculo desviacion (x - x_media)
x_desv = []
y_desv = []

for n in x:
    x_desv.append(n-x_media)
    
for n in y:
    y_desv.append(n-y_media)
    
#Calculo (x - x_meia) * (y - y_media)
desv_multi = []

for n in range(n_values):
    desv_multi.append(x_desv[n] * y_desv[n])

desv_total = sum(desv_multi)
    

#calculo covarianza
covar = (desv_total / (n_values - 1)) 


#Calculo desviacion estandar
#x_ds = ((sum(x_desv)**2) / (n_values -1))**0.5
x_desv_sq = []
for n in x_desv:
    x_desv_sq.append(n ** 2)
x_desv_sq = sum(x_desv_sq)
y_desv_sq = []
for n in y_desv:
    y_desv_sq.append(n ** 2)
y_desv_sq = sum(y_desv_sq)

x_s = ((x_desv_sq / (n_values - 1)) ** 0.5)
y_s = ((y_desv_sq / (n_values - 1)) ** 0.5)


#Calculamos el coeficiente de correlacion de Pearsonr (r)
r = (covar / (x_s * y_s))


#Calculo error estandar
err_std = (((1 - r ** 2) / (n_values - 2)) ** 0.5)


#Comparacion t-students
#Revisa si el free_deg o (grado de libertad) es mayo a 1000, si lo es,
#datacolumn (fila con los valores de t-students para ese grado de libertad), es
#directamente la columna de infinito
if free_deg > 1000:
    table_fd = 'inf'
    datacolumn = t_stud_table.iloc[55].tolist()
#Si el grado de libertad es diferente al anterior, busca el grado de libertad
#entre los grados disponibles y elije el mas proximo dentro de la tabla de 
#t-students. Datacolumn guarda la fila de esta grado de libertad.
else:
    table_fd = min(t_stud_table['df'], key=lambda x:abs(x-free_deg))
    datacolumn = t_stud_table.loc[t_stud_table['df'] == table_fd]
    datacolumn = datacolumn.iloc[0].tolist()
    

#Se atribuye el coeficiente de correlacion
if r > (err_std*datacolumn[8]):
    correl_val = 0.001
    print("El coeficiente de correlacion es significativo al p < 0.001")
elif r > (err_std*datacolumn[7]):
    correl_val = 0.002
    print("El coeficiente de correlacion es significativo al p < 0.002")
elif r > (err_std*datacolumn[6]):
    correl_val = 0.005
    print("El coeficiente de correlacion es significativo al p < 0.005")
elif r > (err_std*datacolumn[5]):
    correl_val = 0.01
    print("El coeficiente de correlacion es significativo al p < 0.01")
elif r > (err_std*datacolumn[4]):
    correl_val = 0.02
    print("El coeficiente de correlacion es significativo al p < 0.02")
elif r > (err_std*datacolumn[3]):
    correl_val = 0.05
    print("El coeficiente de correlacion es significativo al p < 0.05")
elif r > (err_std*datacolumn[2]):
    correl_val = 0.1
    print("El coeficiente de correlacion es significativo al p < 0.1")
elif r > (err_std*datacolumn[1]):
    correl_val = 0.2
    print("El coeficiente de correlacion es significativo al p < 0.2")
else:
    correl_val = '< 0.2'
    print('El coeficiente de correlacion p > 0.2')

#Se imprimen los resultados de los estadisticos
print('X media: ' + str(x_media))
print('Y media: ' + str(y_media))
print('Covarianza: ' + str(covar))
print("r: " + str(r))
print('Desviacion estandar X: ' + str(x_desv))
print('Desviacion estandar Y: ' + str(y_desv))
print('Error estandar: ' + str(err_std))
print('Coeficiente de correlacion: ' + str(correl_val))


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

