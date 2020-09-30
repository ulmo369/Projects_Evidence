import pandas as pd # importa la librería pandas y la asigna a la variable pd

datos_consumo = pd.read_excel('datos.xlsx') # indicamos el nombre de nuestro archivo a ser leído

print("--PRIMEROS 5 DATOS--")
print(datos_consumo.head())

datos = datos_consumo[["Fecha (dd/mm/aa)","Calorías (kcal)"]] # seleccionamos las dos columnas que necesitaremos
print("\n\n--5 DATOS DE LOS DATOS QUE NECESITAMOS--")
print(datos.head()) # imprimiendo los datos selecccionados

print("\n\n--TOTAL DE CALORIAS--")
suma_calorías = datos["Calorías (kcal)"].sum()
print(suma_calorías) # despliega el total de calorias

print("\n\n--TOTAL DE DIAS UNICOS--")
días = datos["Fecha (dd/mm/aa)"].nunique()
print(días) # despliega el total de días unicos

print("\n\n--PROMEDIO DE CALORIAS--")
calorías_promedio = suma_calorías/días # total de calorías consumidas entre el número de días que tomó consumirlas
print("Tu promedio de calorías consumidas en", días,"días es:", calorías_promedio)

print("\n\n--CAPTURA DE DATOS--")
peso = int(input("Ingresa tu peso en kilogramos: "))
altura = int(input("Ingresa tu altura en centimetros: "))
edad = int(input("Ingresa tu edad en años: "))
genero = input("Ingresa tu género, Mujer/Hombre: ")

if(genero == "Mujer"):
   calorías_requeridas = 655+(9.56*peso)+(1.85*altura)-(4.68*edad) # fórmula para estimar calorías requeridas en mujer
elif(genero == "Hombre"):
  calorías_requeridas = 66.5+(13.75*peso)+(5*altura)-(6.8*edad) # fórmula para estimar calorías requeridas en hombre
print("Con base en tus datos, tu consumo de calorías al día debe ser de:", calorías_requeridas)

print("\n\n--DIFERENCIA ENTRE CALORIAS CONSUMIDAS Y REQUERIDAS--")
diferencia = calorías_promedio - calorías_requeridas
print(diferencia)

print("\n\n--RESULTADO DE LA APROXIMACION--")
efecto_anual = diferencia * 450/3500 * 365 /1000 # realiza la proporción, se multiplica por 365 (días) y se divide entre 1000 (gramos) para obtener kilogramos
print("Si continuas con el consumo calórico actual, en un año tu cambio de masa corporal sería aproximadamente de:",efecto_anual,"kg")

