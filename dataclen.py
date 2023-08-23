#	Comandos Python essenciais para as funções destacadas ao lado:
#		Quantificar Duplicatas
#		Quantificar Null
#		Quantificar valores muito fora da média
#		Fazer uma cópia de uma linha antes de dropa-la do DF
#		Remover Duplicatas
#		Remover espaços em branco em uma string
#		Join/Merge
#		Formatar o DataType
#		Extrair substrings
#		Contados dado uma condição específica
#		Ordenar os dados de um DF
#		Aplicar Filtros em um DF
#		Plotar Gráficos

##########################

#Quantificar Duplicatas

import pandas as pd

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'seu_arquivo.xlsx'
nome_planilha = 'Sheet3'  # Nome da planilha que você deseja ler

# Lê a planilha específica do arquivo Excel e cria um DataFrame
dataframe = pd.read_excel(nome_arquivo, sheet_name=nome_planilha)

# Conta a quantidade de linhas duplicadas no DataFrame
quantidade_duplicadas = dataframe.duplicated().sum()

# Exibe a quantidade de linhas duplicadas
print("Quantidade de linhas duplicadas:", quantidade_duplicadas)

##########################
Quantificar Null

import pandas as pd

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'seu_arquivo.xlsx'
nome_planilha = 'Sheet3'  # Nome da planilha que você deseja ler

# Lê a planilha específica do arquivo Excel e cria um DataFrame
dataframe = pd.read_excel(nome_arquivo, sheet_name=nome_planilha)

# Conta a quantidade de linhas com valores nulos no DataFrame
quantidade_nulos = dataframe.isnull().sum().sum()

# Exibe a quantidade de linhas com valores nulos
print("Quantidade de linhas com valores nulos:", quantidade_nulos)

##########################
Quantificar valores muito fora da média

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'seu_arquivo.xlsx'
nome_planilha = 'Sheet3'  # Nome da planilha que você deseja ler
nome_coluna = 'nome_da_coluna'  # Nome da coluna que você deseja analisar

# Lê a planilha específica do arquivo Excel e cria um DataFrame
dataframe = pd.read_excel(nome_arquivo, sheet_name=nome_planilha)

# Escolha um limite em termos de desvios padrão para considerar um valor discrepante
limite_desvios = 2  # Por exemplo, considerar valores além de 2 desvios padrão como discrepantes

# Calcula a média e o desvio padrão da coluna escolhida
media_coluna = dataframe[nome_coluna].mean()
desvio_padrao_coluna = dataframe[nome_coluna].std()

# Calcula os limites superior e inferior para valores discrepantes
limite_superior = media_coluna + limite_desvios * desvio_padrao_coluna
limite_inferior = media_coluna - limite_desvios * desvio_padrao_coluna

# Identifica linhas com valores discrepantes
linhas_discrepantes = dataframe[
    (dataframe[nome_coluna] > limite_superior) | (dataframe[nome_coluna] < limite_inferior)
]

# Obtém a contagem de linhas com valores discrepantes
quantidade_discrepantes = linhas_discrepantes.shape[0]

# Exibe a quantidade de linhas com valores discrepantes
print(f"Quantidade de linhas com valores discrepantes na coluna '{nome_coluna}': {quantidade_discrepantes}")

##########################
Fazer uma cópia de uma linha antes de dropa-la do DF

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'seu_arquivo.xlsx'
nome_planilha = 'Sheet3'  # Nome da planilha que você deseja ler
nome_coluna = 'nome_da_coluna'  # Nome da coluna para aplicar o critério

# Lê a planilha específica do arquivo Excel e cria um DataFrame
dataframe = pd.read_excel(nome_arquivo, sheet_name=nome_planilha)

# Cria um segundo DataFrame vazio para armazenar as linhas que serão excluídas
linhas_excluidas = pd.DataFrame(columns=dataframe.columns)

# Define o critério para dropar linhas (por exemplo, valores abaixo de 10 na coluna escolhida)
critério = 10

# Filtra as linhas que atendem ao critério e as move para o DataFrame de linhas excluídas
linhas_para_excluir = dataframe[dataframe[nome_coluna] < critério]
linhas_excluidas = linhas_excluidas.append(linhas_para_excluir)

# Remove as linhas do DataFrame original
dataframe = dataframe[dataframe[nome_coluna] >= critério]

# Exibe o DataFrame original após a exclusão
print("DataFrame Original após exclusão:")
print(dataframe)

# Exibe o DataFrame de linhas excluídas
print("DataFrame de Linhas Excluídas:")
print(linhas_excluidas)

##########################
Remover Duplicatas

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'seu_arquivo.xlsx'
nome_planilha = 'Sheet3'  # Nome da planilha que você deseja ler
nome_coluna = 'nome_da_coluna'  # Nome da coluna para remover duplicatas

# Lê a planilha específica do arquivo Excel e cria um DataFrame
dataframe = pd.read_excel(nome_arquivo, sheet_name=nome_planilha)

# Remove as linhas duplicadas com base na coluna específica
dataframe_sem_duplicatas = dataframe.drop_duplicates(subset=nome_coluna)

# Exibe o DataFrame após a remoção de duplicatas
print("DataFrame após remoção de duplicatas:")
print(dataframe_sem_duplicatas)

##########################
Remover espaços em branco em uma string



##########################
Join/Merge

# Substitua 'arquivo1.xlsx' e 'arquivo2.xlsx' pelos nomes dos seus arquivos Excel
arquivo1 = 'arquivo1.xlsx'
arquivo2 = 'arquivo2.xlsx'

# Carrega os DataFrames a partir dos arquivos Excel
dataframe1 = pd.read_excel(arquivo1)
dataframe2 = pd.read_excel(arquivo2)

# Define a coluna em que você deseja fazer o join
coluna_de_join = 'coluna_em_comum'

# Realiza o join entre os DataFrames baseado na coluna de join
dataframe_joined = dataframe1.merge(dataframe2, on=coluna_de_join, how='inner')

# Exibe o DataFrame resultante do join
print(dataframe_joined)

##########################
Formatar o DataType

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'seu_arquivo.xlsx'
nome_planilha = 'Sheet1'  # Nome da planilha que você deseja ler
nome_coluna = 'coluna_para_alterar'  # Nome da coluna para alterar o datatype

# Lê a planilha específica do arquivo Excel e cria um DataFrame
dataframe = pd.read_excel(nome_arquivo, sheet_name=nome_planilha)

# Altera o datatype da coluna para string
dataframe[nome_coluna] = dataframe[nome_coluna].astype(str)

# Exibe o DataFrame após a alteração de datatype
print(dataframe)

##########################
#Formatar um dos campos para DataType data/hora

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'seu_arquivo.xlsx'
nome_planilha = 'Sheet1'  # Nome da planilha que você deseja ler
nome_coluna = 'coluna_para_alterar'  # Nome da coluna para alterar o datatype

# Lê a planilha específica do arquivo Excel e cria um DataFrame
dataframe = pd.read_excel(nome_arquivo, sheet_name=nome_planilha)

# Altera o datatype da coluna para datetime
dataframe[nome_coluna] = pd.to_datetime(dataframe[nome_coluna])

# Exibe o DataFrame após a alteração de datatype
print(dataframe)

###########
#alt2

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'seu_arquivo.xlsx'
nome_planilha = 'Sheet1'  # Nome da planilha que você deseja ler
nome_coluna = 'coluna_para_alterar'  # Nome da coluna para alterar o datatype

# Lê a planilha específica do arquivo Excel e cria um DataFrame
dataframe = pd.read_excel(nome_arquivo, sheet_name=nome_planilha)

# Converte a coluna para datetime usando pd.to_datetime()
dataframe[nome_coluna] = pd.to_datetime(dataframe[nome_coluna])

# Exibe o DataFrame após a alteração de datatype
print(dataframe)

##########################
Extrair substrings

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'seu_arquivo.xlsx'
nome_planilha = 'Sheet1'  # Nome da planilha que você deseja ler
nome_coluna_original = 'coluna_original'  # Nome da coluna a ser quebrada
delimitador = '-'  # O delimitador usado para dividir a coluna original

# Lê a planilha específica do arquivo Excel e cria um DataFrame
dataframe = pd.read_excel(nome_arquivo, sheet_name=nome_planilha)

# Divide a coluna original em novas colunas usando o delimitador
nova_coluna_1, nova_coluna_2 = dataframe[nome_coluna_original].str.split(delimitador, 1).str

# Adiciona as novas colunas ao DataFrame
dataframe['nova_coluna_1'] = nova_coluna_1
dataframe['nova_coluna_2'] = nova_coluna_2

# Exibe o DataFrame com as novas colunas
print(dataframe)

##########################
Contados dado uma condição específica

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'seu_arquivo.xlsx'
nome_planilha = 'Sheet1'  # Nome da planilha que você deseja ler
nome_coluna = 'coluna_de_interesse'  # Nome da coluna para aplicar a condição
valor_condicao = 100  # Valor para a condição

# Lê a planilha específica do arquivo Excel e cria um DataFrame
dataframe = pd.read_excel(nome_arquivo, sheet_name=nome_planilha)

# Filtra as linhas que atendem à condição
linhas_atendendo_condicao = dataframe.loc[dataframe[nome_coluna] == valor_condicao]

# Obtém a contagem de linhas que atendem à condição
quantidade_linhas_atendendo_condicao = linhas_atendendo_condicao.shape[0]

# Exibe a quantidade de linhas que atendem à condição
print(f"Quantidade de linhas atendendo à condição: {quantidade_linhas_atendendo_condicao}")

##########################
Ordenar os dados de um DF

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'seu_arquivo.xlsx'
nome_planilha = 'Sheet1'  # Nome da planilha que você deseja ler
nome_coluna_para_ordenar = 'coluna_para_ordenar'  # Nome da coluna usada para ordenar

# Lê a planilha específica do arquivo Excel e cria um DataFrame
dataframe = pd.read_excel(nome_arquivo, sheet_name=nome_planilha)

# Ordena o DataFrame com base na coluna especificada
dataframe_ordenado = dataframe.sort_values(by=nome_coluna_para_ordenar)

# Exibe o DataFrame ordenado
print(dataframe_ordenado)

##########################
Aplicar Filtros em um DF

def aplicar_filtro(dataframe, coluna, valor):
    """
    Aplica um filtro a um DataFrame.
    
    Parâmetros:
    - dataframe: DataFrame a ser filtrado.
    - coluna: Nome da coluna para aplicar o filtro.
    - valor: Valor para filtrar na coluna.
    
    Retorna o DataFrame filtrado.
    """
    dataframe_filtrado = dataframe[dataframe[coluna] == valor]
    return dataframe_filtrado

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'seu_arquivo.xlsx'
nome_planilha = 'Sheet1'  # Nome da planilha que você deseja ler

# Lê a planilha específica do arquivo Excel e cria um DataFrame
dataframe = pd.read_excel(nome_arquivo, sheet_name=nome_planilha)

# Aplica um filtro ao DataFrame
coluna_filtro = 'coluna_de_interesse'
valor_filtro = 100
dataframe_filtrado = aplicar_filtro(dataframe, coluna_filtro, valor_filtro)

# Exibe o DataFrame após o filtro
print(dataframe_filtrado)

##########################
Plotar Gráficos

import pandas as pd
import matplotlib.pyplot as plt

# Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
nome_arquivo = 'seu_arquivo.xlsx'
nome_planilha = 'Sheet1'  # Nome da planilha que você deseja ler

# Lê a planilha específica do arquivo Excel e cria um DataFrame
dataframe = pd.read_excel(nome_arquivo, sheet_name=nome_planilha)

# Exemplo de gráfico de barras
def exemplo_grafico_de_barras():
    plt.figure(figsize=(10, 6))
    dataframe['coluna_de_interesse'].value_counts().plot(kind='bar')
    plt.title('Exemplo de Gráfico de Barras')
    plt.xlabel('Valores')
    plt.ylabel('Frequência')
    plt.show()

# Exemplo de gráfico de dispersão
def exemplo_grafico_de_dispersao():
    plt.figure(figsize=(10, 6))
    plt.scatter(dataframe['coluna_x'], dataframe['coluna_y'])
    plt.title('Exemplo de Gráfico de Dispersão')
    plt.xlabel('Coluna X')
    plt.ylabel('Coluna Y')
    plt.show()

# Exemplo de gráfico de linha
def exemplo_grafico_de_linha():
    plt.figure(figsize=(10, 6))
    dataframe.groupby('coluna_tempo')['coluna_valor'].sum().plot()
    plt.title('Exemplo de Gráfico de Linha')
    plt.xlabel('Tempo')
    plt.ylabel('Valor')
    plt.show()

# Chamada das funções de exemplo
exemplo_grafico_de_barras()
exemplo_grafico_de_dispersao()
exemplo_grafico_de_linha()

##########################

##########################