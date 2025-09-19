#!/usr/bin/env python3

import unittest
import sys

def executar_todos_testes():
    """Executa todos os testes unitários"""
    
    # Descobre e executa todos os testes
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')
    
    # Executa os testes
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Retorna código de saída baseado no resultado
    return 0 if result.wasSuccessful() else 1

if __name__ == "__main__":
    print("=== Executando Testes Unitários ===\n")
    exit_code = executar_todos_testes()
    
    if exit_code == 0:
        print("\n✅ Todos os testes passaram!")
    else:
        print("\n❌ Alguns testes falharam!")
    
    sys.exit(exit_code)
