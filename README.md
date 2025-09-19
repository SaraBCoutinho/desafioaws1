Projeto utilizando prompts em terminal vscode. 

# Aplicação de Classificação de Texto

Classifica textos como **Verdadeiro** ou **Falso** usando duas abordagens diferentes.

## Instalação

```bash
pip install -r requirements.txt
```

## Como usar

### Aplicação principal
```bash
python3 app.py
```

### Classificadores individuais
```bash
# Classificador simples
python3 classificador_simples.py

# Classificador ML
python3 classificador_ml.py
```

### MCP Server (Model Context Protocol)
```bash
# Instalar como MCP server
python3 instalar_mcp.py

# Executar servidor diretamente
python3 mcp_server.py
```

### Testes unitários
```bash
# Executar todos os testes
python3 executar_testes.py

# Executar testes individuais
python3 test_classificador_simples.py
python3 test_classificador_ml.py
```

### Gerar diagrama de arquitetura
```bash
python3 gerar_diagrama.py
```

## Arquivos

- `app.py` - Aplicação principal
- `classificador_simples.py` - Classificador baseado em regras
- `classificador_ml.py` - Classificador com machine learning
- `mcp_server.py` - Servidor MCP para integração com Q CLI
- `mcp_config.json` - Configuração do servidor MCP
- `instalar_mcp.py` - Script de instalação do MCP server
- `test_classificador_simples.py` - Testes do classificador simples
- `test_classificador_ml.py` - Testes do classificador ML
- `executar_testes.py` - Script para executar todos os testes
- `gerar_diagrama.py` - Script para gerar diagrama de arquitetura
- `requirements.txt` - Dependências Python

## Ferramentas MCP

Após instalar como MCP server, você terá acesso a:

- `classificar_simples` - Classificação baseada em regras
- `classificar_ml` - Classificação com machine learning
