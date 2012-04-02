#!/usr/bin/env python27
#coding=utf8
'''
Cipherka (main program)
Author: Martin Mirbauer, David Roesel
Web: --
Version: --
Description: --
'''
import os, sys, gtk
# Load list of 
import modules.__init__

class Main: 
    def __init__(self):
        # Create of widgets and linking event handlers according to Glade
        self.builder = gtk.Builder()
        self.builder.add_from_file(sys.path[0] + '/' + 'gui.xml') 
        self.builder.connect_signals(self) 
              
        # Closing the window should be handled as terminating the program
        self.w('main_window').connect('configure_event', self.on_main_window_configure_event)
        self.w('main_window').connect('destroy', lambda w: gtk.main_quit())
        self.all_modules = modules.__init__.__all__
        # print(self.all_modules)
        
        muj_liststore = gtk.ListStore(gtk.gdk.Pixbuf, str)
        #for name,icon in [['Plain Text', getattr(gtk, "STOCK_COLOR_PICKER")],
        #                ['PDF', getattr(gtk, "STOCK_COLOR_PICKER")],
        #                ['Postscript', getattr(gtk, "STOCK_COLOR_PICKER")],
        #                ['Web Page (HTML)', getattr(gtk, "STOCK_COLOR_PICKER")],
        #                ['JPEG', getattr(gtk, "STOCK_COLOR_PICKER")]]:
        for name in self.all_modules:
            icon = getattr(gtk, "STOCK_COLOR_PICKER")
            image = gtk.icon_theme_get_default().load_icon(icon,24,gtk.ICON_LOOKUP_USE_BUILTIN)
            muj_liststore.append([image,name])
        
        # Set up a liststore for combobox1
        self.w("modules_selector").set_model(muj_liststore)
        
        # Add renderers for pictures and text
        renderer = gtk.CellRendererPixbuf()
        self.w("modules_selector").pack_start(renderer, expand=False)
        self.w("modules_selector").add_attribute(renderer, 'pixbuf', 0)
        
        renderer = gtk.CellRendererText()
        self.w("modules_selector").pack_start(renderer, expand=True)
        self.w("modules_selector").add_attribute(renderer, 'text', 1)        
        
        # Pre-select of the first item and loading module accordingly
        self.w("modules_selector").set_active(0) 
        self.changed_cb(self.w("modules_selector"))
        
        # Add event handlers
        self.w('modules_selector').connect('changed', self.changed_cb)
        
        # Get and give the versions of GTK and pyGTK
        versions="gtk: "+str(gtk.gtk_version)+" pygtk: "+str(gtk.pygtk_version)+" cipherka: "+str(self.ciph_version())
        self.w('versions_label').set_text(versions)
        
        # Show the main window
        self.w('main_window').set_gravity(gtk.gdk.GRAVITY_STATIC)
        self.w('main_window').show_all()
    
    def ciph_version(self):
        return "alpha"    
    
    def show_settings_window(self):
        '''Showing/hiding the settings window.'''
        # If the toggle button is active, show the settings window
        if self.w("settings_toggle").get_active():
            # Get current position of main and setting windows
            x_sett, y_sett = self.w('settings_window').get_position()
            x_main, y_main = self.w('main_window').get_position()
            # If the setting window is in the right position...
            if (x_sett-x_main==(180+490)) and (y_sett-y_main==(25-30)):
                # ...show it.
                self.w('settings_window').show()
            else: 
                # ...reset its position and move it accordingly
                self.w('settings_window').set_position(gtk.WIN_POS_CENTER_ON_PARENT)
                self.w('settings_window').show()
                self.w('settings_window').move(x_main+675,y_main)
                # Wait for the moving to finish
                while gtk.events_pending():
                    gtk.main_iteration()
        else:
            self.w('settings_window').hide()
        #print(gtk.gdk.GdkEventType(gtk.gdk.DELETE))
        
    
    def w(self, widgetname):
        '''Pomůcka pro stručný přístup k widgetům'''
        return self.builder.get_object(widgetname)
    
    def process(self, input, method, parameters=None):
        '''This function initiates encryption/decryption by calling the selected module and returning the result.'''
        #sys.path.append('modules')    # Allow importing from folder
        #self.method = 'modules.' + method
        sys.path.append(os.path.join(sys.path[0], 'modules'))   # Allow importing from folder
        self.method = method
        # Import module by name and return it (not __init__.py)
        self.module = __import__(self.method, globals(), locals(), [self.method], -1)    
        # Call the function inside the module
        return self.module.run(input, parameters)    
    
    ## Event handlers from hereon
    def on_settings_toggle_toggled(self, widget):
        self.show_settings_window()
            
    def on_main_window_configure_event(self, *args):
        x, y   = self.w('main_window').get_position()
        sx, sy = self.w('main_window').get_size()
        tx = self.w('settings_window').get_style().xthickness
        self.w('settings_window').move(x+sx+20,y)
    
    def on_start_clicked(self, widget):
        '''Calls the 'process' function and supplies it with necessary parameters.'''
        
        # Get selected module
        model = self.w('modules_selector').get_model()
        index = self.w('modules_selector').get_active()
        
        selected_module = model[index][1]
        print "Selected module:", selected_module
        
        input = self.w('inputText').get_text(self.w('inputText').get_start_iter(), self.w('inputText').get_end_iter())
        print('Input: ' + input)
       
        # Call the selected module
        output = self.process(input, selected_module, None) 
        print('Output: ' + output)
        self.w('outputText').set_text(output)
    
    def on_settings_window_delete_event(self, widget = None, event = None):
        # Catch DELETE event (on settings_window close)
        if event != None and event.type == gtk.gdk.DELETE:
        	# Hide settings_window
        	self.w("settings_toggle").set_active(False)
        	# Update settings_window's visibility
        	self.show_settings_window()
        	# Cancel window close action (settings_window is already invisible)
        	return True    
    
    def changed_cb(self, combobox):
        '''Detects change of module selection in order to show additional module settings.'''
        model = combobox.get_model()
        index = combobox.get_active()
        
        # If there was any opened settings window -> close it and reset the toggle button
        if self.w('settings_window'):
            self.w('settings_window').destroy()
            self.w("settings_toggle").set_active(False)
        
        # Create a settings window and hide it (for now)    
        self.builder.add_from_file(sys.path[0] + '/modules/' + 'morse_gui.xml')
        self.w('settings_window').set_transient_for(self.w('main_window'))
        self.w('settings_window').connect('delete-event', self.on_settings_window_delete_event)
        self.w('settings_window').set_gravity(gtk.gdk.GRAVITY_STATIC)
        
        print "Hodnota změněna na ", model[index][1]


def myerr(exc_type, exc_value, tb): 
    import traceback; 
    traceback.print_exception(exc_type, exc_value, tb)
    #raw_input()  # comment out for error report without stopping
# minor edit of error reporting -> program will now stop
sys.excepthook = myerr      

# Initialization of the main class
MainInstance = Main()       
# Wait for user input
gtk.main()                  
