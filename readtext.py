


if __name__ == '__main__':


	f = open('ESTUDIANTE_DE_MANAGUA.txt','a')
	informacion = raw_input('ingrese informacion al fichero-->')
	linea = '{contenido} \n'
	info  = linea.format(contenido=informacion)
	f.write(info)
	f.close()

	f = open('ESTUDIANTE_DE_MANAGUA.txt','r')
	for line in f :
		print (line)
	#print (f.readline())
	f.close()
