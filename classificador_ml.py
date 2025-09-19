
#!/usr/bin/env python3

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle
import os

class ClassificadorML:
    def __init__(self):
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=1000)),
            ('classifier', MultinomialNB())
        ])
        self.treinado = False
    
    def treinar(self, textos, labels):
        """Treina o modelo com dados de exemplo"""
        self.pipeline.fit(textos, labels)
        self.treinado = True
    
    def classificar(self, texto):
        """Classifica um texto como True ou False"""
        if not self.treinado:
            raise ValueError("Modelo não foi treinado")
        
        resultado = self.pipeline.predict([texto])[0]
        confianca = max(self.pipeline.predict_proba([texto])[0])
        
        return resultado, confianca
    
    def salvar_modelo(self, caminho):
        """Salva o modelo treinado"""
        with open(caminho, 'wb') as f:
            pickle.dump(self.pipeline, f)
    
    def carregar_modelo(self, caminho):
        """Carrega um modelo salvo"""
        with open(caminho, 'rb') as f:
            self.pipeline = pickle.load(f)
        self.treinado = True

def criar_dados_exemplo():
    """Cria dados de exemplo para treinamento"""
    textos = [
        "Isso é verdade", "Está correto", "Sim, confirmo",
        "É verdadeiro", "Positivo", "Certo",
        "Isso é falso", "Está errado", "Não, nego",
        "É mentira", "Negativo", "Incorreto"
    ]
    
    labels = [True, True, True, True, True, True,
              False, False, False, False, False, False]
    
    return textos, labels

def main():
    classificador = ClassificadorML()
    modelo_path = "modelo_classificador.pkl"
    
    # Verifica se existe modelo salvo
    if os.path.exists(modelo_path):
        print("Carregando modelo salvo...")
        classificador.carregar_modelo(modelo_path)
    else:
        print("Treinando novo modelo...")
        textos, labels = criar_dados_exemplo()
        classificador.treinar(textos, labels)
        classificador.salvar_modelo(modelo_path)
        print("Modelo treinado e salvo!")
    
    print("\n=== Classificador ML (Verdadeiro/Falso) ===")
    
    while True:
        texto = input("\nDigite um texto (ou 'sair' para terminar): ")
        
        if texto.lower() == 'sair':
            break
        
        try:
            resultado, confianca = classificador.classificar(texto)
            emoji = "✅" if resultado else "❌"
            status = "VERDADEIRO" if resultado else "FALSO"
            print(f"{emoji} {status} (Confiança: {confianca:.2%})")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
