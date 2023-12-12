 import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotx

# Codice 1: Grafico delle energie rinnovabili
df_renewable = pd.read_csv("datasets/renewable_en.csv")

years_renewable = df_renewable['Year']
hydro = df_renewable['Hydro(TWh)']
biofuel = df_renewable['Biofuel(TWh)']
solar_pv = df_renewable['Solar PV (TWh)']
geothermal = df_renewable['Geothermal (TWh)']

plt.style.use("default")
plt.figure(figsize=(15, 6))

colors_renewable = ["#aec6cf", "#c9e2b3", "#ffe97d", "#f8c471"]
size = 4
plt.subplot(1, 2, 1)

plt.plot(years_renewable, hydro, label='Hydro', marker='.', color=colors_renewable[0], linewidth=size)
plt.plot(years_renewable, biofuel, label='Biofuel', marker='.', color=colors_renewable[1], linewidth=size)
plt.plot(years_renewable, solar_pv, label='Solar PV', marker='.', color=colors_renewable[2], linewidth=size)
plt.plot(years_renewable, geothermal, label='Geothermal', marker='.', color=colors_renewable[3], linewidth=size)

plt.xlabel('')
plt.ylabel('Energy generation (TWh)')
plt.title('World data on renewable power generation (1990-2017)')
matplotx.line_labels()
#plt.legend()
plt.grid(False)
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

plt.subplot(1, 2, 2)

i = 0
for fd in filtered_data:
    plt.plot(fd["Year"].astype(int), fd["Consumption"], color=colors[i], label=names[i], linewidth=4)
    i += 1

matplotx.line_labels()

plt.ylabel("Energy consumption (TWh)")
plt.title("World data on non-renewable power generation (1990-2017)")

ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.subplots_adjust(wspace=0.4)
plt.savefig("images/Renewable vs non-renewable energy generation.png")
plt.show()

