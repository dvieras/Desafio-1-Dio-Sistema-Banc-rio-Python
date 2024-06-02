saldo = 2000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
    ========== Menu ==========
    
    Escolha uma das opções a seguir:
     
    [1] - Sacar
    [2] - Depositar
    [3] - Extrato
    [0] - Sair

    ==========================
"""

while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor a ser sacado: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
    
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")
            
        elif excedeu_saques:
            print("Operação falhou! Número maximo de saques excedido.")
            
        elif valor > 0: 
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Valor sacado com Sucesso.")
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é invalido.")
            
    elif opcao == 2:
        valor = float(input("Informe o valor a ser Depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação realizado com sucesso!.")
            
        else:
            print("Operação falhou ! O valor informado é inválido.")
        
    elif opcao == 3:
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=============================")
        
    elif opcao == 0:
        print("Obrigado por usar nosso serviço. Até logo!")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
        
