import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def get_stats(df):
    numeric = df.select_dtypes(include='number')
    return pd.DataFrame({
        'Mean': numeric.mean(),
        'Median': numeric.median(),
        'Mode': numeric.mode().iloc[0]
    })

def plot_histograms(df):
    figs = []
    numeric = df.select_dtypes(include='number')
    for col in numeric.columns:
        fig, ax = plt.subplots()
        sns.histplot(numeric[col], kde=True, ax=ax, color='skyblue')
        ax.set_title(f"{col} Distribution")
        figs.append(fig)
    return figs
