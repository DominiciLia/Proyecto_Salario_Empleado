
seguridadSocial = 5.91
isr= 15 #15%


def calcularSueldoBruto(sueldo) :

 sueldodescuentado = sueldo * seguridadSocial /100

 print (f" La seguridad social toma de su sueldo:{sueldodescuentado}")

 sueldoMenosIsr = sueldo * isr /100

 print (f"El Isr al 15% toma de su sueldo :{sueldoMenosIsr}")

 SueldoBruto = sueldo -sueldodescuentado - sueldoMenosIsr

 print()
 print(f"---{nombre},tu salario bruto tiene un valor de:{SueldoBruto}---")


nombre = input("——¿Cómo te llamas?—— ")
print()
salario = float(input("——¿Cuanto ganas——? "))

calcularSueldoBruto(salario)

