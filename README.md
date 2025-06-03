📊 Monitoramento do Nível do Rio Tietê — Modelagem Polinomial e Alerta de Enchentes

🔍 Descrição do Projeto

Este projeto foi desenvolvido para simular o monitoramento do nível do Rio Tietê durante 10 dias consecutivos de chuva intensa, com o objetivo de prever situações de risco de enchente.

Utilizamos modelagem polinomial para aproximar os dados e gerar uma função matemática que representa o comportamento do rio ao longo dos dias. A visualização dos dados permite destacar níveis críticos, auxiliando no planejamento de evacuação e emissão de alertas.

📈 Explicação Matemática

🔹 1. Modelagem Polinomial
Utilizamos um polinômio de grau 3 (forma cúbica) para ajustar os dados de nível do rio:

f
(
x
)
=
a
x
3
+
b
x
2
+
c
x
+
d
f(x)=ax 
3
 +bx 
2
 +cx+d
Esse tipo de polinômio é ideal para comportamentos que crescem, se estabilizam ou diminuem ao longo do tempo — como é o caso do nível de um rio durante uma sequência de dias chuvosos.

Os coeficientes 
a
,
b
,
c
,
d
a,b,c,d são calculados automaticamente com a função polyfit da biblioteca NumPy, com base nos 10 pontos de dados simulados.

🔹 2. Domínio e Imagem da Função
Domínio: Dias analisados → 
x
∈
[
1
,
10
]
x∈[1,10]
Imagem: Intervalo dos níveis do rio durante o período → 
y
∈
[
0.5
,
2.6
]
 
(em metros)
y∈[0.5,2.6](em metros)
🔹 3. Ponto Máximo
O ponto máximo da função é o dia em que o nível do rio atinge o valor mais alto (neste caso, 2.6 metros). Esse ponto é identificado automaticamente pelo código com:

np.argmax(niveis)
🔹 4. Critério de Risco de Enchente
Consideramos que há risco de enchente sempre que o nível do rio ultrapassa 2 metros. O código marca esses pontos em vermelho no gráfico e imprime os dias de risco.

🧪 Dados Utilizados

Os dados foram simulados com base em estudos reais sobre o comportamento do Rio Tietê em épocas de chuva intensa. Cada valor representa o nível do rio em metros ao final de cada um dos 10 dias consecutivos:

Dia	Nível do Rio (m)
1	0.5
2	0.8
3	1.2
4	1.5
5	2.0
6	2.3
7	2.5
8	2.6
9	2.4
10	2.1
▶️ Como Executar

📋 Requisitos
Python 3.x
Bibliotecas: matplotlib e numpy
🛠️ Instalar as bibliotecas
pip install matplotlib numpy
🏃 Rodar o código
Copie o código Python para um arquivo chamado monitoramento_tiete.py
No terminal, vá até a pasta onde o arquivo está salvo:
cd caminho/da/sua/pasta
Execute:
python monitoramento_tiete.py
👥 Autores

Nome do Autor 1 — RA/ID
Nome do Autor 2 — RA/ID
Nome do Autor 3 — RA/ID
🎥 Vídeo Demonstrativo

➡️ Clique aqui para assistir ao vídeo

✅ Conclusão

A modelagem polinomial é uma ferramenta poderosa para antecipar comportamentos naturais com base em dados. Neste projeto, ela auxilia na previsão de enchentes a partir do comportamento do rio, permitindo a emissão de alertas antecipados e o planejamento de ações preventivas em áreas de risco.
