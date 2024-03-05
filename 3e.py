def proximo_valor_sequencia_fibonacci(sequencia):
    if len(sequencia) < 2:
        return "A sequência deve ter pelo menos dois valores."

    penultimo_numero = sequencia[-2]
    ultimo_numero = sequencia[-1]
    proximo_valor = penultimo_numero + ultimo_numero

    return proximo_valor

sequencia = [1, 1, 2, 3, 5, 8]
proximo_valor = proximo_valor_sequencia_fibonacci(sequencia)

print(f"Sequência: {sequencia}")
print(f"Próximo valor: {proximo_valor}")
