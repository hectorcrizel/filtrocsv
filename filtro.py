import pandas as pd
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pyperclip  # Importar o módulo para copiar para a área de transferência

Tk().withdraw()

csv_file = askopenfilename(title="Selecione o arquivo CSV", filetypes=[("CSV files", "*.csv")])
if not csv_file:
    print("Nenhum arquivo selecionado.")
    exit()

try:
    df = pd.read_csv(csv_file, encoding='latin1', sep=';', on_bad_lines='skip')  # Ajuste o delimitador se necessário
except Exception as e:
    print(f"Erro ao ler o arquivo CSV: {e}")
    exit()


colunas = ['Atendimento', 'Atraso no serviço', 'Situação', 'Prioridade', 'Previsão de encerramento', 'Equipe', 'Responsável']
df = df[colunas]


print("Valores únicos na coluna 'Situação':", df['Situação'].unique())


hora_atual = datetime.now().hour
saudacao = "Boa tarde." if hora_atual >= 12 else "Bom dia."


data_hora_atual = datetime.now().strftime("%H-%M %d_%m_%Y")
nome_arquivo = f'repasse {data_hora_atual}.txt'


with open(nome_arquivo, 'w', encoding='utf-8') as f:
    f.write(f"{saudacao}\n\n")
    f.write("Segue repasse de chamados:\n\n")

    # Filtrar e escrever os dados por status
    for status in ['AGUARDANDO ATENDIMENTO', 'EM ATENDIMENTO', 'SUSPENSO']:
        f.write(f"*{status}*\n\n")
        filtered_df = df[df['Situação'].str.strip().str.upper() == status]
        if not filtered_df.empty:
            f.write("\t".join(colunas) + "\n")  # Cabeçalho
            for index, row in filtered_df.iterrows():
                f.write("\t".join(row.astype(str)) + "\n")
        else:
            f.write("Nenhum registro encontrado.\n")
        f.write("\n")


with open(nome_arquivo, 'r', encoding='utf-8') as f:
    conteudo = f.read()


conteudo = conteudo.replace('nan', '').replace('NAN', '')

o
with open(nome_arquivo, 'w', encoding='utf-8') as f:
    f.write(conteudo)


pyperclip.copy(conteudo)

print(f"Arquivo gerado: {nome_arquivo}")
print("Conteúdo copiado para a área de transferência.")
