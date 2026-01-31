import csv

nomeDoArquivo = input("Digite o nome do arquivo CSV: ")

try:
    with open(nomeDoArquivo, mode="r", encoding="utf-8") as arquivo:
        amostra = arquivo.read(1024)
        arquivo.seek(0)

        dialeto = csv.Sniffer().sniff(amostra)

        leitor = csv.DictReader(arquivo, dialect=dialeto)

        for linha in leitor:
            print("-"*40)
            for chave, valor in linha.items():
                print(f"{chave}: {valor}")

except FileNotFoundError:
    print("Arquivo não encontrado.")
except csv.Error:
    print("Erro ao interpretar o arquivo CSV.")