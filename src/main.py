### Imports
# Standard library
from pathlib import Path

# Third-party libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Local files


DATA_PATH: Path = Path("data\\datasample.csv")
WEEKDAYS: dict[int, str] = {
    1: "mandag",
    2: "tirdag",
    3: "onsdag",
    4: "torsdag",
    5: "fredag",
    6: "lørdag",
    7: "søndag",
}


# Matplotlib style config
plt.style.use("ggplot")


def plot_histogram(data: dict[str, list[int | float]], title: str = "Histogram", xlabel: str = "X label", ylabel: str = "Y label") -> None:
    """
    Plots a histogram from a dictionary of keys and their corresponding values.

    Args
    ----
        data: A dictionary object.
        title: The title of the histogram. Defaults to `Histogram`.
        xlabel: The label for the x-axis. Defaults to `X label`.
        ylabel: The label for the y-axis. Defaults to `Y label`.
    """
    keys = list(data.keys())
    values = list(data.values())
    plt.bar(keys, values, color="#4169E1")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def step_1() -> None:
    """
    Load data in and plot frequenli of `Frigivelsesdato` as a histogram.
    """
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    data = df["Frigivelsesdato"].value_counts().to_dict()
    plot_histogram(data, "Histogram over friveks af bestillin over datoer", "Frigivelsesdatoer", "frequns")


def step_2() -> None:
    # Vi fratage uge 52 og 53 (uge 01 i år 2025), da det er midt i juleferien, hvilket ikke er med til at give et retvisende billede for en vagtplan.
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    data = df["Frigivelsesdato"].value_counts().to_dict()
    plot_histogram(data)
    

def step_3(column: str) -> None:
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")

    for warehouse in df["Lager"].unique():
        temp_df = df[df["Lager"] == warehouse]
        data = temp_df[column].value_counts().to_dict()
        plot_histogram(data)




def step_4():
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    for warehouse in df["Lager"].unique():
        temp_df = df[df["Lager"] == warehouse]
        data = []
        for week in temp_df["Week"].unique():
            a = temp_df[temp_df["Week"] == week]
            data.append(a["Weekday"].value_counts().to_dict())
        
        days = {u[day]: [] for day in range(1, 8)}
        for value in data:
            for day in range(1, 8):
                try:
                    days[u[day]].append(value[day])
                except KeyError:
                    pass

        data = {}
        for key, value in days.items():
            data[key] = np.mean(value)


        plot_histogram(data)

def main():
    step_1()
    # step_2()
    #step_3("Frigivelsesdato")
    #step_3("Lagerområde")
    #step_4()



if __name__ == "__main__":
    main()
