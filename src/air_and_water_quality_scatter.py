import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.colors as mcolors

# Carica il file CSV in un DataFrame
file_name = 'datasets/cities_air_quality_water_pollution.csv'

df = pd.read_csv(file_name)

df[" WaterPollution"] = 100 - df[" WaterPollution"]

# Grafico a dispersione con matplotlib
#cmap = mcolors.LinearSegmentedColormap.from_list('custom_gray', ['#000000', '#b7b7b7'])
plt.figure(figsize=(10, 6))
colors = (df[" AirQuality"] + df[" WaterPollution"])/2
#scatter = plt.scatter(x=df[' AirQuality'], y=df[' WaterPollution'], c=colors, cmap=cmap, s=5)
scatter = plt.scatter(x=df[' AirQuality'], y=df[' WaterPollution'], c=colors, cmap="cividis", s=7)
colorbar = plt.colorbar(scatter, ticks = [0, 100], label = "General combined quality")
colorbar.ax.yaxis.set_ticks_position('none')  # Rimuovi solo le tacchette dalla colorbar
plt.title('Worldwide cities distribution of air and water quality')
plt.xlabel('Air quality')
plt.ylabel('Water quality')
ax = plt.gca()

# Rimuovi i bordi del grafico
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Rendi non visibili le tacchette sull'asse x e y
ax.tick_params(axis='both', which='both', length=0)

plt.savefig("images/Air and water quality scatterplot.png")
plt.show()
