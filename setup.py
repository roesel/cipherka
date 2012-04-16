from distutils.core import setup
import py2exe
import glob

setup(
    name="cipherka",
    windows = [
                  {
                      'script': 'cipherka.py',
                  }
              ],

    options = {
                  'py2exe': {
                      'packages':'encodings',
                      'includes': 'cairo, pango, pangocairo, atk, gobject, gio',
                  }
              },
    data_files=['gui.xml',
                'README',
                ("modules", glob.glob("modules/*.*")),
                ("media", glob.glob("media/*.png"))
    ]
)