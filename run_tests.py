"""Ejecuta todas las pruebas sin instalar nada:  python run_tests.py"""
import os, sys, unittest

RAIZ = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(RAIZ, "src"), os.path.join(RAIZ, "tests")]
resultado = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.discover(os.path.join(RAIZ, "tests")))
sys.exit(0 if resultado.wasSuccessful() else 1)
