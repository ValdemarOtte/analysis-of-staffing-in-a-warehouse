### Imports
# Standard library
from pathlib import Path
import csv
from datetime import datetime
from collections import Counter

# Third-party libraries
import matplotlib.pyplot as plt
import pandas as pd

# Local files


DATA_PATH: Path = Path("data\\datasample.csv")




def plot_histogram(df, column: str) -> None:
    
    data = df[column].value_counts().to_dict()
    categories = list(data.keys())
    values = list(data.values())
    plt.bar(categories, values)

    # Tilføj titler og labels
    plt.title('Histogram af dictionary')
    plt.xlabel('Dato')
    plt.ylabel('Count')
    plt.xticks(rotation=45)  # Rotér x-aksens labels for bedre læsbarhed
    plt.tight_layout()

    plt.show()



def step_1():
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    plot_histogram(df, "Frigivelsesdato")


def step_2():
    # Vi fraregne uge 52 og 53 (uge 01 i år 2025), da det er midt i juleferien, hvilket ikke er med til at give et retvisende billede af en vagtplan.
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    plot_histogram(df, "Frigivelsesdato")
    

def step_3():
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    warehourses = df["Lager"].unique()
    for warehouse in warehourses:
        temp_df = df[df["Lager"] == warehouse]
        plot_histogram(temp_df, "Frigivelsesdato")



def step_4():
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    warehourses = df["Lager"].unique()
    for warehouse in warehourses:
        temp_df = df[df["Lager"] == warehouse]
        plot_histogram(temp_df, "Lagerområde")

def main():
    # step_1()
    # step_2()
    # step_3()
    step_4()



if __name__ == "__main__":
    main()
