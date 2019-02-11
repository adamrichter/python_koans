#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
from .hardcoded import *


class MyAboutExample(Koan):

    def test_zmienna_sciezek_do_modolow(self):
        """
        Wskaż zmienną Python w której przetrzymywane są ścieżki do modółów
        """
        import sys
        self.assertEqual(sys.path, sciezki)
        # A teraz ścieżkę do zmiennej systemowej jako string 
        self.assertEqual('$PYTHONPATH', sciezki_zmienna_systemowa)



