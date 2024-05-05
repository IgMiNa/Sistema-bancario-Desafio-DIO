from Sist_Bancario import SistemaBancario

def main():
    conta = SistemaBancario(0)
    while True:
        conta.mostrar_menu()
        resposta = int(input("Selecione uma das operações: "))
        match resposta:
            case 1:
                conta.depositar()
            case 2:
                conta.sacar()
            case 3:
                conta.visualizar_extrato()
            case 4:
                break
            case _:
                print("Operação inválida!")

if __name__ == "__main__":
    main()