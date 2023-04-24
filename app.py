import scipy
import time
import math

# Sair do programa    
def sair():
    print("\nDesligando...")
    time.sleep(1)
# Menu do programa
def menu():
    while True:
        # Exibição do menu
        print("\n\n__________Integrais & Cia__________")
        print("---------------Menu---------------")
        print("Selecione uma opção:")
        print("1 - Integrar por Riemann")
        print("2 - Integrar por Newton-Cotes")
        print("3 - Sair\n")
    
        # Solicita a escolha do usuário
        escolha = input()
        
        # Caso a entrada seja válida, é executada a chamada do método correspondente ao comando dado.
        # Caso 1 - Determinar valor aproximado da integral fornecida, pelo método de Newton-Cotes
        if escolha == "1":
        elif escolha == "2":
        elif escolha == "3":
            sair()
            break
        else: # Verifica se a entrada é válida
            print("Opção inválida. Tente novamente.")

menu() # Execução do programa
