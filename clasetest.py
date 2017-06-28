


class Mascota(object):
	def __init__(self,color='red'):
		self.color = color

	def obtener_color(self):
		return self.color

		

class Gato(Mascota):
	def __init__(self,color,tamano):
		super(Gato,self).__init__(color)
		self.tamano=tamano

	def obtener_tamano(self):
		Mascota.__init__(self,color,tamano)
		return 'El tamano del gato es {tamano}'.format(tamano=self.tamano)

	def obtener_color(self):
		color = super(Gato,self).obtener_color()
		return 'El color del Gato es {color}'.format(color=color)


class Perro(Mascota):
	def __init__(self,color,edad):
		super(Perro,self).__init__(color)
		self.edad = edad

	def Obtener_Edad(self):
		return 'La edad del perro es {edad}'.format(edad=self.edad)

	def obetener_color (self):
		color = super(Perro,self).obtener_color()
		return 'El color del perro es {color}'.format(color=color)

if __name__ == '__main__':

	perro = Perro('blue','7')
	print perro.obetener_color()
	print perro.Obtener_Edad()


