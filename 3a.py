def proximo_valor_sequencia_aritmetica(sequencia):
    if len(sequencia) < 2:
        return "A sequência deve ter pelo menos dois valores para determinar a razão."
    
    razao = sequencia[1] - sequencia[0]
    proximo_valor = sequencia[-1] + razao
    
    return proximo_valor

sequencia = [1, 3, 5, 7]
proximo_valor = proximo_valor_sequencia_aritmetica(sequencia)

print(f"Sequência: {sequencia}")
print(f"Próximo valor: {proximo_valor}")