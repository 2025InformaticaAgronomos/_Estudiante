import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# test_script_simple.py
from PR1 import ejemplo as pr01

def test_ej1():
    assert pr01.a == 2
    assert pr01.b == 3
    assert pr01.c == 5
def test2_ej2():
    assert pr01.h == 1
    assert pr01.k == 3
    assert pr01.m == 4