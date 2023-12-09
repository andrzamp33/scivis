import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Coal': 9863.33,
    'Natural Gas': 5882.82,
    'Nuclear': 2636.03,
    'Oil': 841.87,
    'Waste': 114.04,
    'Municipal Wastes': 74.05,
    'Others': 36.02
}

# Estrai i dati e le etichette
categories = list(data.keys())
values = list(data.values())

# Crea un grafico a barre orizzontali con colori personalizzati
colors = ['#9ec8e9', '#ffdbbf', '#c1e6bf', '#d8b3e6', '#f5ebbf', '#d89797', '#a4b3d9']

# Usa figure e axes per maggior controllo
fig, ax = plt.subplots()

ax.barh(categories, values, color=colors)
ax.set_xlabel('Contribution (TWh)')
ax.set_title('Energy Generation by Source')

# Rimuovi le griglie
ax.grid(False)

# Aggiungi etichette per ciascuna barra
for index, value in enumerate(values):
    ax.text(value, index, f' {value} TWh', ha='left', va='center', fontsize=8, color='black')

# Nascondi assi
ax.set_xticks([])

# Rimuovi i bordi
sns.despine()

# Rimuovi i bordi dalla figura e dagli assi
ax.set_frame_on(False)
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# Mostra il grafico
plt.show()
