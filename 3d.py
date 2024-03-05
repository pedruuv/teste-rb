def proximo_valor_sequencia_quadrados_perfeitos_pares(sequencia):
    if len(sequencia) < 1:
        return "A sequência deve ter pelo menos um valor."

    ultimo_numero = sequencia[-1]
    proximo_numero_par = (int(ultimo_numero ** 0.5) + 2)
    proximo_valor = proximo_numero_par ** 2

    return proximo_valor

sequencia = [4, 16, 36, 64]
proximo_valor = proximo_valor_sequencia_quadrados_perfeitos_pares(sequencia)

print(f"Sequência: {sequencia}")
print(f"Próximo valor: {proximo_valor}")
