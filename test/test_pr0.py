import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PR0 import asigna as caso

def test():
    assert caso.a == 1
    assert caso.b == 2
