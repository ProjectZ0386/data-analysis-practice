import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, AutoMinorLocator 

class GoldAnalyzer:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        for col in self.df.columns:
            if col != "Date":
                self.df[col] = pd.to_numeric(
                    self.df[col].astype(str).str.replace(",",""),errors="coerce"
                    )
    
    def plot_currencies(self, currencies):
        for currency in currencies:
            fig, ax = plt.subplots(figsize=(15,7))
            plt.plot(self.df["Date"], self.df[currency], label=currency)
            
            ax.xaxis.set_major_locator(MaxNLocator(nbins=20))
            ax.yaxis.set_major_locator(MaxNLocator(nbins=15))
        
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.xlabel("Date", fontsize=15)
            plt.ylabel("Price", fontsize=15)
            plt.title(f"Gold Price in {currency} Over Time", fontsize=20)
            plt.legend(fontsize=20)
            plt.show()
    
    def summary(self, summary):
        print("\n"+"="*50)
        print("Gold Price Analysis Summary")
        print("="*50)
        for column in summary:
            if column != "Date":
                print(f"\n{column} statistics")
                print("-"*30)
                print(f"{'Maximum':<15}:{self.df[column].max():.2f}")
                print(f"{'Minimum':<15}:{self.df[column].min():.2f}")
                print(f"{'Average':<15}:{self.df[column].mean():.2f}")
                print(f"{'Median':<15}:{self.df[column].median():.2f}")


analyzer = GoldAnalyzer("Daily.csv")
analyzer.plot_currencies(["USD", "EUR"])
analyzer.summary(["USD", "EUR"])