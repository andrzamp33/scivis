from matplotlib import pyplot as plt
import matplotx
import pandas as pd
import math

# https://www.kaggle.com/datasets/alisahad/e-waste-recycling-rate-2008-2018-europe

plt.style.use("default")

data = pd.read_csv("datasets/ewaste_europe.csv")
years = data["period"]

countries = []
values = []

for column in data.columns[1:]:
    countries.append(column)

for i in range(0, len(countries)-1):
    values.append(data[countries[i]])


average = [0] * len(years)

for i in range(0, len(years)):
    c = 0
    for j in range(0, len(values)-1):
        if not math.isnan(values[j].at[i]):
            c += 1
            average[i] += values[j].at[i]
    average[i] = average[i] / c

lw = 1

years = years[1:]

plt.plot(years, data["Germany"][1:], color = "black", label="Germany", linewidth=lw, alpha=0.8)
plt.plot(years, data["United Kingdom"][1:], color = "black", label="UK", linewidth=lw, alpha=0.8)
plt.plot(years, data["Sweden"][1:], color = "black", label="Sweden", linewidth=lw, alpha=0.8)
plt.plot(years, data["France"][1:], color = "black", label="France", linewidth=lw, alpha=0.8)
plt.plot(years, data["Spain"][1:], color = "black", label="Spain", linewidth=lw, alpha=0.8)
plt.plot(years, data["Netherlands"][1:], color = "black", label="Netherlands", linewidth=lw, alpha=0.8)

plt.plot(years, average[1:], color="#b2df8a", label="Average", linewidth=4, linestyle="--")

plt.title("E-waste of European countries")
plt.ylabel("Collection, reuse, and recycling rate (%)")

matplotx.line_labels()

ax = plt.gca()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.tick_params(axis='both', which='both', length=0)

plt.tight_layout()

plt.savefig("images/European countries e-waste.png")

plt.show()

