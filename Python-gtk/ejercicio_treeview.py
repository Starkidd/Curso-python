import gi

gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class MiVentana(Gtk.Window):
	def __init__(self,*args,**kwargs):
		super(MiVentana,self).__init__(*args,**kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event',Gtk.main_quit)
		self.agregar_contenedor()
		self.agregar_entrada()
		self.agregar_boton()
		self.agregar_lista()
		


	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)



	def agregar_entrada (self):
		self.entrada = Gtk.Entry()
		self.contenedor.attach(self.entrada,0,0,2,1)
		self.entradaMonto = Gtk.Entry()
		self.contenedor.attach(self.entradaMonto,2,0,1,1)




	def agregar_boton(self):
		self.boton = Gtk.Button('Agregar')
		self.label = Gtk.Label()
		self.contenedor.attach_next_to(self.label, self.entrada, Gtk.PositionType.BOTTOM, 1,1)

		self.contenedor.attach_next_to(
			self.boton,
			self.label,
			Gtk.PositionType.BOTTOM,
			3,
			1
			)

		


	def agregar_lista(self):
		""" ----CREA UN TREE VIEW----
		1. Crear el model de datos Gtk.ListStore(type,type,....type)
		2. Crear el widget que contiene o muestra los datos de modelo. TreeVieqw(<models>)
		3. Definir las colmnas y su contenido.

		3.1 crear celda para cada columna de la fila
		# Los CellRenderer son widget que sirven para mostrar contenido 
		# dentro de otros widgets dependiendo de su tipo
		3.2 Crear columans (TreeVIew) del TreeView que mostraran los datos usando CellRenderer widgets como elementos hijos
		3.3 agregar cada treeViewColumn al Treeview widget"""

		self.modelo = Gtk.ListStore(str,float)
		self.lista_activos = Gtk.TreeView(self.modelo)

		descripcion = Gtk.CellRendererText()
		columna_descripcion = Gtk.TreeViewColumn('Descripcion',descripcion,text=0)

		monto = Gtk.CellRendererText()
		columna_monto = Gtk.TreeViewColumn('Monto',monto,text=1)

		self.lista_activos.append_column(columna_descripcion)
		self.lista_activos.append_column(columna_monto)

		self.contenedor.attach_next_to(
			self.lista_activos,
			self.boton,
			Gtk.PositionType.BOTTOM,
			3, 
			1)

		self.boton.connect('clicked',self.agregar_fila)
		
	def agregar_fila(self,btn):



		if self.entrada.get_text() and self.entradaMonto.get_text():
			textoDescrip = self.entrada.get_text()
			textoMonto = self.entradaMonto.get_text()
			self.modelo.append([textoDescrip,float(textoMonto)])
			self.entrada.set_text('')
			self.entradaMonto.set_text('')
			self.label.set_text("")
		else:
			self.label.set_markup('<b>Inserte los valores correctamente</b>')


		


		






if __name__ == '__main__':

	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()