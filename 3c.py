def proximo_valor_sequencia_quadrados_perfeitos(sequencia):
    if len(sequencia) < 1:
        return "A sequência deve ter pelo menos um valor."
    
    proximo_valor = (len(sequencia))**2
    
    return proximo_valor

sequencia = [0, 1, 4, 9, 16, 25, 36]
proximo_valor = proximo_valor_sequencia_quadrados_perfeitos(sequencia)

print(f"Sequência: {sequencia}")
print(f"Próximo valor: {proximo_valor}")
