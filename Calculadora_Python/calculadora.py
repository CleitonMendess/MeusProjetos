def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

print("Calculadora simples em Python")
print("Operações disponíveis: +  -  *  /")

a = float(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
b = float(input("Digite o segundo número: "))

if operador == '+':
    resultado = somar(a, b)
elif operador == '-':
    resultado = subtrair(a, b)
elif operador == '*':
    resultado = multiplicar(a, b)
elif operador == '/':
    resultado = dividir(a, b)
else:
    resultado = "Operador inválido!"

print("Resultado:", resultado)
