#__all__ = ['flip', 'morse', 'reverse', 'vigenere', 'column']
import os
import glob
__all__ = [ os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/*.py") if not f[-11:-3] == "__init__"]
