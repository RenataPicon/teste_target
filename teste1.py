def isFibonacci(n):
    if n < 0:
        return False

    def isPerfectSquare(x):
        s = int(x ** 0.5)
        return s * s == x

    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)

try:
    number = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    if isFibonacci(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
