# Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset (ajustar o caminho se necessário)
df = pd.read_csv('bcdata.sgs.29035.csv', sep=';', decimal=',')

# Converter a coluna de data para o formato datetime
df['data'] = pd.to_datetime(df['data'], dayfirst=True)

# Ordenar por data (precaução)
df = df.sort_values('data')

# Calcular a média móvel de 12 meses para suavizar a série
df['media_movel_12m'] = df['valor'].rolling(window=12).mean()

# Plotar gráfico com a série original e a média móvel
plt.figure(figsize=(14, 6))
plt.plot(df['data'], df['valor'], label='Comprometimento da Renda (%)', color='blue', linewidth=1)
plt.plot(df['data'], df['media_movel_12m'], label='Média Móvel (12 meses)', color='red', linewidth=2)
plt.title('Tendência do Comprometimento da Renda das Famílias Brasileiras com Dívidas')
plt.xlabel('Ano')
plt.ylabel('Percentual da Renda (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
