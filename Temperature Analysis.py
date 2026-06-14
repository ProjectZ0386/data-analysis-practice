import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, AutoMinorLocator

class temperatureAnalysis:
    def __init__(self, file):
        self.df = pd.read_csv(file)
        self.df['dt'] = pd.to_datetime(self.df['dt'])

    def plot_compare (self,cities):
        fig, ax = plt.subplots(figsize=(15, 7))

        color = ["red","blue"]

        for city, color in zip(cities, color):
            df_city = self.df[self.df['City'] == city]
            yearly = df_city.groupby(df_city['dt'].dt.year)['AverageTemperature'].mean()
            ax.plot(yearly.index ,yearly.values ,label=city, color=color)

        plt.xlabel("Year",fontsize=15)
        plt.ylabel("Avg Temperature",fontsize=15)
        plt.title("Yearly Average Temperature Comparison",fontsize=20)
        plt.legend()
        plt.grid(True)
        plt.show()

analyzer =temperatureAnalysis('GlobalLandTemperaturesByCity.csv')
analyzer.plot_compare(['Bangkok','Tokyo'])