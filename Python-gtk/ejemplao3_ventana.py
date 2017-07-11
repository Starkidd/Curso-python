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
		self.add(self.contenedor)


	def agregar_text(self):
		self.text = Gtk.Entry()
		self.contenedor.attach(self.text,0,0,1,1)
		
		

	def agregar_boton(self):
		self.boton = Gtk.Button('BOTON 1')
		self.boton.connect('clicked',self.pasar_valor)
		self.contenedor.attach(self.boton,0,1,1,1)
		
		

	def agregar_label(self):
		self.label = Gtk.Label('Texto Definido')
		self.contenedor.attach(self.label,0,2,1,1)


	def pasar_valor(self,temporal):
		inp = self.text.get_text()
		self.label.set_markup(inp)




		

if __name__ == '__main__':

	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()


