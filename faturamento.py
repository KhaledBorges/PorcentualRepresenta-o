valor_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(valor_estados.values())

print("Percentual de representação de cada estado:")
for estado, faturamento in valor_estados.items():
    percentual = (faturamento / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")
# O loop for declara "estado" e "faturamento", chave e valor do objeto "valor_estados"
