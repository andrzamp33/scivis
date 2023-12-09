import matplotlib.pyplot as plt

data = {
    'Tidal': 19448.16,
    'Hydro': 9863.33,
    'Wind': 5882.82,
    'Biofuel': 2636.03,
    'Solar PV': 841.87,
    'Geothermal': 114.04,
    'Renewable waste': 74.05,
    'Solar Thermal': 36.02
}

# Estrai i dati e le etichette
categories = list(data.keys())
values = list(data.values())

# Crea un grafico a barre orizzontali con colori personalizzati
colors = ['blue','yellow','green','mediumpurple','gray','indianred','orange']
plt.barh(categories, values, color=colors)
plt.xlabel('Contribution (TWh)')
plt.title('Energy Generation by Source')

# Rimuovi le griglie
plt.grid(False)

# Aggiungi un'ombreggiatura di sfondo per maggiore enfasi
plt.gca().set_facecolor('#f0f0f0')

# Aggiungi etichette per ciascuna barra
for index, value in enumerate(values):
    plt.text(value, index, f' {value} TWh', ha='left', va='center', fontsize=8, color='black')

# Nascondi assi
plt.xticks([])

# Mostra il grafico
plt.show()
