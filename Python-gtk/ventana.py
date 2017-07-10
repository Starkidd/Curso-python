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
	button.connect('clicked',imprimir_algo)
	
	contenedor = Gtk.VBox()
	contenedor.pack_start(button,False,False,0)
	contenedor.pack_end(button2,False,False,0)
	ventana.add(contenedor)

	ventana.show_all()
	Gtk.main()