
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Codice grafico 1
data_1 = {
    'Tidal': 19448.16,
    'Hydro': 9863.33,
    'Wind': 5882.82,
    'Biofuel': 2636.03,
    'Solar PV': 841.87,
    'Geothermal': 114.04,
    'Renewable waste': 74.05,
    'Solar Thermal': 36.02
}

categories_1 = list(data_1.keys())
values_1 = list(data_1.values())

# Inverto l'ordine delle categorie e dei valori
categories_1 = categories_1[::-1]
values_1 = values_1[::-1]

colors_1 = ["#ff9999", "#ffb3e6", "#f8c471", "#ffeaa7", "#c9e2b3", "#ffcccc", "#aec6cf", "#b3b3cc"]

# Codice grafico 2
category_names_2 = ["Hydro", "Biofuel", "Solar", "Geothermal"]

results_2 = {}

data_2 = pd.read_csv("datasets/top20CountriesPowerGeneration.csv", usecols=["Country", "Hydro(TWh)", "Biofuel(TWh)", "Solar PV (TWh)", "Geothermal (TWh)"])

for indice, riga in data_2.iterrows():
    results_2.update({riga["Country"]: []})
    results_2[riga["Country"]].append(riga["Hydro(TWh)"])
    results_2[riga["Country"]].append(riga["Biofuel(TWh)"])
    results_2[riga["Country"]].append(riga["Solar PV (TWh)"])
    results_2[riga["Country"]].append(riga["Geothermal (TWh)"])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# Grafico 1
ax1.barh(categories_1, values_1, color=colors_1)
ax1.set_xlabel('Contribution (TWh)')
ax1.set_title('Energy generation by source (1997-2017)')
ax1.grid(False)
for index, value in enumerate(values_1):
    ax1.text(value, index, f' {value}', ha='left', va='center', fontsize=8, color='black')
ax1.set_xticks([])
ax1.tick_params(axis='y', which='both', left=False)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)

# Grafico 2
labels = list(results_2.keys())
data = np.array(list(results_2.values()))
data_cum = data.cumsum(axis=1)
category_colors_2 = ["#aec6cf", "#c9e2b3", "#ffeaa7", "#f8c471"]

for i, (colname, color) in enumerate(zip(category_names_2, category_colors_2)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    rects = ax2.barh(labels, widths, left=starts, height=0.8, label=colname, color=color, edgecolor="none")

ax2.legend(ncols=len(category_names_2), bbox_to_anchor=(1, 0), loc='lower right', fontsize='small')
ax2.invert_yaxis()
ax2.xaxis.set_visible(False)
ax2.set_xlim(0, np.sum(data, axis=1).max())
ax2.set_title('Energy generation by major countries (1997-2017)')

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)

ax2.tick_params(axis='y', which='both', left=False)

plt.tight_layout()

plt.savefig("images/Renewable energy by type and country.png")
plt.show()

