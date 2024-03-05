def calcular_fibonacci(n):
    fib_seq = [0,1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        
    return fib_seq

def verifica_pertencimento(numero, sequencia):
    return numero in sequencia

numero = 2
sequencia_fibonacci = calcular_fibonacci(numero)
pertence = verifica_pertencimento(numero, sequencia_fibonacci)

if pertence:
    print(f"O número {numero} pertence à sequência de fibonacci")
else:
    print(f"O número {numero} não pertence à sequência de fibonacci")