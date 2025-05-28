import pandas as pd
import matplotlib.pyplot as plt

# Configurar para exibir acentuação corretamente
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'DejaVu Sans'

# Caminhos dos arquivos CSV
paths = {
    "22701": "bcdata.sgs.22701.csv",  # Percentual de famílias endividadas
    "22702": "bcdata.sgs.22702.csv",  # Percentual com dívidas em atraso
    "22703": "bcdata.sgs.22703.csv",  # Percentual sem condições de pagar
}

# Função para carregar e processar os dados
def carregar_processar_dataset(path, corrigir_negativos=False):
    df = pd.read_csv(path, sep=';', decimal=',')
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df = df.sort_values('data')
    if corrigir_negativos:
        df = df[df['valor'] >= 0]
    df['media_movel_12m'] = df['valor'].rolling(window=12).mean()
    return df

# Carregar e processar os datasets
df_22701 = carregar_processar_dataset(paths["22701"], corrigir_negativos=True)
df_22702 = carregar_processar_dataset(paths["22702"])
df_22703 = carregar_processar_dataset(paths["22703"])

# Plotar os três gráficos
plt.figure(figsize=(18, 15))

# 1. Percentual de famílias endividadas
plt.subplot(3, 1, 1)
plt.plot(df_22701['data'], df_22701['valor'], label='Famílias Endividadas (%)', color='blue')
plt.plot(df_22701['data'], df_22701['media_movel_12m'], label='Média Móvel (12 meses)', color='red', linewidth=2)
plt.title('Tendência - Famílias Endividadas (%)')
plt.xlabel('Ano')
plt.ylabel('Percentual (%)')
plt.legend()
plt.grid(True)

# 2. Dívidas em atraso
plt.subplot(3, 1, 2)
plt.plot(df_22702['data'], df_22702['valor'], label='Dívidas em Atraso (%)', color='green')
plt.plot(df_22702['data'], df_22702['media_movel_12m'], label='Média Móvel (12 meses)', color='red', linewidth=2)
plt.title('Tendência - Famílias com Dívidas em Atraso (%)')
plt.xlabel('Ano')
plt.ylabel('Percentual (%)')
plt.legend()
plt.grid(True)

# 3. Sem condições de pagar dívidas
plt.subplot(3, 1, 3)
plt.plot(df_22703['data'], df_22703['valor'], label='Sem Condições de Pagar (%)', color='purple')
plt.plot(df_22703['data'], df_22703['media_movel_12m'], label='Média Móvel (12 meses)', color='red', linewidth=2)
plt.title('Tendência - Famílias sem Condições de Pagar Dívidas (%)')
plt.xlabel('Ano')
plt.ylabel('Percentual (%)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
