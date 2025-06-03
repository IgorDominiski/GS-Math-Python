import numpy as np
import matplotlib.pyplot as plt

# 1. Dados simulados: dias e níveis do rio Tietê (m)
dias = np.arange(1, 11)
niveis = np.array([0.5, 0.8, 1.2, 1.5, 2.0, 2.3, 2.5, 2.6, 2.4, 2.1])

# 2. Definir domínio e imagem
dominio = (dias.min(), dias.max())
imagem = (niveis.min(), niveis.max())

print(f"Domínio (dias): {dominio}")
print(f"Imagem (níveis do rio em metros): {imagem}")

# 3. Ponto máximo
indice_max = np.argmax(niveis)
dia_max = dias[indice_max]
nivel_max = niveis[indice_max]

print(f"Ponto máximo: dia {dia_max} com nível {nivel_max} m")

# 4. Identificar dias de risco (> 2 metros)
limite_risco = 2.0
dias_risco = dias[niveis > limite_risco]
niveis_risco = niveis[niveis > limite_risco]
print(f"Dias de risco (nível > {limite_risco} m): {list(dias_risco)}")

# 5. Ajuste polinomial cúbico
coef = np.polyfit(dias, niveis, 3)  # coeficientes do polinômio cúbico
polinomio = np.poly1d(coef)

# Valores do polinômio para um domínio mais denso para o gráfico
dias_finos = np.linspace(dominio[0], dominio[1], 100)
niveis_polinomio = polinomio(dias_finos)

# 6. Plotar gráfico
plt.figure(figsize=(10,6))
plt.plot(dias, niveis, 'bo', label='Nível Real')
plt.plot(dias_finos, niveis_polinomio, 'g-', label='Ajuste Polinomial Cúbico')
plt.plot(dias_risco, niveis_risco, 'ro', markersize=10, label='Risco de Enchente (>2m)')
plt.axhline(y=limite_risco, color='r', linestyle='--', label='Limite de Risco (2m)')

# Destacar ponto máximo
plt.plot(dia_max, nivel_max, 'ks', markersize=12, label='Ponto Máximo')

plt.title('Monitoramento do Nível do Rio Tietê - 10 Dias')
plt.xlabel('Dia')
plt.ylabel('Nível do Rio (m)')
plt.xticks(dias)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
