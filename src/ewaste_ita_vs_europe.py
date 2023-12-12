from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# Aggiungi etichette sopra le barre con i valori
def add_labels(ax, bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom', color='black', fontsize=8)

plt.style.use("default")

data = pd.read_csv("datasets/ewaste.csv", usecols=["Country", "Waste category", "WST_OPER", "UNIT", "Year", "Value"])

df_filtered = data[data['Year'].isin([2019, 2020])]

df_filtered_italy = df_filtered[df_filtered['Country'] == 'Italy']

result = df_filtered[(df_filtered['Waste category'] == 'Total waste') & (df_filtered['UNIT'] == 'KG_HAB')] \
    .groupby(['Country', "Year", 'WST_OPER'])['Value'].sum().reset_index(name='TotalKGs')

it_result = df_filtered_italy[(df_filtered_italy['Waste category'] == 'Total waste') & (df_filtered_italy['UNIT'] == 'KG_HAB')] \
    .groupby(['Country', "Year", 'WST_OPER'])['Value'].sum().reset_index(name='TotalKGs')

length = len(result) / 3  # Ogni paese ha 3 record

mkt = [result[(result['WST_OPER'] == 'MKT') & (result['Year'] == 2019)]["TotalKGs"].sum() / length,
       result[(result['WST_OPER'] == 'MKT') & (result['Year'] == 2020)]["TotalKGs"].sum() / length]
col = [result[(result['WST_OPER'] == 'COL') & (result['Year'] == 2019)]["TotalKGs"].sum() / length,
       result[(result['WST_OPER'] == 'COL') & (result['Year'] == 2020)]["TotalKGs"].sum() / length]
rcy = [result[(result['WST_OPER'] == 'RCY') & (result['Year'] == 2019)]["TotalKGs"].sum() / length,
       result[(result['WST_OPER'] == 'RCY') & (result['Year'] == 2020)]["TotalKGs"].sum() / length]

mkt_it = [it_result[(it_result['WST_OPER'] == 'MKT') & (it_result['Year'] == 2019)]["TotalKGs"].sum(),
          it_result[(it_result['WST_OPER'] == 'MKT') & (it_result['Year'] == 2020)]["TotalKGs"].sum()]
col_it = [it_result[(it_result['WST_OPER'] == 'COL') & (it_result['Year'] == 2019)]["TotalKGs"].sum(),
          it_result[(it_result['WST_OPER'] == 'COL') & (it_result['Year'] == 2020)]["TotalKGs"].sum()]
rcy_it = [it_result[(it_result['WST_OPER'] == 'RCY') & (it_result['Year'] == 2019)]["TotalKGs"].sum(),
          it_result[(it_result['WST_OPER'] == 'RCY') & (it_result['Year'] == 2020)]["TotalKGs"].sum()]

years = ["2019", "2020"]
type = ["Produced", "Collected", "Recycled"]
x_indexes = np.arange(len(years))
x_indexes_comp = np.arange(len(type))
width = 0.065

fig, axs = plt.subplots(2, 2, figsize=(12, 8))

prod_color = "#d2a073"
col_color = "#c8a58f"
rcy_color = "#d9cdba"


# Primo grafico
bar1 = axs[0, 0].bar(x_indexes - width, mkt, width=width, color=prod_color, label="Newly produced electronics", edgecolor="black", linewidth=0.1)
bar2 = axs[0, 0].bar(x_indexes, col, width=width, color=col_color, label="Collected electronic waste", edgecolor="black", linewidth=0.1)
bar3 = axs[0, 0].bar(x_indexes + width, rcy, width=width, color=rcy_color, label="Recycled electronic waste", edgecolor="black", linewidth=0.1)
axs[0, 0].set_ylabel("Kilograms per capita")
axs[0, 0].set_xticks(ticks=x_indexes)
axs[0, 0].set_xticklabels(years)
axs[0, 0].set_title("Average E-waste recycling in european countries")

axs[0, 0].tick_params(left=False, bottom=False)

add_labels(axs[0, 0], bar1)
add_labels(axs[0, 0], bar2)
add_labels(axs[0, 0], bar3)

# Secondo grafico
bar1 = axs[0, 1].bar(x_indexes - width, mkt_it, width=width, color=prod_color, edgecolor="black", linewidth=0.1)
bar2 = axs[0, 1].bar(x_indexes, col_it, width=width, color=col_color, edgecolor="black", linewidth=0.1)
bar3 = axs[0, 1].bar(x_indexes + width, rcy_it, width=width, color=rcy_color, edgecolor="black", linewidth=0.1)
axs[0, 1].set_ylabel("Kilograms per capita")
axs[0, 1].set_xticks(ticks=x_indexes)
axs[0, 1].set_xticklabels(years)
axs[0, 1].set_title("E-waste recycling in Italy")

axs[0, 1].tick_params(left=False, bottom=False)

add_labels(axs[0, 1], bar1)
add_labels(axs[0, 1], bar2)
add_labels(axs[0, 1], bar3)

# Terzo grafico
bar1 = axs[1, 0].bar(x_indexes_comp - width, [mkt_it[0], col_it[0], rcy_it[0]], width=width, color=[prod_color, col_color, rcy_color], edgecolor="black", linewidth=0.1)
bar2 = axs[1, 0].bar(x_indexes_comp, [mkt[0], col[0], rcy[0]], width=width, color=[prod_color, col_color, rcy_color], edgecolor="black", linewidth=0.1)
axs[1, 0].set_ylabel("Kilograms per capita")
axs[1, 0].set_xticks(ticks=x_indexes_comp)
axs[1, 0].set_xticklabels(type)
axs[1, 0].set_title("2019: Italy vs Europe average")

axs[1, 0].tick_params(left=False, bottom=False)


# Quarto grafico
bar1 = axs[1, 1].bar(x_indexes_comp - width, [mkt_it[1], col_it[1], rcy_it[1]], width=width, color=[prod_color, col_color, rcy_color], edgecolor="black", linewidth=0.1)
bar2 = axs[1, 1].bar(x_indexes_comp, [mkt[1], col[1], rcy[1]], width=width, color=[prod_color, col_color, rcy_color], edgecolor="black", linewidth=0.1)
axs[1, 1].set_ylabel("Kilograms per capita")
axs[1, 1].set_xticks(ticks=x_indexes_comp)
axs[1, 1].set_xticklabels(type)
axs[1, 1].set_title("2020: Italy vs Europe average")

axs[1, 1].tick_params(left=False, bottom=False)

axs[0, 0].set_yticks([])
axs[0, 1].set_yticks([])

# Rimuovo i bordi da ogni subplot
for ax in axs.flat:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')

# Legenda
fig.legend([bar1, bar2, bar3], ["Newly produced electronics", "Collected electronic waste", "Recycled electronic waste"],
           loc="upper center", bbox_to_anchor=(0.5, 0), ncol=3, fontsize="small")

plt.tight_layout()

plt.savefig("images/E-waste: Italy vs Europe.png", bbox_inches="tight")
plt.show()

