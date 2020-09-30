def calculadora(nombre, apellido, edad, estatura, peso): #Funcion que contendrá los calculos, reciviendo los datos
    
    print("\n¡Hola",nombre, apellido,"!") # Saludo con nombre
    print("Tu peso registrado es de",peso,"kg") # se muestra el peso registrado 
    print("Tu estatura es de",estatura,"mts") # se muestra la estatura registrada
    imc =  peso / estatura ** 2 # se calcula el imc
    
    if imc <= 18.4: # si el IMC es menor a 18.4
        print("De acuerdo con estos datos tú IMC es","{0:.1f}".format(imc),"lo que indica: Peso bajo") # se imprime el resultado con 1 decimal

    elif imc >= 18.5 and imc <= 24.9: # sino, si el IMC es mayor a 18.5 y menor 24.9 
        print("De acuerdo con estos datos tú IMC es","{0:.1f}".format(imc),"lo que indica: Peso normal")# se imprime el resultado con 1 decimal

    elif imc >= 25 and imc <= 29.9: # sino, si el IMC es mayor a 25 y menor a 29.9
        print("De acuerdo con estos datos tú IMC es","{0:.1f}".format(imc),"lo que indica: sobre peso")# se imprime el resultado con 1 decimal

    else: # sino cae en ninguno de los rangos anteriores entonces es mayor
        print("De acuerdo con estos datos tú IMC es","{0:.1f}".format(imc),"lo que indica: Obesidad")# se imprime el resultado con 1 decimal
    
    
if __name__=="__main__":#main del código
    
    nombre = str(input("Ingresa tu nombre: ")) #variable del NOMBRE

    apellido = str(input("Ingresa tu apellido: ")) #variable del APELLIDO

    edad = int(input("Ingresa tu edad: ")) #varible de la EDAD

    estatura = float(input("Ingresa tu estatura en metros (Ej:1.78): ")) #variable de la ESTATURA
    
    peso = float(input("Ingresa tu peso en Kg: ")) #variable del PESO
    
    persona = [nombre, apellido, edad, estatura, peso] #Lista con los datos
    print("Datos:",persona)#se imprimen los datos
    
    calculadora(persona[0], persona[1], persona[2], persona[3], persona[4]) #llamada de la función para recivir los datos pedidos para la lista
    
    guia = """

    Cómo leer resultados

    Nivéles de Peso de acuerdo al IMC:

    IMC por debajo de 18.5: Peso bajo

    IMC entre 18.5 – 24.9: Peso normal

    IMC entre 25.0 – 29.9: Sobrepeso

    IMC de más de 30.0: Obesidad"""

    print(guia)
    
    from datetime import datetime # importamos la librería de fechas y horas

    from pytz import timezone # importamos la librería de zonas horarias 

    zona_horaria = timezone('America/Mexico_City') # definimos el uso horario de Monterrey

    fecha_hora = datetime.now(zona_horaria) # definimos la variable fecha_hora usando la función now() para saber fecha y hora actual, y le indicamos la zona horaria

    fecha_hora_formato = fecha_hora.strftime("%B %d, %Y %H:%M:%S") # le damos formato a la fecha y hora

    print("\nCreated on", fecha_hora_formato) # imprimimos la fecha y hora

    autor = "Diego Emilio Barrera Hernández" # definimos la variable autor con nuestro nombre

    print("Author:",autor) # imprimimos nombre del autor
