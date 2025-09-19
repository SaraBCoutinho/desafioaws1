#!/usr/bin/env python3

import json
import os
import sys

def instalar_mcp_server():
    """Instala o MCP server no Q CLI"""
    
    # Caminho do arquivo de configuração do Q CLI
    config_path = os.path.expanduser("~/.config/q/mcp_servers.json")
    
    # Configuração do servidor
    server_config = {
        "classificador-texto": {
            "command": "python3",
            "args": ["mcp_server.py"],
            "cwd": os.getcwd()
        }
    }
    
    # Carrega configuração existente ou cria nova
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        config = {"mcpServers": {}}
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
    
    # Adiciona o servidor
    config["mcpServers"].update(server_config)
    
    # Salva a configuração
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ MCP Server instalado em: {config_path}")
    print("\nPara usar:")
    print("1. Reinicie o Q CLI")
    print("2. Use as ferramentas: classificar_simples e classificar_ml")

if __name__ == "__main__":
    print("=== Instalando MCP Server ===")
    instalar_mcp_server()
