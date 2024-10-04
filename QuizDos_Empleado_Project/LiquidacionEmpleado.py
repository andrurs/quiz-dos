#Datos de entrada

nombre = "Andres Rodriguez"
salario = int (input("Ingrese su salario: "))
diasTrabajados =int (input("Ingrese los días trabajados: "))
#operaciones
prima = salario*diasTrabajados/360
cesantias =(salario*diasTrabajados)/360
interesCesantias=(cesantias*0.12)/diasTrabajados
vacaciones = (salario*diasTrabajados)/720
liquidacion=prima+cesantias+interesCesantias+vacaciones

#salida
print(f"Señor {nombre} para los {diasTrabajados} días laborados y salario ${salario} su liquidacion se compone así:"
      f"\nPrima:\t\t\t\t ${prima:.2f}\nCesantía:\t\t\t ${cesantias:.2f}\nIntereses cesantías: ${interesCesantias:.2f}"
      f"\nVacaciones:\t\t\t ${vacaciones:.2f} \nLiquidacion:\t\t ${liquidacion:.2f}")