#Funcao que apresenta e solicita escolha de funcao matematica a ser calculada
def opcoes():
    funcao = 0
    while funcao != 9:
        print("-----------Calculadora Científica------------")
        print("Qual função você deseja utilizar?")
        print("Opção 1: eˣ")
        print("Opção 2: ln x")
        print("Opção 3: log x")
        print("Opção 4: sen x")
        print("Opção 5: cos x")
        print("Opção 6: tg x")
        print("Opção 7: √x")
        print("Opção 8: π")
        print("Opção 9: sair")
        print("")
        funcao = int(input("Digite a opção: "))
        if funcao != 8 and funcao != 9:
            print("")
            x = float(input("Digite o x: "))
        match funcao:
            case 1:
                print(f"e^ ({x}) = {e_x(x)}")
            case 2:
                print(f"ln ({x}) = {ln_x(x)}")
            case 3:
                print(f"log ({x}) = {log_x(x)}")
            case 4:
                sen_x(x)
                print(f"sen ({x}) = {sen_x(x)}")
            case 5:
                print(f"cos ({x}) = {cos_x(x)}")
            case 6:
                print(f"tg ({x}) = {tg_x(x)}")
            case 7:
                print(f"raiz ({x}) = {raiz_x(x)}")
            case 8:
                pi()
                print(f"pi = {pi()}")
            case 9:
                exit()
    

def e_x(x, precisao=150):
    #Algoritmo que resolve a funcao e^x
    resultado = 0.0
    for n in range(precisao):
        resultado += x**n / factorial(n)
    return resultado

def ln_x(x, precisao = 100):
    #Algoritmo que resolve a funcao len x
    resultado = 0.0
    sinal = 1
    for n in range(1,precisao):
        resultado += sinal*(((x-1)**n)/n)
        sinal *= -1
    return resultado

def log_x(x, precisao=100):
    # Algoritmo que resolve a função log x
    resultado = 0.0
    resultado = ln_x(x)/ln_x(10)
    return resultado

def sen_x(x, precisao = 150):
    #Algoritmo que resolve a funcao sen x
    resultado = 0.0
    operador = 0
    for n in range(precisao):
        if n%2 != 0 and operador == 0:
            resultado += x**n / factorial(n)
            operador = 1
        elif n%2 != 0 and operador == 1:
            resultado = resultado - (x**n / factorial(n))
            operador = 0
        else:
            continue
    return resultado

def cos_x(x, precisao = 150):
    #Algoritmo que resolve a funcao cos x
    resultado = 0.0
    operador = 0
    for n in range(precisao):
        if n%2 == 0 and operador == 0:
            resultado += x**n / factorial(n)
            operador = 1
        elif n%2 == 0 and operador == 1:
            resultado = resultado - (x**n / factorial(n))
            operador = 0
        else:
            continue
    return resultado

def tg_x(x, precisao = 100):
    #Algoritmo que resolve a funcao tan x
    resultado = sen_x(x) / cos_x(x)
    return resultado

def raiz_x(x, terms=100):
    resultado = x / 2.0
    for n in range(terms):
        resultado = resultado - (resultado**2 - x) / (2 * resultado)
    return resultado

def pi(precisao = 1000):
    #Algoritmo que resolve a constante pi
    resultado = 0.0
    for n in range(precisao):
        resultado += ((-1)**n)/((2*n)+1)
    return resultado*4

def factorial(n):
    #Algoritmo que calcula o fatorial de um numero
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

opcoes()
