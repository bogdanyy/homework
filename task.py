import gi
gi.require_version ( 'Gtk' , '3.0' )
from gi.repository import Gtk

class MyWindow(Gtk . Window):

    def __init__ (self):
        Gtk.Window.__init__(self, title="Диспетчер задач")
        self.set_border_width(3)
        self.set_resizable(True)

        self.notebook = Gtk.Notebook()
        self.add (self.notebook)

        self.page1 = Gtk.Box()
        self.page1.set_border_width ( 10 )
        self.page1.add(Gtk.Label('Process'))
        self.notebook.append_page(self.page1, Gtk.Label('Процессы'))

        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add ( Gtk.Label('Resourcess'))
        self.notebook.append_page(self.page2, Gtk.Label('Ресурсы'))

        self.page3 = Gtk.Box()
        self.page3.set_border_width(10)
        self.page3.add ( Gtk.Label('File system'))
        self.notebook.append_page(self.page3, Gtk.Label('Файловая система'))

        
       