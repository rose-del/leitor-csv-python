# 📄 Leitor de Arquivos CSV em Python

Este projeto é um script em Python que lê arquivos CSV de forma flexível e eficiente, funcionando com diferentes formatos de separadores (`,`, `;`,...) e exibindo os dados de forma padronizada no terminal.

---

## Funcionalidades

- 📂 Lê qualquer arquivo CSV informado pelo usuário
- 🔎 Detecta automaticamente o delimitador do arquivo (`;`, `,`, etc.)
- 🧠 Não carrega o arquivo inteiro na memória
- 📊 Exibe os dados de forma organizada no terminal
- ⚠️ Tratamento de erro para arquivo inexistente

---

## Tecnologias utilizadas

- Python 3
- Biblioteca padrão `csv`

---

## Como usar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/rose-del/leitor-csv-python.git
````

Entre na pasta do projeto:

```bash
cd leitor-csv-python
cd leitor
```

---

### 2. Prepare o arquivo CSV

Você pode utilizar seus próprios arquivos CSV ou os arquivos de exemplo que já vêm no projeto.

#### 📁 Arquivos de teste
O projeto possui uma pasta chamada `csv` com alguns arquivos CSV para testes tirados dos sites mencionado mais abaixo.

📌 Para utilizá-los:
- arraste ou copie **um arquivo** da pasta `csv`
- cole o arquivo dentro da pasta `leitor`

#### Observações:
* Baixe ou crie um arquivo CSV
* Sites recomendados para baixar facilmente arquivos **CSV**:
    - https://www.kaggle.com/datasets
    - https://dadosabertos.bcb.gov.br/dataset
* O arquivo **deve estar codificado em UTF-8**
* Coloque o arquivo CSV **dentro da pasta do `leitor`**

Exemplo:

```
leitor/
├── leitor.py
├── dados.csv
```

---

### 3. Execute o programa

No terminal, execute:

```bash
python3 leitor.py
```

Quando solicitado, digite o nome do arquivo CSV:

```text
Digite o nome do arquivo CSV: dados.csv
```

O conteúdo do arquivo será exibido no terminal.

---

## Como o programa funciona por dentro

### Detecção automática do formato do CSV

O programa utiliza o `csv.Sniffer()` para identificar automaticamente:

* o delimitador do arquivo (`;`, `,`, etc.)
* o padrão do CSV

Para isso, ele **não lê o arquivo inteiro**.

### Leitura eficiente de memória

O código lê apenas os **primeiros 1024 bytes** do arquivo para detectar o formato:

```python
amostra = arquivo.read(1024)
arquivo.seek(0)
```

Isso evita:

* alto consumo de memória
* problemas com arquivos CSV muito grandes

Após a detecção, o arquivo é lido normalmente desde o início.

---

## Observações importantes

* Caso o arquivo não esteja em UTF-8, pode ser necessário ajustar o `encoding`
---
