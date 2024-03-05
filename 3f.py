def proximo_valor_sequencia(sequencia):
    if len(sequencia) < 2:
        return "A sequência deve ter pelo menos dois valores."

    diferenca = sequencia[-1] - sequencia[-2]
    proximo_valor = sequencia[-1] + diferenca

    return proximo_valor

sequencia = [2, 10, 12, 16, 17, 18, 19]
proximo_valor = proximo_valor_sequencia(sequencia)

print(f"Sequência: {sequencia}")
print(f"Próximo valor: {proximo_valor}")
