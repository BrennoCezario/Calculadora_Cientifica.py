#Funcao que apresenta e solicita escolha de funcao matematica a ser calculada
def opcoes():
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
    print("")
    funcao = int(input("Digite a opção: "))
    if funcao != 8:
        print("")
        x = float(input("Digite o x: "))
    match funcao:
        case 1:
            print(f"e^{x} = {e_x(x)}")
        case 2:
            ln_x(x)
            print(f"ln{x} = {ln_x(x)}")
        case 3:
            log_x(x)
        case 4:
            sen_x(x)
            print(f"sen({x}) = {sen_x(x)}")
        case 5:
            cos_x(x)
        case 6:
            tg_x(x)
        case 7:
            raiz_x(x)
        case 8:
            pi()
            print(f"pi = {pi()}")

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

def log_x(x, precisao = 100):
    #Algoritmo que resolve a funcao log x
    return 1

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
    return 1

def raiz_x(x, precisao = 100):
    #Algoritmo que resolve a funcao raiz
    return 1

def pi(precisao = 1000):
    #Algoritmo que resolve a constante pi
    resultado = 0.0
    for n in range(precisao):
        resultado += ((-1)**n)/((2*n)+1)
    return resultado*4

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

opcoes()
