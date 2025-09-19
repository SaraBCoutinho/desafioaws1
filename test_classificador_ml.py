#!/usr/bin/env python3

import unittest
import os
import tempfile
from classificador_ml import ClassificadorML, criar_dados_exemplo

class TestClassificadorML(unittest.TestCase):
    
    def setUp(self):
        """Configura o teste com um classificador treinado"""
        self.classificador = ClassificadorML()
        textos, labels = criar_dados_exemplo()
        self.classificador.treinar(textos, labels)
    
    def test_treinamento(self):
        """Testa se o modelo foi treinado corretamente"""
        self.assertTrue(self.classificador.treinado)
    
    def test_classificacao_basica(self):
        """Testa classificação básica"""
        resultado, confianca = self.classificador.classificar("Isso é verdade")
        self.assertIsInstance(resultado, bool)
        self.assertGreater(confianca, 0)
        self.assertLessEqual(confianca, 1)
    
    def test_erro_modelo_nao_treinado(self):
        """Testa erro quando modelo não foi treinado"""
        classificador_novo = ClassificadorML()
        with self.assertRaises(ValueError):
            classificador_novo.classificar("teste")
    
    def test_salvar_carregar_modelo(self):
        """Testa salvar e carregar modelo"""
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pkl') as tmp:
            tmp_path = tmp.name
        
        try:
            # Salva modelo
            self.classificador.salvar_modelo(tmp_path)
            self.assertTrue(os.path.exists(tmp_path))
            
            # Carrega modelo
            novo_classificador = ClassificadorML()
            novo_classificador.carregar_modelo(tmp_path)
            self.assertTrue(novo_classificador.treinado)
            
            # Testa se funciona
            resultado, _ = novo_classificador.classificar("teste")
            self.assertIsInstance(resultado, bool)
            
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    def test_dados_exemplo(self):
        """Testa criação de dados de exemplo"""
        textos, labels = criar_dados_exemplo()
        self.assertEqual(len(textos), len(labels))
        self.assertGreater(len(textos), 0)
        self.assertTrue(all(isinstance(label, bool) for label in labels))

if __name__ == "__main__":
    unittest.main()
