# Instruções de Execução com Ambiente Virtual (venv)

Este guia explica como configurar e utilizar um ambiente virtual (`venv`) em Python para executar os scripts deste repositório sem erros de módulos ausentes, como:

```text
Traceback (most recent call last):
  File "estatistica/atividade_desvio_padrao.py", line 19, in <module>
    import matplotlib
ModuleNotFoundError: No module named 'matplotlib'
```

---

## 1. Por que esse erro acontece?

O erro `ModuleNotFoundError: No module named 'matplotlib'` (ou `numpy`, `pandas`) ocorre quando o script é executado pelo interpretador global do sistema (ex: `/usr/bin/python3`), onde essas bibliotecas externas não estão instaladas.

Para resolver, deve-se utilizar o **ambiente virtual (`.venv`)** do projeto, que contém todas as dependências isoladas listadas no arquivo [`requirements.txt`](./requirements.txt).

---

## 2. Guia Rápido (Se o `.venv` já existir)

Se a pasta `.venv/` já estiver criada na raiz do repositório:

### Opção A: Ativando o ambiente virtual no terminal (Recomendado)

1. Certifique-se de estar na **pasta raiz do repositório** (`data-science/`):
   ```bash
   # Se estiver dentro de uma subpasta (como 'estatistica/'), volte para a raiz:
   cd ~/workspace/data-science
   ```

2. Ative o ambiente virtual:
   - **Linux / macOS (na raiz do projeto)**:
     ```bash
     source .venv/bin/activate
     ```
     *(Se você já estiver dentro da pasta `estatistica/`, use `source ../.venv/bin/activate`)*
   - **Windows (PowerShell)**:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **Windows (Prompt de Comando / CMD)**:
     ```cmd
     .venv\Scripts\activate.bat
     ```

3. Note que o prefixo `(.venv)` aparecerá no início da linha do seu terminal.

4. Execute o script desejado:
   - Se estiver na raiz (`data-science/`):
     ```bash
     python estatistica/atividade_desvio_padrao.py
     ```
   - Se estiver dentro da pasta `estatistica/`:
     ```bash
     python atividade_desvio_padrao.py
     ```

5. Quando terminar, para sair do ambiente virtual:
   ```bash
   deactivate
   ```

---

### Opção B: Executando direto pelo binário do `.venv` (Sem ativar)

Você pode invocar diretamente o executável do Python do ambiente virtual sem precisar ativá-lo:

- **Linux / macOS**:
  - Se estiver na raiz (`data-science/`):
    ```bash
    ./.venv/bin/python estatistica/atividade_desvio_padrao.py
    ```
  - Se estiver dentro da pasta `estatistica/`:
    ```bash
    ../.venv/bin/python atividade_desvio_padrao.py
    ```

- **Windows**:
  - Se estiver na raiz (`data-science\`):
    ```powershell
    .venv\Scripts\python.exe estatistica\atividade_desvio_padrao.py
    ```
  - Se estiver dentro da pasta `estatistica\`:
    ```powershell
    ..\.venv\Scripts\python.exe atividade_desvio_padrao.py
    ```

---

## 3. Passo a Passo Completo (Criação e Instalação do Zero)

Se precisar recriar ou configurar o ambiente do zero em uma nova máquina:

### Passo 1: Criar o ambiente virtual `.venv`

Na pasta raiz do projeto:

- **Linux / macOS**:
  ```bash
  python3 -m venv .venv
  ```
  > **Atenção (Ubuntu/Debian):** Se receber o aviso `The virtual environment was not created successfully because ensurepip is not available`, instale o pacote do sistema:
  > ```bash
  > sudo apt update && sudo apt install -y python3-venv python3-pip
  > ```

- **Windows**:
  ```powershell
  python -m venv .venv
  ```

---

### Passo 2: Ativar o ambiente virtual

- **Linux / macOS**:
  ```bash
  source .venv/bin/activate
  ```

- **Windows (PowerShell)**:
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
  *(Se o PowerShell bloquear a execução de scripts, execute antes: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`)*

- **Windows (CMD)**:
  ```cmd
  .venv\Scripts\activate.bat
  ```

---

### Passo 3: Instalar as bibliotecas do `requirements.txt`

Com o ambiente virtual ativo `(.venv)`:

```bash
pip install -r requirements.txt
```

As seguintes bibliotecas e suas dependências serão instaladas:
- `matplotlib` (Geração e plotagem de gráficos)
- `pandas` (Manipulação e formatação de tabelas de dados)
- `numpy` (Operações numéricas e matriciais)

---

### Passo 4: Executar os scripts

Exemplos de execução:

```bash
# Atividade de Estatística (Média, Desvio Padrão e Gráficos)
python estatistica/atividade_desvio_padrao.py

# Tutorial de Vendas
python tutorial_python/analise_vendas_mensais.py
```

---

## 4. Configuração no VS Code / Antigravity / Cursor

Para que o botão de "Run" (Play) da IDE e o autocomplete usem o `.venv` automaticamente:

1. Abra a paleta de comandos: `Ctrl + Shift + P` (ou `Cmd + Shift + P` no macOS).
2. Digite e selecione: **`Python: Select Interpreter`**.
3. Escolha o interpretador correspondente ao `.venv`:
   - Exemplo: `Python 3.12.x ('.venv': venv) ./.venv/bin/python`
4. Abra um novo terminal integrado na IDE (`Ctrl + '`). Ele detectará o `.venv` e o ativará automaticamente com o prefixo `(.venv)`.

---

## 5. Alternativa Rápida com `uv`

Este repositório possui suporte ao gerenciador `uv` (localizado em `.bin/uv`). Caso queira utilizá-lo:

```bash
# 1. Criar o venv
./.bin/uv venv .venv

# 2. Instalar os pacotes
./.bin/uv pip install -r requirements.txt

# 3. Executar o script
./.venv/bin/python estatistica/atividade_desvio_padrao.py
```

---

## 6. Resolução de Dúvidas e Erros Frequentes

| Erro / Situação | Causa | Solução |
| :--- | :--- | :--- |
| `ModuleNotFoundError: No module named 'matplotlib'` | O terminal está usando o Python global em vez do `.venv`. | Execute `source .venv/bin/activate` ou use `./.venv/bin/python script.py`. |
| `bash: .venv/bin/activate: No such file or directory` | O comando foi executado dentro de uma subpasta (ex: `estatistica/`). | Volte para a raiz com `cd ..` e execute `source .venv/bin/activate`, ou use `source ../.venv/bin/activate`. |
| `ensurepip is not available` ao criar o venv no Linux | Sistema Debian/Ubuntu sem o pacote `python3-venv`. | Execute `sudo apt install python3-venv python3-pip`. |
| `Activate.ps1 cannot be loaded...` no Windows | Política de execução de scripts restrita no PowerShell. | Execute `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`. |
| Imagem do gráfico não abre na tela | Ambiente headless (terminal sem interface gráfica/X11). | O script detecta automaticamente e salva a imagem em [`estatistica/grafico_desvio_padrao.png`](./estatistica/grafico_desvio_padrao.png). |

