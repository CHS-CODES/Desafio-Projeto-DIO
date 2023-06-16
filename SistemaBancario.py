menu = """
================Banco CHS===============

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

==================2023==================

=>
"""

saldo = 0
limite_saque = 3
limite_dia = 500
numero_saque = 0
extrato = " "

while True:
    opcao = input(menu)
    
    if opcao == '1':
        valor = float(input("Informe o valor do Deposito:"))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
    
    elif opcao == '2':
        valor = float(input("Informe o valor de Saque:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_dia
        excedeu_lim_saq = numero_saque >= limite_saque
        
        if excedeu_saldo:
            print("Saldo insuficiente.")
            
        elif excedeu_limite:
            print("Você atingiu o Limite diario de Saque.")
            
        elif excedeu_lim_saq:
            print("Você atingiu limite de numeros de Saques.")
            opcao
            
        elif valor > 0:
            saldo -= valor
            extrato += f" Saque: R$ {valor:.2f}\n"
            numero_saque +=1
            print("Saque Realizado com Sucesso!")
        
        else:
            print("Operação Falhou! Valor é invalido")
    
    elif opcao == '3':
        print("\n================Extrato================")
        print("Não foram realizadas movimentação." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=========================================")
        
    elif opcao == '4':
        print("============Obrigado por usar CHS==============")
        break
    
    else:
        print("Operação invalido, digite novamente a opção desejada.")