def somar(a, b):
    return a + b 

def subtrair(a, b):
    return a - b 

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "erro: divisao por zero"
        return a / b 

print("=== calculadora com funções ===")
    
n1 = float(input("digite o primeiro numero: "))
n2 = float(input("digite o segundo numero: "))
    
print(f"Soma: {somar(n1, n2)}")
print(f"Subtração: {subtrair(n1, n2)}")
print(f"Multiplicação: {multiplicar(n1, n2)}")
print(f"Divisão: {dividir(n1, n2)}")