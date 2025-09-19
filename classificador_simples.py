#!/usr/bin/env python3

def classificar_texto(texto):
    """Classifica texto como verdadeiro ou falso baseado em palavras-chave"""
    texto = texto.lower()
    
    palavras_verdadeiro = ['sim', 'verdade', 'correto', 'certo', 'positivo', 'confirmo']
    palavras_falso = ['não', 'falso', 'incorreto', 'errado', 'negativo', 'nego']
    
    for palavra in palavras_verdadeiro:
        if palavra in texto:
            return True
    
    for palavra in palavras_falso:
        if palavra in texto:
            return False
    
    return None  # Indeterminado

def main():
    print("=== Classificador de Texto (Verdadeiro/Falso) ===")
    
    while True:
        texto = input("\nDigite um texto (ou 'sair' para terminar): ")
        
        if texto.lower() == 'sair':
            break
            
        resultado = classificar_texto(texto)
        
        if resultado is True:
            print("✅ VERDADEIRO")
        elif resultado is False:
            print("❌ FALSO")
        else:
            print("❓ INDETERMINADO")

if __name__ == "__main__":
    main()
