import csv

dados_tabela = [
    ["Nome","Cargo","Idade"],
    ["Carlos","Analista",21],
    ["Ana","Desempregada",30],
    ["Pelé","Jogador",28],
    ["Lucas","Estagiário",18]
]

with open ("08.2-funcionarios.csv","w",encoding="utf-8",newline="") as arquivo_csv:
    escrever = csv.writer(arquivo_csv)
    escrever.writerows(dados_tabela)