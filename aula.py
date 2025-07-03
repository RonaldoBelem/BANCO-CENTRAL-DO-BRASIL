import datetime

print("===================================")
print("   BEM-VINDO AO BANCO PYTHONBANK   ")
print("===================================\n")

usuario = input("Crie seu nome de usuário: ")
senha = input("Crie sua senha: ")

print("\nCadastro realizado com sucesso!")
print(f"Bem-vindo, {usuario}!\n")

menu = """
=========== MENU ===========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
============================

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

# Autenticação
while True:
    print("🔐 Faça login para continuar:")
    login = input("Usuário: ")
    senha_digitada = input("Senha: ")

    if login == usuario and senha_digitada == senha:
        print("\n✅ Login realizado com sucesso!\n")
        break
    else:
        print("❌ Usuário ou senha incorretos. Tente novamente.\n")

# Loop principal
while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append({"tipo": "Depósito", "valor": valor, "data": data})
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("❌ Operação falhou! Valor inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("❌ Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("❌ Operação falhou! Saque acima do limite.")
        elif excedeu_saques:
            print("❌ Operação falhou! Número de saques excedido.")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append({"tipo": "Saque", "valor": valor, "data": data})
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("❌ Operação falhou! Valor inválido.")

    elif opcao == "e":
        print("\n========= EXTRATO =========")
        if not extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for item in extrato:
                print(f"{item['data']} - {item['tipo']}: R$ {item['valor']:.2f}")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===========================\n")

    elif opcao == "q":
        confirma = input("Tem certeza que deseja sair? (s/n): ").lower()
        if confirma == "s":
            print("\nObrigado por usar o PythonBank. Até logo!\n")
            break
        else:
            print("👍 Operação cancelada. Voltando ao menu...\n")

    else:
        print("❌ Opção inválida. Tente novamente.\n")

