#!/usr/bin/env python
# coding: utf-8

import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
import tnefmgr

class TnefReader:
	def __init__(self,file):
		#self.glade=gtk.glade.XML(os.path.join(os.path.dirname(os.path.abspath(__file__)),'ui/main.glade'),None,None)
		#self.ventana=self.glade.get_widget('main')
		#self.lista=self.glade.get_widget('lista')
		
		self.tnef=tnefmgr.TnefMgr(file)

		builder = gtk.Builder()
		builder.add_from_file(os.path.join(os.path.dirname(os.path.abspath(__file__)),'ui/main.glade'))
		builder.connect_signals(self)
		self.ventana=builder.get_object('main')
		self.ventana.set_title("TNEF Reader - "+os.path.basename(file))
		self.lista=builder.get_object('lista')
		

	def rellenaFicheros(self):
		store=self.lista.get_model()		

		c1=gtk.TreeViewColumn("Fichero",gtk.CellRendererText(),text=0)		
		c2=gtk.TreeViewColumn("Tamaño",gtk.CellRendererText(),text=1)
		
		self.lista.append_column(c1)
		self.lista.append_column(c2)

		self.tnef.open()
		self.ficheros=self.tnef.list()
		for f in self.ficheros:
			store.append([f,str(self.tnef.getSize(f))])


	def on_lista_row_activated(self,sender,numero,noUsado):
		self.tnef.preview(self.ficheros[numero[0]])

	def on_btnSave_clicked(self,sender):
		try:			
			tree_sel = self.lista.get_selection()
			(tm, ti) = tree_sel.get_selected()
			if ti == None:
				self.alert("Please, pick a file")
				return

			selected = tm.get_value(ti, 0)
			
			dialog = gtk.FileChooserDialog("Please choose a folder", self.ventana, gtk.FileChooserAction.SAVE,	
				(gtk.STOCK_CANCEL, gtk.ResponseType.CANCEL, "Select", gtk.ResponseType.OK))
			dialog.set_current_name(selected)
			dialog.set_default_size(800, 400)
			response = dialog.run()

			if response == gtk.ResponseType.OK:
				self.tnef.extract(selected,dialog.get_filename())
				dialog.destroy()
				self.alert(selected+" saved.")
			else:
				dialog.destroy()
		
		except Exception as ex:
			self.alert(str(ex))

	def on_close(self,sender):
		self.tnef.close()
		self.ventana.destroy()
		gtk.main_quit()

	def alert(self,text,title="TNEF Reade",mode=gtk.MessageType.INFO):
		dlg = gtk.MessageDialog(self.ventana, 0, mode,
            gtk.ButtonsType.OK, text)
		dlg.set_title(title)
		dlg.run()
		dlg.destroy()



	def run(self):
		self.rellenaFicheros()
		self.ventana.show_all()

if __name__ == '__main__':
	def printHelp():
		print("USE:")
		print("%s <file>" % sys.argv[0])
		
	if len(sys.argv) == 1:
		printHelp()
		sys.exit(1)

	if not os.path.exists(sys.argv[1]):
		print("%s not exists" % sys.argv[1])
		sys.exit(1)

	d = TnefReader(sys.argv[1])
	d.run()
	gtk.main()
