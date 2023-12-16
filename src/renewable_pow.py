import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotx

# Codice 1: Grafico delle energie rinnovabili
df_renewable = pd.read_csv("renewable_en.csv")

years_renewable = df_renewable['Year']
hydro = df_renewable['Hydro(TWh)']
biofuel = df_renewable['Biofuel(TWh)']
solar_pv = df_renewable['Solar PV (TWh)']
geothermal = df_renewable['Geothermal (TWh)']

plt.style.use("default")

colors_renewable = ["#aec6cf", "#c9e2b3", "#ffe97d", "#f8c471"]
size = 4
plt.plot(years_renewable, hydro, label='Hydro', marker='.', color=colors_renewable[0], linewidth=size)
plt.plot(years_renewable, biofuel, label='Biofuel', marker='.', color=colors_renewable[1], linewidth=size)
plt.plot(years_renewable, solar_pv, label='Solar PV', marker='.', color=colors_renewable[2], linewidth=size)
plt.plot(years_renewable, geothermal, label='Geothermal', marker='.', color=colors_renewable[3], linewidth=size)

plt.xlabel('')
plt.ylabel('Energy generation (TWh)')
plt.title('World data on renewable power generation (1990-2017)')
matplotx.line_labels()
plt.grid(False)
sns.despine()
plt.gcf().set_size_inches(len(years_renewable) // 2, 6)

plt.savefig("renewable_plot.png")
plt.show()
