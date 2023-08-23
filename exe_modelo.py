###############
#Exemplo de modelo simples

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

# Gerando dados de exemplo
np.random.seed(0)
n_samples = 100
faltas = np.random.randint(0, 10, n_samples)
qualidade_entregas = np.random.uniform(0, 10, n_samples)
agilidade_entregas = np.random.uniform(0, 10, n_samples)
score = 40 + 3*faltas - 2*qualidade_entregas + 4*agilidade_entregas + np.random.normal(0, 5, n_samples)

# Normalizando os dados
scaler = MinMaxScaler()
X = np.column_stack((faltas, qualidade_entregas, agilidade_entregas))
X = scaler.fit_transform(X)
y = scaler.fit_transform(score.reshape(-1, 1))

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Treinando o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Desnormalizando as previsões
y_pred = scaler.inverse_transform(y_pred)

# Avaliando o desempenho do modelo
score_train = model.score(X_train, y_train)
score_test = model.score(X_test, y_test)

print("Score R2 (treino):", score_train)
print("Score R2 (teste):", score_test)

##########################

peso_agilidade = 0.5
peso_qualidade = 0.3
peso_faltas = 0.2

# Multiplicando as variáveis pelos pesos
score = peso_faltas * faltas + peso_qualidade * qualidade_entregas + peso_agilidade * agilidade_entregas

###########################

# Definindo os pesos para cada variável
peso_agilidade = 0.5
peso_qualidade = 0.3
peso_faltas = 0.2

# Calculando o score ponderado para cada funcionário
scores_ponderados = peso_faltas * faltas + peso_qualidade * qualidade_entregas + peso_agilidade * agilidade_entregas

# Normalizando os scores ponderados entre 0 e 100
normalized_scores = (scores_ponderados - np.min(scores_ponderados)) / (np.max(scores_ponderados) - np.min(scores_ponderados)) * 100

#############################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

# Suponha que 'data' seja o seu DataFrame com as informações dos funcionários
data = pd.DataFrame()
data['funcionario'] = [1,2,3,4,5,6,7,8,9,10]
data['faltas'] = [0,0,1,2,3,0,0,4,0,1]
data['qualidade_entregas'] = [10,9,9,8,8,10,7,5,8,8]
data['agilidade_entregas'] = [10,5,1,5,5,6,7,8,9,9]
data['lucro'] = [100000,90000,12000,50000,60000,60000,50000,40000,80000,50000]
display(data)

# Definindo as variáveis de entrada e o alvo (lucro)
X = data[['faltas', 'qualidade_entregas', 'agilidade_entregas']]
y = data['lucro']

# Normalizando os dados de entrada
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Dividindo os dados em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=0)

# Treinando o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Avaliando o desempenho do modelo
score_train = model.score(X_train, y_train)
score_test = model.score(X_test, y_test)

print("Score R2 (treino):", score_train)
print("Score R2 (teste):", score_test)

###############################

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

# Suponha que 'data' seja o seu DataFrame com as informações dos funcionários
# Suponha que 'data' seja o seu DataFrame com as informações dos funcionários
data = pd.DataFrame()
data['funcionario'] = [1,2,3,4,5,6,7,8,9,10]
data['faltas'] = [0,0,1,2,3,0,0,4,0,1]
data['qualidade_entregas'] = [10,9,9,8,8,10,7,5,8,8]
data['agilidade_entregas'] = [10,5,1,5,5,6,7,8,9,9]

#data['agilidade_entregas'] = [10,9,2,5,6,6,5,4,8,5] Testando algumas possibilidades absurdas
#Bacana! Funciona!

data['lucro'] = [100000,90000,12000,50000,60000,60000,50000,40000,80000,50000]
display(data)

# Definindo as variáveis de entrada e o alvo (lucro)
X = data[['faltas', 'qualidade_entregas', 'agilidade_entregas']]
y = data['lucro']

# Normalizando os dados de entrada
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Treinando o modelo de regressão linear ponderada
model = LinearRegression()
model.fit(X_scaled, y)

# Obtendo os coeficientes do modelo (pesos das variáveis)
peso_faltas, peso_qualidade, peso_agilidade = model.coef_

# Normalizando os pesos para que a soma seja 1
soma_pesos = peso_faltas + peso_qualidade + peso_agilidade
peso_faltas /= soma_pesos
peso_qualidade /= soma_pesos
peso_agilidade /= soma_pesos

print("Peso de faltas:", peso_faltas)
print("Peso de qualidade das entregas:", peso_qualidade)
print("Peso de agilidade das entregas:", peso_agilidade)