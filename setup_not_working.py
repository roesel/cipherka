from distutils.core import setup
import py2exe
import glob

setup(
    name="cipherka",
    scripts=["cipherka.py"],
    data_files=[("gui.xml"),
                ("README"),
                ("modules", glob.glob("modules/*.*")),
                ("media", glob.glob("media/*.png"))
    ]
)