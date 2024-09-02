titulo = 'Menu'
titulo = titulo.center(14,'#')


saldo = 0
LIM_SAQUE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



menu = f"""
{titulo}

[1] - Saque
[2] - Deposito
[3] - Extrato
[4] - Saida

"""

def salvarExtrato(tipo,operacao):
    global extrato
    tipoOperacao=''
    if tipo == 1:
        tipoOperacao="SAQUE"
    elif tipo == 2:
        tipoOperacao ="DEPOSITO"
    extrato += f"\n{tipoOperacao}: {operacao}"
    
    
def saque(saldo,numero_saques,LIM_SAQUE,LIMITE_SAQUES):
    if(numero_saques < LIMITE_SAQUES):
        texto_saque = 'Informe o valor de saque: '
        valor = float(input(texto_saque))
        if(saldo > valor ):
            if(valor <= LIM_SAQUE):
                numero_saques +=1
                saldo_anterior = saldo
                saldo -= valor
                operacao = f"""
    Saque Diário número {numero_saques-1}
    Saldo Anterior: R${saldo_anterior:.2f}
    Valor de Saque: R${valor:.2f}
    Saldo Final:  : R${saldo:.2f}"""
                salvarExtrato(1,operacao)
                return saldo,numero_saques
            else:
                print( "Você possui saldo suficiente, mas o valor de saque excedeu o limite por operação")
        else:
            print( "Saldo insuficiente")
    else:
        print( "Você já fez 3 operações de saque, limite diário atingido!")
    return saldo,numero_saques


def deposito(saldo):
    texto_deposito = 'Informe o valor do seu depósito: '
    valor  = float(input(texto_deposito))
    saldo_anterior = saldo
    saldo+=valor
    operacao = f"""
    Saldo Anterior: R${saldo_anterior:.2f}
    Valor do Depósito: R${valor:.2f}
    Saldo Final:  R${saldo:.2f}"""
    salvarExtrato(2,operacao)
    
    
    return saldo

def exibir_extrato():
    global extrato
    titulo = "EXTRATO"
    titulo = titulo.center(20,"#")
    
    print(f"""
          {titulo}
          {extrato}""")

while True:
    opcao = int(input(menu))

    if opcao != 4:
        if opcao == 1:
            saldo, numero_saques = saque(saldo,numero_saques,LIM_SAQUE,LIMITE_SAQUES)
        elif opcao == 2:
            saldo = deposito(saldo)
        elif opcao == 3:
            exibir_extrato()
        else:
            print("""Opção inválida, por favor selecione dentre as opções listadas!""")
    else:
        break
    
    
    
    