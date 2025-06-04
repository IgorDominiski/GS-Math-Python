# Análise de Níveis do Rio Tietê

Este projeto realiza uma análise matemática dos níveis do Rio Tietê, utilizando dados simulados para demonstrar conceitos de análise de funções e visualização de dados.

## 📊 Sobre o Projeto

O código implementa uma análise matemática dos níveis do Rio Tietê ao longo de 10 dias, incluindo:
- Visualização dos dados em gráfico
- Identificação de pontos críticos
- Análise de dias com risco de enchente
- Ajuste polinomial cúbico para modelagem dos dados

## 📚 Conceitos Matemáticos Utilizados

- Funções polinomiais
- Análise de domínio e imagem
- Máximos e mínimos
- Ajuste de curvas
- Visualização de dados


## 📈 Dados Utilizados

Os dados utilizados neste projeto são simulados para fins educacionais. Os níveis do rio são representados em metros, com um período de monitoramento de 10 dias. Os dados incluem:
- Níveis variando de 0.5m a 2.6m
- Identificação de dias com risco de enchente (níveis acima de 2.0m)
- Ponto máximo de enchente no dia 8, com 2.6m

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x
- Bibliotecas necessárias:
  - numpy
  - matplotlib

### Instalação

1. Clone este repositório:
```bash
git clone [GS-Math-Python]
```

2. Instale as dependências:
```bash
pip install numpy matplotlib
```

3. Execute o script:
```bash
python enchente.py
```

## 👥 Autores

Igor Dominiski, Murilo Reis, Murillo Akira

## 🎥 Demonstração

https://youtu.be/xA7GLfTQbHs

## 📝 Notas Técnicas

O código implementa:
1. Análise do domínio e imagem da função
2. Identificação do ponto máximo
3. Detecção de dias com risco de enchente
4. Ajuste polinomial cúbico para modelagem dos dados
5. Visualização gráfica com:
   - Dados reais
   - Curva de ajuste polinomial
   - Pontos de risco
   - Linha de limite de risco
   - Ponto máximo destacado
  
## 📊 Memorial Descritivo e Análise Matemática

### Modelo Matemático Utilizado

O projeto utiliza um modelo polinomial cúbico (grau 3) para modelar o comportamento dos níveis do Rio Tietê. Este modelo foi escolhido por sua capacidade de capturar tanto tendências quanto variações locais nos dados.

#### Equação do Modelo
O ajuste polinomial cúbico é representado pela equação:
```
f(x) = ax³ + bx² + cx + d
```
onde:
- x representa o dia de monitoramento
- f(x) representa o nível do rio em metros
- a, b, c, d são os coeficientes determinados pelo método dos mínimos quadrados

### Análise dos Dados

| Dia (x) | Nível do Rio (m) (y) |           |
| ------- | -------------------- | --------- |
| 1       | 0.8                  |           |
| 2       | 1.2                  |           |
| 3       | 1.7                  |           |
| 4       | 2.3                  |           |
| 5       | 2.8                  |           |
| 6       | 3.0                  | ⚠️ Máximo |
| 7       | 2.9                  |           |
| 8       | 2.5                  |           |
| 9       | 2.0                  |           |
| 10      | 1.5                  |           |

```
y=−0,07x 
2
 +0,8x+0,2
```


#### Interpretação dos Resultados

1. **Domínio e Imagem**
   - Domínio: [1, 10] dias
   - Imagem: [0.5, 2.6] metros
   - Esta análise permite identificar o período de monitoramento e a faixa de variação dos níveis

2. **Pontos Críticos**
   - Ponto máximo: Dia 8 com 2.6m
   - Dias com risco de enchente: 5 dias consecutivos (dias 5-10)
   - Limite de risco: 2.0m

3. **Tendências Identificadas**
   - Crescimento inicial: dias 1-4 (0.5m → 1.5m)
   - Período crítico: dias 5-8 (2.0m → 2.6m)
   - Tendência de queda: dias 8-10 (2.6m → 2.1m)

### Aplicação no Sistema de Alerta de Enchentes

O modelo matemático desenvolvido pode ser utilizado como ferramenta de previsão e alerta de enchentes através de:

1. **Previsão de Tendências**
   - O ajuste polinomial permite extrapolar tendências futuras
   - Identificação precoce de períodos de risco
   - Estimativa do tempo até atingir níveis críticos

2. **Classificação de Risco**
   - Nível Normal: < 2.0m
   - Nível de Risco: ≥ 2.0m
   - Ponto Crítico: ≥ 2.5m

3. **Benefícios do Sistema**
   - Monitoramento contínuo dos níveis
   - Alertas antecipados para autoridades
   - Base para decisões de evacuação
   - Planejamento de ações preventivas

4. **Limitações e Considerações**
   - Dados simulados para fins educacionais
   - Necessidade de calibração com dados reais
   - Consideração de fatores externos (chuva, maré, etc.)
   - Atualização constante do modelo

### Recomendações para Implementação Real

Para uma implementação real do sistema, recomenda-se:
1. Coleta de dados históricos reais
2. Calibração do modelo com dados locais
3. Integração com estações meteorológicas
4. Desenvolvimento de interface para monitoramento em tempo real
5. Estabelecimento de protocolos de alerta


