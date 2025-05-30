SubProceso areat(a,b)
	Definir resultado Como Real
	resultado= (a*b)/2
	Escribir "La area es: ", resultado
FinSubProceso

SubProceso suma(num1,num2)
	Definir resultado Como Entero
	resultado= num1+num2
	Escribir "La suma es: ", resultado
FinSubProceso

Algoritmo sin_titulo
	Definir n1, n2 Como Entero
	Escribir "Ingrese la base"
	Leer n1
	Escribir "Ingrese la altura"
	Leer n2
	areat(n1 ,n2)
	Escribir "Ingrese el numero 1"
	Leer num1
	Escribir "Ingrese el numero 2"
	Leer num2
	suma(num1 ,num2)
FinAlgoritmo



