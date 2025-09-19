#!/usr/bin/env python3
"""
Script para gerar diagrama de arquitetura da aplicação de classificação de texto
Requer: pip install diagrams
"""

from diagrams import Diagram, Cluster
from diagrams.programming.language import Python
from diagrams.programming.framework import Flask
from diagrams.programming.flowchart import StoredData, Database, Display

def gerar_diagrama():
    with Diagram("Arquitetura - Aplicação de Classificação de Texto", 
                 show=False, 
                 direction="TB",
                 filename="arquitetura_classificacao_texto"):
        
        # Entrada do usuário
        user = Python("Usuário")
        
        # Aplicação principal
        app = Python("app.py\n(Menu Principal)")
        
        # Classificadores
        with Cluster("Classificadores"):
            simples = Python("classificador_simples.py\n(Regras)")
            ml = Python("classificador_ml.py\n(Machine Learning)")
        
        # Componentes ML
        with Cluster("Componentes ML"):
            sklearn = Flask("scikit-learn\n(TfidfVectorizer + MultinomialNB)")
            modelo = StoredData("modelo_classificador.pkl\n(Modelo Salvo)")
        
        # Dados de treinamento
        dados = Database("Dados de Exemplo\n(Textos + Labels)")
        
        # Fluxo principal
        user >> app
        app >> simples
        app >> ml
        
        # Fluxo ML
        ml >> sklearn
        sklearn >> modelo
        dados >> sklearn
        
        # Resultados
        resultado = Display("Resultado:\n✅ VERDADEIRO\n❌ FALSO\n❓ INDETERMINADO")
        
        simples >> resultado
        ml >> resultado

if __name__ == "__main__":
    print("Gerando diagrama de arquitetura...")
    gerar_diagrama()
    print("Diagrama salvo como: arquitetura_classificacao_texto.png")
