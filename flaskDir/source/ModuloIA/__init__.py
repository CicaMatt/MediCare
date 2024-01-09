import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
df = pd.read_csv("heart.csv")
if __name__ == "__main__":
    """
    fig, axes = plt.subplots(3, 2, figsize=(15, 12))

    sns.histplot(df['age'], kde=True, ax=axes[0, 0])
    axes[0, 0].set_title('Age Distribution')

    sns.countplot(x='sex', data=df, ax=axes[0, 1])
    axes[0, 1].set_title('Sex Distribution (0 = Female, 1 = Male)')

    sns.histplot(df['chol'], kde=True, ax=axes[1, 0])
    axes[1, 0].set_title('Cholesterol Level Distribution')

    sns.histplot(df['trtbps'], kde=True, ax=axes[1, 1])
    axes[1, 1].set_title('Resting Blood Pressure Distribution')

    sns.histplot(df['oldpeak'], kde=True, ax=axes[2,0])
    axes[2, 0].set_title('Old Peak Distribution')
    plt.savefig('figures')

    plt.tight_layout()

    # Correlation Analysis
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=False, fmt=".2f", cmap='viridis')
    plt.title("Correlation Matrix of Heath Disease")

    plt.show()

    numeric_var=['age','trtbps','chol','thalachh','oldpeak']
    numeric_axis_name = ["Age of the Patient", "Resting Blood Pressure", "Cholesterol", "Maximum Heart Rate Achieved", "ST Depression"]

    numeric_var.append("HeartDisease")

    title_font = {"family": "arial", "color": "darkred", "weight": "bold", "size": 15}
    axis_font = {"family": "arial", "color": "darkblue", "weight": "bold", "size": 13}

    for i, z in list(zip(numeric_var, numeric_axis_name)):
        graph = sns.FacetGrid(df[numeric_var], hue="HeartDisease", height=5, xlim=((df[i].min() - 10), (df[i].max() + 10)))
        graph.map(sns.kdeplot, i, fill=True)
        graph.add_legend()

        plt.title(i, fontdict=title_font)
        plt.xlabel(z, fontdict=axis_font)
        plt.ylabel("Density", fontdict=axis_font)

        plt.tight_layout()
        plt.show()
    """
    """
#Istogramma del sesso
    fig=px.histogram(df,
                 x="sex",
                 color="HeartDisease",
                 hover_data=df.columns,
                 barmode="group")
    fig.show()
    """
    """
#Istogramma dolore al petto
    fig=px.histogram(df,
                 x="cp",
                 color="HeartDisease",
                 hover_data=df.columns,
                 barmode="group"
                )
    fig.show()
    """
    """
#Istogramma livello glucosio nel sangue
    fig=px.histogram(df,
                 x="fbs",
                 color="HeartDisease",
                 hover_data=df.columns,
                 barmode="group")

    fig.show()
    """

    """
#Istrogramma curva elettrocardiogramma
    fig=px.histogram(df,
                 x="restecg",
                 color="HeartDisease",
                 hover_data=df.columns,
                 barmode="group")
    fig.show()
    """

    """
#Istrogramma affaticamento da esercizio
    fig=px.histogram(df,
                 x="exng",
                 color="HeartDisease",
                 hover_data=df.columns,
                 barmode="group")
    fig.show()
    """
    """
#Istrogramma tendenza del segmento st
    fig=px.histogram(df,
                 x="slp",
                 color="HeartDisease",
                 hover_data=df.columns,
                 barmode="group")
    fig.show()
    """
    """
#Istrogramma vasi sanguigni colorati dalla fluoroscopia
    fig=px.histogram(df,
                 x="caa",
                 color="HeartDisease",
                 hover_data=df.columns,
                 barmode="group")
    fig.show()
    """
    """
#Istorgramma della Thall
    fig=px.histogram(df,
                 x="thall",
                 color="HeartDisease",
                 hover_data=df.columns,
                 barmode="group")
    fig.show()
    """

    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=False, fmt=".2f", cmap='viridis')
    plt.title("Correlation Matrix of Heath Disease")

    plt.savefig("Matrice.png")
