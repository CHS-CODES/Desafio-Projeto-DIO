import textwrap

#cria tela principal de acesso a menu.
def menu():
    menu = """\n
    ================Banco CHS===============

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo Usuario
    [5]\tNova Conta
    [6]\tlista de Contas
    [7]\tSair

    ==================2023==================
    => """
    return input(textwrap.dedent(menu))

#função de depositar devera ser Positional only - argumentos apenas por posição
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: \t R$ {valor:.2f}\n"
        print("\n=== Deposito Realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! Valor invalido. @@@")
        
    return saldo, extrato

#função de sacar devera ser Keyword only - argumentos apenas por nome
def saque(*, saldo, valor, extrato, limite, numero_saques, limt_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_lim_saq = numero_saques >= limt_saques
    
    if excedeu_saldo:
        print("\n@@@ Saldo insuficiente! @@@")
        
    elif excedeu_limite:
        print("\n @@@ Você atingiu o Limite por Saque! @@@")
        
    elif excedeu_lim_saq:
        print("\n @@@ Você atingiu limite de numeros de Saques! @@@")
        
    elif valor > 0:
        saldo -= valor
        extrato += f" Saque: \t R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque Realizado com Sucesso! ===")
    
    else:
        print("\n @@@ Operação Falhou! Valor é invalido! @@@")
        
    return saldo, extrato

#função de extrato devera ser por Keyword e Positional.            
def exibir_extrato(saldo, /, *, extrato):
    print("\n================Extrato================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo: \t R$ {saldo:.2f}")
    print("=========================================")
        
def criar_usuario(usuarios):
    cpf = input("Informe seu CPF")
    usuario = filtrar_usuario(cpf, usuarios)     
    
    if usuario:
        print("\n @@@ Já existe usuário com esse CPF! @@@")
        return  
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe sua data de nascimento(dd-mm-aaaa): ")    
    endereco = input("Informe seu endereço(Logadouro, Nº - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})
    print("=== Úsuario criado com sucesso! ===")
     
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, num_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n === Conta criada com sucesso! ===")
        return {"agencia":agencia, "num_conta":num_conta, "usuario":usuario}
    
    print("\n@@@ Usuário não encontrado, criação de conta encerrado! @@@")

def lista_contas(contas):
    for conta in contas:
        linha = f"""\
          Agência:\t{conta['agencia']}''
          C/C:\t\t{conta['num_conta']}
          Titular:\t{conta['usuario']['nome']}
        """    
        print("=" * 100)
        print(textwrap.dedent(linha))
    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    numero_saques = 1
    extrato = " "
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "1": #Deposito
            valor = float(input("Informe o valor do Deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "2": #Saque
            valor = float(input("Informe o valor do Saque: "))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limt_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "3": #Extrato
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4": #Criar Usuario
            criar_usuario(usuarios)
            
        elif opcao == "5": #Criar Contas
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, num_conta, usuarios)
            
            if conta:
                contas.append(conta)
        
        elif opcao == "6": #Listar Contas
            lista_contas(contas)
            
        elif opcao == "7": #Sair
            print("\n === Operação Finalizada! ===")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
main()
