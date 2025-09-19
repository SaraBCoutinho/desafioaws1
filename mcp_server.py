#!/usr/bin/env python3

import asyncio
import json
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from classificador_simples import classificar_texto
from classificador_ml import ClassificadorML, criar_dados_exemplo
import os

# Inicializa o servidor MCP
server = Server("classificador-texto")

# Inicializa o classificador ML
classificador_ml = ClassificadorML()
if os.path.exists("modelo_classificador.pkl"):
    classificador_ml.carregar_modelo("modelo_classificador.pkl")
else:
    textos, labels = criar_dados_exemplo()
    classificador_ml.treinar(textos, labels)
    classificador_ml.salvar_modelo("modelo_classificador.pkl")

@server.list_tools()
async def list_tools():
    """Lista as ferramentas disponíveis"""
    return [
        Tool(
            name="classificar_simples",
            description="Classifica texto usando regras simples (verdadeiro/falso)",
            inputSchema={
                "type": "object",
                "properties": {
                    "texto": {
                        "type": "string",
                        "description": "Texto para classificar"
                    }
                },
                "required": ["texto"]
            }
        ),
        Tool(
            name="classificar_ml",
            description="Classifica texto usando machine learning (verdadeiro/falso)",
            inputSchema={
                "type": "object",
                "properties": {
                    "texto": {
                        "type": "string",
                        "description": "Texto para classificar"
                    }
                },
                "required": ["texto"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    """Executa a ferramenta solicitada"""
    
    if name == "classificar_simples":
        texto = arguments.get("texto", "")
        resultado = classificar_texto(texto)
        
        if resultado is True:
            resposta = "✅ VERDADEIRO"
        elif resultado is False:
            resposta = "❌ FALSO"
        else:
            resposta = "❓ INDETERMINADO"
        
        return [TextContent(type="text", text=resposta)]
    
    elif name == "classificar_ml":
        texto = arguments.get("texto", "")
        resultado, confianca = classificador_ml.classificar(texto)
        
        emoji = "✅" if resultado else "❌"
        status = "VERDADEIRO" if resultado else "FALSO"
        resposta = f"{emoji} {status} (Confiança: {confianca:.2%})"
        
        return [TextContent(type="text", text=resposta)]
    
    else:
        raise ValueError(f"Ferramenta desconhecida: {name}")

async def main():
    """Função principal do servidor"""
    async with stdio_server() as streams:
        await server.run(*streams)

if __name__ == "__main__":
    asyncio.run(main())
