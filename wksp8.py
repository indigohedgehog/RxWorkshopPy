"""Rx Workshop: Unified Programing Model.
Part 4 - Bridge event stream to a string observable.
Usage:
    python wksp8.py
"""
from __future__ import print_function
import gi.repository.Gtk
import rx


class Form(gi.repository.Gtk.Window):

    def __init__(self):
        gi.repository.Gtk.Window.__init__(self, title="Form")
        self.subject = rx.subjects.Subject()
        self.subject.subscribe(lambda x: print(x) or self.set_title(x))
        vbox = gi.repository.Gtk.Box(
            orientation=gi.repository.Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = gi.repository.Gtk.Entry()
        self.entry.connect("changed", lambda x:
                           self.subject.on_next(x.get_text()))
        vbox.pack_start(self.entry, True, True, 0)

        hbox = gi.repository.Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)


win = Form()
win.connect("delete-event",  gi.repository.Gtk.main_quit)
win.show_all()
gi.repository.Gtk.main()
