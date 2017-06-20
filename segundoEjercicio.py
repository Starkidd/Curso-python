import argparse

estudiante ={'nombre': 'kid'}
mensajeExiste = "La llave {0} existe en el diccionarios"
mensajeNoExiste = "La llave {0} no existe en el diccionario"


if __name__ == '__main__':

	parser = argparse.ArgumentParser()

	parser.add_argument('Nombre')
	args = parser.parse_args()
	nombre = args.Nombre

	
	
	for llave, datos in estudiante.iteritems():
		print (llave, datos)

		if nombre in estudiante:
			print(mensajeExiste.format(nombre))
			
		else:
			print(mensajeNoExiste.format(nombre))
			
			

		