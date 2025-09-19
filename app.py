#!/usr/bin/env python3

import sys
from classificador_simples import classificar_texto
from classificador_ml import ClassificadorML, criar_dados_exemplo
import os

def main():
    print("=== Aplicação de Classificação de Texto ===")
    print("1. Classificador Simples (regras)")
    print("2. Classificador ML (machine learning)")
    
    escolha = input("\nEscolha uma opção (1 ou 2): ")
    
    if escolha == "1":
        usar_classificador_simples()
    elif escolha == "2":
        usar_classificador_ml()
    else:
        print("Opção inválida!")

def usar_classificador_simples():
    print("\n--- Classificador Simples ---")
    while True:
        texto = input("Digite um texto (ou 'voltar'): ")
        if texto.lower() == 'voltar':
            break
        
        resultado = classificar_texto(texto)
        if resultado is True:
            print("✅ VERDADEIRO")
        elif resultado is False:
            print("❌ FALSO")
        else:
            print("❓ INDETERMINADO")

def usar_classificador_ml():
    print("\n--- Classificador ML ---")
    classificador = ClassificadorML()
    
    if os.path.exists("modelo_classificador.pkl"):
        classificador.carregar_modelo("modelo_classificador.pkl")
    else:
        textos, labels = criar_dados_exemplo()
        classificador.treinar(textos, labels)
        classificador.salvar_modelo("modelo_classificador.pkl")
    
    while True:
        texto = input("Digite um texto (ou 'voltar'): ")
        if texto.lower() == 'voltar':
            break
        
        resultado, confianca = classificador.classificar(texto)
        emoji = "✅" if resultado else "❌"
        status = "VERDADEIRO" if resultado else "FALSO"
        print(f"{emoji} {status} (Confiança: {confianca:.2%})")

if __name__ == "__main__":
    main()
