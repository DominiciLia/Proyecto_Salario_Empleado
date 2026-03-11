
seguridadSocial = 5.91
isr= 15 #15%
bono =  0
dobleSueldo = 0
impuestoISR = 15
sumaGananciasEmpleado = 0

#Recolecta de datos del usuario
nombre = input("——¿Cómo te llamas?—— ")
print()
salario = float(input("——¿Cuanto ganas al mes ——? "))
print()
fechaEntrada = int(input("——¿Cuantos años llevas en la empresa (si lleva menos de un año ponga un 0 )——?"))
print()
print("-------------------------------")

#Funcion para sacar sueldo bruto

def calcularSueldoBruto(sueldo) :

 sueldodescuentado = sueldo * seguridadSocial /100

 print (f"La seguridad social toma de su sueldo: {sueldodescuentado}")

 sueldoMenosIsr = sueldo * isr /100

 print (f"--- El Isr al 15% toma de su sueldo: {sueldoMenosIsr}--- ")

 ##Condicional para saber si aplica o no al bono y doble sueldo

 if fechaEntrada == 0:
    print("--- No aplica al bono ---")

 elif 0 < fechaEntrada <= 5:
    bono = sueldo * (25/100)
    dobleSueldo = sueldo *2
    print(f"--- Su bono es de: {bono}---")
    print(f"--- Su doble sueldo es de: {dobleSueldo}---")
      
    sumaGananciasEmpleado = sueldo + bono + dobleSueldo
     
    if sumaGananciasEmpleado >= 416220 :
       SueldoBruto = sueldo -sueldodescuentado - sueldoMenosIsr - (impuestoISR/100)

 else:
    bono = sueldo * (60/100)
    dobleSueldo = sueldo *2
    print(f"--- Su bono es de: {bono}---")
    print(f"--- Su doble sueldo es de: {dobleSueldo}---")

    sumaGananciasEmpleado = sueldo + bono + dobleSueldo

    if sumaGananciasEmpleado >= 416220 :
       SueldoBruto = sueldo -sueldodescuentado - sueldoMenosIsr - (impuestoISR/100)

 print()
 
 SueldoBruto = sueldo -sueldodescuentado - sueldoMenosIsr
 print(f"--- {nombre},tu salario bruto tiene un valor de: {SueldoBruto} ---")


##Llamada a la función
calcularSueldoBruto(salario)
print()
print("-------------------------------")

