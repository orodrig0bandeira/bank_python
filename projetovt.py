# Criar um sistema bancário simples utilizando Python ou outra linguagem de back
# 1-login
# 2-depósito
# 3-saca


#começo do projeto


usuario = input("qual é o seu usuário?")
senha = input("qual é sua senha?")
u = "negao"
s = "123"
informacoes = 0

if usuario == u and senha == s:
    print("Entrou")
    print("opções")

# acesso ao usuário
    
while True:
    print("\nEscolha uma opção:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Iformar")
    print("4 - Sair")

    opcoes = input("Digite uma das opções acima: ")

    if opcoes == "1":
        valor_deposito = float(input("Digite o valor do depósito: "))
        informacoes += valor_deposito
        print(f"O valor depositado é R$:{valor_deposito:.2f}")

    elif opcoes == "2": 
        valor_saque = float(input("Digite o valor do saque: "))
        informacoes -= valor_saque
        print(f"O valor do saque será R$:{valor_saque:.2f}")

    elif opcoes == "3":
        print(f"Informações bancárias: Saldo bancário é de R$:{informacoes:.2f}")
    
    elif opcoes == "4":
        print("Sessão encerrada, até mais!")
        break
    
    else:
        print("Opção inválida. Por favor, digite novamente.")