import gi

gi.require_version('Gtk','3.0')
from gi.repository import Gtk


def imprimir_algo(btn):
	print btn
	print 'HOLA MUNDO.COM'

if __name__ == '__main__':




	ventana = Gtk.Window(title='Ejemplo 1')
	ventana.connect('delete-event',Gtk.main_quit)
	button = Gtk.Button('BTN 1')
	button2 = Gtk.Button('BTN 2')
	button3 = Gtk.Button('BTN 3')
	button4 = Gtk.Button('BTN 4')

	#button.connect('clicked',imprimir_algo)
	
	contenedor = Gtk.Grid()
	contenedor.set_column_homogeneous(True)
	contenedor.set_row_homogeneous(False)
	contenedor.attach(
		button,#elemento
		0,#columna
		0,#fila
		3,#Nro Columnas a usar
		1,#Nro filas a usar

		)

	contenedor.attach(button2,1,1,1,1)
	contenedor.attach(button3,2,1,1,1)
	contenedor.attach(button4,0,3,1,1)


	ventana.add(contenedor)

	ventana.show_all()
	Gtk.main()