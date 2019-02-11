#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
from types import GeneratorType


class MyAboutIterables(Koan):

    def test_Wszystkie_elementy_dwa_razy_większe(self):
        """
        Wyfiltruj element nieparzyste elementy tablicy i pomnóż razy dwa
        """
        tablica = range(10)
        answer = [x *2 for x in tablica if x % 2 != 0] 
        self.assertEqual(answer, [2,6,10,14,18])
        
        # A teraz dla dict klucz to element parzysty a wartość jest równa klucz razy 2
        answer = {x: x * 2 for x in tablica if x % 2 == 0 }
        self.assertEqual(answer, {0:0, 2:4, 4:8, 6:12, 8:16})

        # utórz z tablicy w ten sposób generator
        answer = (x for x in tablica)
        self.assertEqual(type(answer), GeneratorType)
        self.assertEqual(list(answer), [0,1,2,3,4,5,6,7,8,9])

    def test_produkt_kartezjański(self):
        """
        uzywając comprehensions utwórz produkt kartezjański jak poniżej
        """
        result = [(0,1), (0,0), (1,1), (1,0)]
        answer = [(x,y) for x in range(2) for y in range(1,-1,-1)]
        self.assertEqual(answer,result)


    def test_map(self):
        """
        Używając funkcji zamień tekst na odpowiadjącą mu listę wartości unicode
        """
        result = [65, 100, 97, 109]
        text = "Adam"
        answer = list(map(ord, text))
        self.assertEqual(answer, result)


    
        
    
