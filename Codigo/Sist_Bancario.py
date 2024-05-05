import os

def limpar():
    os.system("cls")

class SistemaBancario:
    def __init__(self, saldo):
        self.__saldo = saldo
        self.__limite = 500
        self.__n_saque = 0
        self.__LIMITE_SAQUE = 3
        self.__extrato = []
        self.__menu = """
Bem-vindo ao Sistema bancário!

Suas opções são:
[1] Depositar
[2] Sacar
[3] Visualizar extrato
[4] Sair
"""

    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.__limite
    
    def get_n_saque(self):
        return self.__n_saque

    def get_LIMITE_SAQUE(self):
        return self.__LIMITE_SAQUE
    
    def get_extrato(self):
        return self.__extrato
    
    def get_menu(self):
        return self.__menu
    
    def set_saldo(self, novo_saldo):
        self.__saldo = novo_saldo
    
    def set_n_saque(self, novo_n_saque):
        self.__n_saque = novo_n_saque
    
    def set_extrato(self, novo_extrato):
        self.__extrato = novo_extrato

    def depositar(self):
        limpar()
        saldo = self.get_saldo()
        extrato = self.get_extrato()
        try:
            valor_dep = float(input("Quanto deseja depósitar: "))
            if valor_dep >= 0:
                saldo += valor_dep
                self.set_saldo(saldo)
                extrato.append(f"+R${valor_dep:.2f}")   
                self.set_extrato(extrato)
            else:
                print("Só pode depositar com número positivos!")
        except ValueError:
            print("Valor inválido!")
   
    def sacar(self):
        limpar()
        saldo = self.get_saldo()
        limite = self.get_limite()
        n_saque = self.get_n_saque()
        LIMITE_SAQUE = self.get_LIMITE_SAQUE()
        extrato = self.get_extrato()

        if n_saque < LIMITE_SAQUE:
            try:
                valor_saq = float(input("Quanto deseja sacar: "))
                if saldo >= valor_saq:
                    if valor_saq <= limite:
                        saldo -= valor_saq
                        self.set_saldo(saldo)
                        extrato.append(f"-R${valor_saq:.2f}")
                        self.set_extrato(extrato)
                        n_saque += 1
                        self.set_n_saque(n_saque)
                    else:
                        print("O valor de saque está acima do limite proposto!")
                else:
                    print("O valor de saque é maior que o valor do saldo!")
            except ValueError:
                print("Valor inválido!")
        else:
            print("Você atingiu seu limite de saques diários!")
    
    def visualizar_extrato(self):
        limpar()
        saldo = self.get_saldo()
        extrato = self.get_extrato()
        print("Histórico de movimentações: \n")
        for x in extrato:
            print(x)
        print(f"\n O saldo atual da conta é: R${saldo:.2f}")
    
    def mostrar_menu(self):
        menu = self.get_menu()
        print(menu)