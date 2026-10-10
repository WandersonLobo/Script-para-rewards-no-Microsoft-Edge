# Script para Rewards no Microsoft Edge

## Por que este script foi criado?

Este é um mini projeto criado para automatizar pesquisas no Microsoft Edge usando uma lista de termos definida pelo usuário. A ideia é evitar a repetição manual de abrir o navegador, pesquisar cada termo e limpar a caixa de pesquisa entre uma consulta e outra.

O script simula o uso do teclado e, por isso, deve ser executado em um computador Windows com o Microsoft Edge instalado.

## Bibliotecas utilizadas

- [PyAutoGUI](https://pyautogui.readthedocs.io/): simula ações de teclado.
- `json`: lê a lista de pesquisas no arquivo `src/banco.json`.
- `time`: adiciona pausas entre as ações.
- `os` e `sys`: localizam o arquivo `banco.json` tanto no código-fonte quanto no executável.

## Como utilizar

### 1. Defina as pesquisas

Edite o arquivo `src/banco.json` e informe os termos que deseja pesquisar. O arquivo deve conter uma lista de textos, por exemplo:

```json
[
  "notícias de tecnologia",
  "previsão do tempo",
  "receitas fáceis"
]
```

Antes de iniciar, salve seu trabalho e deixe o computador livre para que o script possa controlar o teclado.

### 2. Executar pelo VS Code

Instale o Python e a biblioteca necessária:

```powershell
python -m pip install pyautogui
```

Na pasta do projeto, execute:

```powershell
python main.py
```

O programa abrirá o menu Iniciar, localizará o Microsoft Edge e executará as pesquisas do arquivo `src/banco.json`.

### 3. Gerar e executar o `.exe` com PyInstaller

Instale o PyInstaller:

```powershell
python -m pip install pyinstaller
```

Gere o executável usando o arquivo de configuração do projeto:

```powershell
python -m PyInstaller --clean --noconfirm main.spec
```

Depois, execute:

```powershell
.\dist\main.exe
```

O executável será criado na pasta `dist`. O arquivo `src/banco.json` já está configurado no `main.spec` para ser incluído no empacotamento.

> Use o script somente quando puder deixar o teclado e o mouse sem interação durante a execução. A automação depende da posição e do estado atual da interface do Windows e do Edge.
