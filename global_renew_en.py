import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Leggi il dataset
df = pd.read_csv('global-data-on-sustainable-energy.csv')

# Leggi il CSV contenente le informazioni sui continenti
continents_df = pd.read_csv('continents2.csv')

# Unisci i dati del tuo dataframe con le informazioni sui continenti
df = pd.merge(df, continents_df, left_on='Entity', right_on='name', how='left')

# Converti la colonna 'Renewable energy share in the total final energy consumption (%)' in numeri
df['Renewable energy share in the total final energy consumption (%)'] = pd.to_numeric(df['Renewable energy share in the total final energy consumption (%)'], errors='coerce')

# Carica i dati dei confini dei paesi e dei continenti
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Unisci il dataset con i confini del mondo basandosi sulle coordinate geografiche
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# Esegui l'intersezione per ottenere il continente di ciascun punto
gdf = gpd.sjoin(gdf, world[['geometry', 'continent']], op='within', how='left')

# Inizializza la figura
fig, ax = plt.subplots()

# Per ciascun continente
for continent, continent_data in gdf.groupby('continent'):
    # Aggrega i dati a livello di continente
    aggregated_data = continent_data.groupby('Year')['Renewable energy share in the total final energy consumption (%)'].mean()

    
    # Plotta i dati con linee continue
    line, = ax.plot(aggregated_data.index, aggregated_data.values, label=None, linestyle='-')

    # Aggiungi il nome del continente vicino al primo e all'ultimo punto della linea
    ax.annotate(continent, (aggregated_data.index[0], aggregated_data.values[0]),
                textcoords="offset points", xytext=(0,5), ha='left', fontsize=8, color=line.get_color())

# Aggiungi etichette e titoli al grafico
ax.set_xlabel('')
ax.set_ylabel('Renewable energy share in the total final energy consumption (%)')
ax.set_title('Renewable energy share in the total final energy consumption (%) by Continent')

# Imposta il formato degli anni su 4 cifre
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))

# Rimuovi i bordi dalla figura e dagli assi
ax.set_frame_on(False)
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# Mostra il grafico
plt.show()
