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
    
# Integração pelo método de Newton-Cotes    
def integrarNewtonCotes():
    
    expressao_input = input("Insira a funcao a ser integrada: ")
    
    expressao_avaliada = lambda x: eval(expressao_input)
    
    num_trapezios = int(input("\nForneca o numero de trapezios a ser utilizado: "))
    
    casas_decimais = int(input("Arredondamento de casas decimais: "))
    
    # Obtenção do intervalo
    intervalo = requerirIntervalo() # [a, b]
    a = intervalo[0] # Valor inicial do intervalo --> a
    b = intervalo[1] # Valor final do intervalo --> b
    
    # Cálculo da altura dos trapezios (também conhecida como amplitude dos intervalos)
    amplitude = round(((b - a) / num_trapezios), 1)
    
    # O número de casas do arredondamento padrão é corrigido com base no input de casas decimais
    erroArredodamentoPadrao = 0.5

    # Ajuste do valor do arredondamento padrão, com base no numero de casas decimais fornecidas
    erroArredodamentoPadrao = ((erroArredodamentoPadrao / 10.0**casas_decimais) * amplitude) * num_trapezios
 
    # Calculo da área pelo método da somatória de trapézios, com base na função lambda, n° de trapézios,
    # n° de casas decimais (input), amplitude dos trapézios, e valor do intervalo inicial
    resultado = calcArea(expressao_avaliada, num_trapezios, casas_decimais, amplitude, a)
 
    # Print do resultado
    print('\nSoma das areas:', round(resultado, casas_decimais))
    print("Erro de arredondamento:", f"{erroArredodamentoPadrao:.{casas_decimais + 1}f}")
    input("\nPressione qualquer tecla para continuar...\n")

# Computação da integral pela somatória sucessiva dos trapézios, fazendo uso da função lambda
def calcArea(f, trapezios, casas_decimais, amplitude, a):
    
    # Variável local auxiliar da computação da somatória     
    somatoria = 0
    
    print("Tabela:") # Formatação da tabela
    print("   x        f(x)")
    print("------------------")
    
    for i in range(trapezios + 1): # A variável de controle "i" começa em 0
        
        # Variável auxiliar que guarda o valor inicial de X da iteração (inicia-se pelo intervalo inicial, visto A)
        auxA = a 
        
        # Computa a expressão inserida, dado X da iteração e a imprime na tela
        print("-", a, " -> ", calcFuncao(f, a, casas_decimais))
        
        # Incrementa o X da iteração pela amplitude dos trapézios, arrendodado a N casas decimais
        a = round(a + amplitude, casas_decimais)
        
        # Variável auxiliar que guarda o valor do próximo X (incrementado da amplitude)
        # da iteração, para que seja possível realizar o cálculo da área
        next_auxA = calcFuncao(f, a, casas_decimais)
        
        # Enquanto o número da variável de controle do loop for diferente da
        # quantidade de trapézios inserida, é realizada o cálculo da área do trapézio,
        # e é adicionada na somatória das áreas dos trapézios do problema
        if(i != trapezios):
            somatoria = round((somatoria + (((calcFuncao(f, auxA, casas_decimais) + next_auxA)/2)*amplitude)), casas_decimais)

    return somatoria
    
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
    
# Cálculo da função de entrada, dado X, com resultado arredondado a N casas decimais
def calcFuncao(f, x, N):
    
    return round(f(x), N)

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
        # Caso a entrada seja válida, é executada a chamada do método correspondente ao comando dado
        escolha = input()
        
        # Caso 1 - Determinar valor aproximado da integral fornecida, pelo método de Riemann
        if escolha == "1":
            integrarRiemann()
        elif escolha == "2": # Caso 2 - Determinar valor aproximado da integral fornecida, pelo método de Newton-Cotes
            integrarNewtonCotes()
        elif escolha == "3":
            sair()
            break
        else: # Validação de entrada
            print("Opção inválida. Tente novamente.")

menu() # Execução do algoritmo
