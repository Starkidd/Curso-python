import gi

gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):

	def __init__(self,*args,**kwargs):
		super(MiVentana,self).__init__(*args,**kwargs)
		self.set_default_size(500,500)
		self.connect('delete-event',Gtk.main_quit)
		self.contenedor()
		self.agregar_wigets()



	def contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)


	def agregar_wigets(self):
		self.label_user = Gtk.Label('Victoria Usuario ')
		self.contenedor.attach(self.label_user,0,0,1,1)
		self.label_maquina = Gtk.Label('Victoria Maquina')
		self.contenedor.attach(self.label_maquina,0,0,3,1)


if __name__ == '__main__':

	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()