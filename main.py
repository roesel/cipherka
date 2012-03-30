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
        ## Vytvoření widgetů a přidání obsluh událostí podle Glade
        self.builder = gtk.Builder()
        self.builder.add_from_file(sys.path[0] + '/' + 'gui.xml') 
        self.builder.connect_signals(self)       
        self.w('main_window').connect('destroy', lambda w: gtk.main_quit()) # zavření okna -> ukončení programu
        self.all_modules = modules.__init__.__all__
        #print(self.all_modules)
        
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

        ## Nastavení liststore s daty pro combobox1
        self.w("modules_selector").set_model(muj_liststore)

        # U comboboxu1 přidáme renderery pro obrázek a text (viz lekce 17)
        renderer = gtk.CellRendererPixbuf()
        self.w("modules_selector").pack_start(renderer, expand=False)
        self.w("modules_selector").add_attribute(renderer, 'pixbuf', 0)

        renderer = gtk.CellRendererText()
        self.w("modules_selector").pack_start(renderer, expand=True)
        self.w("modules_selector").add_attribute(renderer, 'text', 1)        

        ## Předvybrání první položky 
        self.w("modules_selector").set_active(0)

        ## Přidání obsluhy událostí
        self.w('modules_selector').connect('changed', self.changed_cb)

        self.w('main_window').show_all()
        
        self.changed_cb(self.w("modules_selector"))
    
    def show_settings_window(self):
        if self.w("settings_toggle").get_active():
            self.w('settings_window').show()
        else:
            self.w('settings_window').hide()
            
    def w(self, widgetname):
        '''Pomůcka pro stručný přístup k widgetům'''
        return self.builder.get_object(widgetname)
    
    def process(self, input, method, parameters=None):
        '''This function initiates encryption/decryption by calling the selected module and returning the result.'''
        #sys.path.append('modules')    # Allow importing from folder
        #self.method = 'modules.' + method
        sys.path.append(os.path.join(sys.path[0], 'modules'))   # Allow importing from folder
        self.method = method
        #self.module = __import__(method)    # Import module by name
        self.module = __import__(self.method, globals(), locals(), [self.method], -1)    # Import module by name and return it (not __init__.py)
        return self.module.run(input, parameters)    # Call the function inside the module

    ## Odsud obsluhy událostí
    def on_settings_toggle_toggled(self, widget):
        self.show_settings_window()
    
    def on_start_clicked(self, widget):
        '''Calls the 'process' function and supplies it with necessary parameters.'''
        
        # Get selected module
        model = self.w('modules_selector').get_model()
        index = self.w('modules_selector').get_active()
        
        selected_module = model[index][1]
        print "Selected module:", selected_module
        
        input = self.w('inputText').get_text(self.w('inputText').get_start_iter(), self.w('inputText').get_end_iter())
        print('Input: ' + input)
        #self.output = self.process(self.input, 'morse', None) # Call the module "morse"
        #output = self.process(input, 'vigenere', None) # Call the module "vigenere"
        #self.output = self.process(self.input, 'flip', None) # Call the module "flip"
        #self.output = self.process(self.input, 'reverse', None) # Call the module "reverse"
        output = self.process(input, selected_module, None) # Call the module "vigenere"
        print('Output: ' + output)
        self.w('outputText').set_text(output)
    
    def changed_cb(self, combobox):
        '''Detects change of module selection in order to show additional module settings.'''
        model = combobox.get_model()
        index = combobox.get_active()
        
        self.builder.add_from_file(sys.path[0] + '/modules/' + 'morse_gui.xml')
        self.w('settings_window').show_all()
        self.w('settings_window').hide()
        
        print "Hodnota změněna na ", model[index][1]


def myerr(exc_type, exc_value, tb): 
    import traceback; 
    traceback.print_exception(exc_type, exc_value, tb)
    #raw_input()  # smažte pro výpis chyby bez pozastavení; přejmenujte na input() v pythonu3
sys.excepthook = myerr      # úprava výpisu chyb, aby se program pozastavil po výpisu

MainInstance = Main()       # inicializace hlavní třídy programu
gtk.main()                  # program čeká na události, které vyvolá uživatel
