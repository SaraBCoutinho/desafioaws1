#!/usr/bin/env python3

import unittest
from classificador_simples import classificar_texto

class TestClassificadorSimples(unittest.TestCase):
    
    def test_palavras_verdadeiro(self):
        """Testa palavras que devem retornar True"""
        self.assertTrue(classificar_texto("Sim, isso é verdade"))
        self.assertTrue(classificar_texto("Está correto"))
        self.assertTrue(classificar_texto("É positivo"))
        self.assertTrue(classificar_texto("Confirmo que sim"))
    
    def test_palavras_falso(self):
        """Testa palavras que devem retornar False"""
        self.assertFalse(classificar_texto("Não, isso é falso"))
        self.assertFalse(classificar_texto("Está errado"))
        self.assertFalse(classificar_texto("É negativo"))
        self.assertFalse(classificar_texto("Nego essa informação"))
    
    def test_texto_indeterminado(self):
        """Testa textos que devem retornar None"""
        self.assertIsNone(classificar_texto("Texto neutro"))
        self.assertIsNone(classificar_texto("Informação qualquer"))
        self.assertIsNone(classificar_texto(""))
    
    def test_case_insensitive(self):
        """Testa se funciona com maiúsculas e minúsculas"""
        self.assertTrue(classificar_texto("SIM"))
        self.assertFalse(classificar_texto("NÃO"))
        self.assertTrue(classificar_texto("Verdade"))

if __name__ == "__main__":
    unittest.main()
