#Exemplo de encadeamento / aninhamento
tem_cartao = False
saldo = 70.0

if tem_cartao:
    if saldo >= 100: 
        print("Compra Aprovada, saldo suficiente")
    else:
        print("Compra Negada, saldo insuficiente")

else:
    print("Erro, cartão não inserido")