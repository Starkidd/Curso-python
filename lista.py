#crear 20 num aleatorios entre 0 y el 100
#imprimir una lista de los numeros generados
#ordenados ascendentemente, primero los pares y luego los impares

#ejemplo: si los num generados so [4,3,5,6,2]
#el resultado sera [2,4,6,3,5]

import random



mi_list=[]
for x in range(0,20):
	num=random.randrange(0,100)
	mi_list.insert(0,num)

print('numeros generado:')

for index in range(len(mi_list)):
	print(mi_list[index])
	mi_list.sort()
	
	

print('numeros ordenados de forma ascendentes')

mi_list.sort()
for index in range(len(mi_list)):
	if (mi_list[index])%2==0:
	
		print(mi_list[index])

for index in range(len(mi_list)):
	if(mi_list[index])%2!=0:
		print(mi_list[index])








  


