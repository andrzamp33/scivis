import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from io import StringIO

# Leggi i dati
data = """
Year,Hydro(TWh),Biofuel(TWh),Solar PV (TWh),Geothermal (TWh)
1990,2191.67,3.88,0.09,36.42
1991,2268.63,4.19,0.1,37.39
1992,2267.16,4.63,0.12,39.3
1993,2397.67,5.61,0.15,40.23
1994,2419.73,7.31,0.17,41.05
1995,2545.96,7.95,0.19,39.89
1996,2583.18,9.45,0.22,42.18
1997,2614.54,12.08,0.27,42.38
1998,2628.63,16.07,0.35,45.35
1999,2636.26,21.52,0.61,48.66
2000,2695.85,31.34,0.99,51.98
2001,2638.2,38.45,1.32,51.57
2002,2711.12,52.85,1.58,52.29
2003,2726.33,64.23,2.01,54.09
2004,2894.22,84.43,2.66,56.5
2005,3019.5,103.92,3.92,58.28
2006,3124.34,133.05,5.52,59.61
2007,3165.71,170.83,7.47,62.29
2008,3285.59,221.05,11.92,64.91
2009,3338.82,277.44,20.04,67.03
2010,3530.72,341.38,32.22,68.1
2011,2603.78,436.01,63.76,69.29
2012,3765.96,525.04,99.03,70.27
2013,2898.28,646.36,139.64,71.74
2014,3976.01,718.07,190.25,77.52
2015,3989.28,838.31,250.75,80.56
2016,4162.26,958.15,329.14,82.18
2017,4197.29,1127.31,443.55,85.34
"""

# Leggi i dati dallo string io
df = pd.read_csv(StringIO(data))

# Estrai i dati
years = df['Year']
hydro = df['Hydro(TWh)']
biofuel = df['Biofuel(TWh)']
solar_pv = df['Solar PV (TWh)']
geothermal = df['Geothermal (TWh)']

# Attiva lo stile 
plt.style.use("default")

# Plotting
plt.figure(figsize=(10, 6))

# Colori distinti per ciascuna linea
colors = ["#aec6cf", "#c9e2b3", "#ffeaa7","#f8c471"]

size = 4
plt.plot(years, hydro, label='Hydro', marker='.', color=colors[0], linewidth= size)
plt.plot(years, biofuel, label='Biofuel', marker='.', color=colors[1], linewidth= size)
plt.plot(years, solar_pv, label='Solar PV', marker='.', color=colors[2], linewidth= size)
plt.plot(years, geothermal, label='Geothermal', marker='.', color=colors[3], linewidth= size)

# Aggiungi etichette e titoli al grafico
plt.xlabel('', fontsize=18)
plt.ylabel('Energy Generation (TWh)', fontsize=16)
plt.title('Renewable Power Generation (1990-2017)', fontsize=20)
plt.legend()

# Rimuovi griglie
plt.grid(False)

# Rimuovi i bordi
sns.despine()

# Mostra il grafico
plt.show()
