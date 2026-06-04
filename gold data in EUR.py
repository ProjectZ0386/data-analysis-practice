import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, AutoMinorLocator
df=pd.read_csv('Daily.csv')

fig, ax = plt.subplots(figsize=(15, 7))
ax.plot(df["Date"], df["EUR"],color="green")

# จำกัดจำนวนป้ายแกน X สูงสุด 20 ป้าย
ax.xaxis.set_major_locator(MaxNLocator(nbins=20))
ax.yaxis.set_major_locator(MaxNLocator(nbins=15))

plt.xticks(rotation=45, ha='right')
plt.xlabel("Date", fontsize=17)
plt.ylabel("EUR", fontsize=17)
plt.title("Price of Gold Data", fontsize=20)
plt.legend(["EUR"], fontsize=18)
plt.tight_layout()
plt.show()