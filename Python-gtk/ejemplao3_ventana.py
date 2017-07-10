import gi

gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class MiVentana(Gtk.Window):
	def __init__(self,*args,**kwargs):
		super(MiVentana,self).__init__(*args,**kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event',Gtk.main_quit)
		self.agregar_contenedor()
		self.agregar_boton()
		self.agregar_text()
		self.agregar_label()

	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.contenedor.set_row_homogeneous(False)



	def agregar_text(self):
		self.text = Gtk.Entry("TEXT 1")
		text.get_text()
		#agregar_contenedor(contenedor.attach(self.text,0,0,1,1))


	def agregar_boton(self):
		self.boton = Gtk.Button('BOTON 1')
		
		

	def agregar_label(self):
		self.label = Gtk.Label('LABEL 1')
		label.set_markup('texto')
		

if __name__ == '__main__':

	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()


