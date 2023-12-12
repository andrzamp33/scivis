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
fig, axs = plt.subplots(1, 2, figsize=(15, 6), sharey=True)

colors_renewable = ["#aec6cf", "#c9e2b3", "#ffeaa7", "#f8c471"]
size = 1.5
axs[0].plot(years_renewable, hydro, label='Hydro', color=colors_renewable[0], linewidth=size)
axs[0].plot(years_renewable, biofuel, label='Biofuel', color=colors_renewable[1], linewidth=size)
axs[0].plot(years_renewable, solar_pv, label='Solar PV', color=colors_renewable[2], linewidth=size)
axs[0].plot(years_renewable, geothermal, label='Geothermal', color=colors_renewable[3], linewidth=size)

axs[0].set_xlabel('')
axs[0].set_ylabel('Energy generation (TWh)')
axs[0].set_title('World data on renewable power generation (1990-2017)')
matplotx.line_labels()
axs[0].grid(False)
axs[0].legend()
sns.despine()

# Codice 2: Grafico dei combustibili fossili
coal_data = pd.read_csv("coal-consumption-by-country-terawatt-hours-twh.csv", usecols=["Entity", "Year", "Coal consumption - TWh"]).rename(columns={"Coal consumption - TWh": "Consumption"})
fossil_data = pd.read_csv("fossil-fuel-primary-energy.csv", usecols=["Entity", "Year", "Fossil fuels (TWh)"]).rename(columns={"Fossil fuels (TWh)": "Consumption"})
oil_data = pd.read_csv("oil-consumption-by-country.csv", usecols=["Entity", "Year", "Oil consumption - TWh"]).rename(columns={"Oil consumption - TWh": "Consumption"})
gas_data = pd.read_csv("gas-consumption-by-country.csv", usecols=["Entity", "Year", "Gas consumption - TWh"]).rename(columns={"Gas consumption - TWh": "Consumption"})
carbon_data = pd.read_csv("low-carbon-energy-consumption.csv", usecols=["Entity", "Year", "Low-carbon energy (TWh - equivalent)"]).rename(columns={"Low-carbon energy (TWh - equivalent)": "Consumption"})
nuclear_data = pd.read_csv("primary-energy-nuclear.csv", usecols=["Entity", "Year", "Nuclear (TWh - equivalent)"]).rename(columns={"Nuclear (TWh - equivalent)": "Consumption"})

data = [coal_data, fossil_data, oil_data, gas_data, carbon_data, nuclear_data]
names = ["Coal", "Fossil fuel", "Oil", "Gas", "Low carbon", "Nuclear"]
colors = ['#FFBB99', '#935C7F', '#CDAAB4', '#B85381', '#FFD699', '#FF8B8E']

filtered_data = []

for df in data:
    filtered_df = df[(df['Entity'] == 'World') & (df['Year'] >= 1990) & (df['Year'] <= 2017)]
    filtered_data.append(filtered_df)

i = 0
for fd in filtered_data:
    axs[1].plot(fd["Year"].astype(int), fd["Consumption"], color=colors[i], label=names[i], linewidth=size)
    i += 1

matplotx.line_labels()

axs[1].set_ylabel("Energy consumption (TWh)")
axs[1].set_title("World data on non-renewable power generation (1990-2017)")

for ax in axs:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

plt.subplots_adjust(wspace=0.4)
plt.savefig("combined_plot.png")
plt.show()
