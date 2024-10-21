# Paso 1: Definir el valor actual del Euro y Dolar con respecto al peso mexicano

tipo_cambio_eur_a_mxn = 23.70
tipo_cambio_usd_a_mxn = 20.75

# Paso 2: Solicitar al usuario el tipo de conversion (Euro a Mex o Dolar a Mex)

tipo_de_conversion= input("Ingrese la moneda origen para la conversión (EUR/USD): ")
print(tipo_de_conversion)

#Paso 3: Solicitar al usuario el monto a convertir

monto_a_convertir= float(input("Ingrese el monto a convertir: ")) 
print(monto_a_convertir)

#Paso 4: Realizar la conversion utilizando el tipo de cambio correspondiente



#Paso 5; Mostrar el resultado de la conversion al usuario 

if tipo_de_conversion.upper() == "EUR":  
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn 
    print ("El resultado de la conversion de EUR a MXN es: ", resultado)  
elif tipo_de_conversion.upper() == "USD": 
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print(" El resulrado de la conversion de USD a MXN e: ", resultado) 
else:
    print( "No esta disponible este tipo de conversion actualmente")   