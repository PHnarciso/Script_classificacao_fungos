import pandas as pd

# Leitura do arquivo CSV de entrada
input_file = "tabela_completa.csv"
df = pd.read_csv(input_file)

# Lista de colunas de características (ajuste conforme necessário)
caracteristicas = df.columns[1:4]

# Cria um dicionário para armazenar os grupos de fungos idênticos
grupos = {}

# Itera pelas linhas do DataFrame
for index, row in df.iterrows():
    # Converte a linha em uma tupla para que possa ser usada como chave no dicionário
    tupla_caracteristicas = tuple(row[caracteristicas])

    # Verifica se a tupla de características já existe no dicionário
    if tupla_caracteristicas in grupos:
        grupos[tupla_caracteristicas].append(row['ID'])
    else:
        grupos[tupla_caracteristicas] = [row['ID']]

# Cria um DataFrame para o arquivo de saída
saida = pd.DataFrame(columns=['Grupo', 'Ids'])

# Preenche o DataFrame de saída com os grupos e IDs
for grupo, ids in grupos.items():
    saida = saida.append({'Grupo': grupo, 'Ids': ', '.join(map(str, ids))}, ignore_index=True)

# Escreve o DataFrame de saída em um arquivo CSV
output_file = "fungos_identicos.csv"
saida.to_csv(output_file, index=False)


