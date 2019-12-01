from UI import task
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


if __name__ == "__main__":
    win = task.MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()