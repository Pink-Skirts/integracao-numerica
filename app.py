import scipy
import time
import math

# Exs. de uso de operadores especiais p/ funções:
# Seno(x) = math.sin(x)
# log(x) na base 10 = math.log(x, 10)
# ln(x) = math.log(x, math.e) 

# Integração padrão pelo método da Soma de Riemann
def integrarRiemann():
    
    expressao_input = input("Insira a funcao a ser integrada: ")
    
    # Mapeamento de X na expressão input, resultando na expressão lambda
    expressao_avaliada = lambda x: eval(expressao_input)
    
    casas_decimais = int(input("Arredondamento de casas decimais: "))
    
    # Obtenção do intervalo
    intervalo = requerirIntervalo()
    a = intervalo[0] # Valor inicial do intervalo --> a
    b = intervalo[1] # Valor final do intervalo --> b
    
    # Computação da integral da expressão fornecida como entrada
    resultado = scipy.integrate.quad(expressao_avaliada, a, b)
    
    # Print do resultado
    print('\nRESULTADO: ', round(resultado[0], casas_decimais))
    input("\nPressione qualquer tecla para continuar...\n")
    
    
# Requisição dos valores do intervalo da integral    
def requerirIntervalo(): 
    
    a = float(input("\nIntervalo\nInsira o valor do ponto INICIAL: "))
    b = float(input("Insira o valor do ponto FINAL: "))
    print("\n")
    
    return [a, b]

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
            integrarRiemann()
        elif escolha == "3":
            sair()
            break
        else: # Verifica se a entrada é válida
            print("Opção inválida. Tente novamente.")

menu() # Execução do algoritmo
