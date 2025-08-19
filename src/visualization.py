import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_class_distribution(df, target_col):
    counts = df[target_col].value_counts()
    fig = px.bar(counts, x=counts.index, y=counts.values,
                 text=counts.values, title=f"Distribution of {target_col}")
    fig.show()

def plot_numeric_hist(df, col):
    plt.figure(figsize=(6,4))
    plt.hist(df[col].dropna(), bins=40, alpha=0.85, color="skyblue", edgecolor="black")
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

def correlation_heatmap(df):
    plt.figure(figsize=(12,8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Feature Correlation Heatmap")
    plt.show()
